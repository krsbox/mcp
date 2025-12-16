import asyncio
from contextlib import asynccontextmanager
from typing import Dict, List, Any, Optional
from pathlib import Path

# Import actual mcp types and client session
from mcp.client.stdio import stdio_client
from mcp.types import Tool, CallToolResult
from mcp import ClientSession, StdioServerParameters

# Import our abstract base class
from src.llm_wrapper.mcp.interfaces import MCPClient 

class StdioMCPClient(MCPClient):
    """
    An MCPClient implementation for connecting to a local MCP server via stdio.
    This client manages the lifecycle of the subprocess and the MCP session.
    """
    def __init__(self, server_params: StdioServerParameters):
        self.server_params = server_params
        self._session: Optional[ClientSession] = None
        self._process: Optional[asyncio.subprocess.Process] = None

    @asynccontextmanager
    async def connect(self):
        """
        Establishes a connection to the stdio server and yields the client session.
        This should be used as an async context manager.
        """
        if self._session:
            raise RuntimeError("StdioMCPClient is already connected.")

        print(f"Starting stdio client with command: {' '.join(self.server_params.command_line)}")
        
        try:
            # stdio_client is an async context manager that returns a ClientSession and the process
            async with stdio_client(self.server_params) as (session, process):
                self._session = session
                self._process = process
                print(f"Stdio client connected. Process PID: {self._process.pid}")
                yield self
            
            # Ensure session and process are cleaned up after exiting the context
            self._session = None
            self._process = None
            print("Stdio client disconnected gracefully.")
        except Exception as e:
            print(f"Error connecting StdioMCPClient: {e}")
            if self._process:
                await self.disconnect() # Attempt to clean up process if it started and failed
            raise # Re-raise the exception


    async def list_tools(self) -> List[Tool]:
        """
        Lists all available tools from the connected stdio server.
        Requires an active session.
        """
        if not self._session:
            raise RuntimeError("StdioMCPClient is not connected. Call connect() first.")
        
        response = await self._session.list_tools()
        return response.tools

    async def call_tool(self, name: str, arguments: Dict[str, Any]) -> CallToolResult:
        """
        Executes a specific tool on the connected stdio server.
        Requires an active session.
        """
        if not self._session:
            raise RuntimeError("StdioMCPClient is not connected. Call connect() first.")
        
        return await self._session.call_tool(name, arguments)

    async def disconnect(self):
        """
        Explicitly disconnects the client and terminates the subprocess.
        This method is primarily for explicit control if not using the 'connect'
        async context manager, or for error cleanup.
        """
        if self._process and self._process.returncode is None:
            print(f"Terminating stdio client process (PID: {self._process.pid})...")
            self._process.terminate()
            try:
                await asyncio.wait_for(self._process.wait(), timeout=5)
                print(f"Process {self._process.pid} terminated gracefully.")
            except asyncio.TimeoutError:
                print(f"Process {self._process.pid} did not terminate gracefully, killing...")
                self._process.kill()
                await self._process.wait() # Wait for it to be truly dead
                print(f"Process {self._process.pid} killed.")
            except Exception as e:
                print(f"Error during process termination: {e}")
            finally:
                self._process = None
                self._session = None
                print("Stdio client fully disconnected and process cleaned up.")
        elif self._session:
            # If session exists but process is already gone
            self._session = None
            print("Stdio client session cleared (process already terminated or not started).")

# --- Test Utilities (for development and demonstration) ---
async def create_dummy_mcp_server_script(path: Path):
    """Creates a dummy MCP server Python script for testing."""
    dummy_server_content = """
import asyncio
from mcp.server.stdio import StdioServer
from mcp.types import Tool, CallToolResult
from pydantic import BaseModel

class MyToolInput(BaseModel):
    message: str

async def my_tool_function(input: MyToolInput) -> CallToolResult:
    print(f"Dummy server received message for my_tool: {input.message}", flush=True)
    return CallToolResult(content=f"Server says: '{input.message}'")

class EchoToolInput(BaseModel):
    text: str

async def echo_tool_function(input: EchoToolInput) -> CallToolResult:
    print(f"Dummy server echoing for echo_tool: {input.text}", flush=True)
    return CallToolResult(content=input.text)

my_server = StdioServer(
    name="my_test_server",
    tools=[
        Tool(name="my_tool", description="A test tool", input_schema=MyToolInput.model_json_schema()),
        Tool(name="echo_tool", description="Echoes text", input_schema=EchoToolInput.model_json_schema())
    ]
)

my_server.register_tool_function("my_tool", my_tool_function)
my_server.register_tool_function("echo_tool", echo_tool_function)

if __name__ == "__main__":
    print("Dummy MCP server starting...", flush=True)
    asyncio.run(my_server.run_forever())
    print("Dummy MCP server stopped.", flush=True)
"""
    if not path.is_file():
        path.write_text(dummy_server_content)
        print(f"Created dummy MCP server script: {path}")

async def cleanup_dummy_mcp_server_script(path: Path):
    """Cleans up the dummy MCP server Python script."""
    if path.is_file():
        path.unlink()
        print(f"Cleaned up dummy MCP server script: {path}")

if __name__ == "__main__":
    async def test_stdio_client():
        print("--- Testing StdioMCPClient ---")
        dummy_server_path = Path("my_mcp_server.py")
        await create_dummy_mcp_server_script(dummy_server_path)
        
        server_params = StdioServerParameters(command_line=["python", str(dummy_server_path)])
        client = StdioMCPClient(server_params)

        try:
            async with client.connect() as connected_client:
                print("\nListing tools:")
                tools = await connected_client.list_tools()
                for tool in tools:
                    print(f"- {tool.name}: {tool.description}")

                print("\nCalling 'my_tool':")
                result = await connected_client.call_tool("my_tool", {"message": "Hello from client!"})
                print(f"Result for my_tool: {result.content}")

                print("\nCalling 'echo_tool':")
                echo_result = await connected_client.call_tool("echo_tool", {"text": "This is an echo test."})
                print(f"Result for echo_tool: {echo_result.content}")

        except Exception as e:
            print(f"An error occurred during client interaction: {e}")
        finally:
            await cleanup_dummy_mcp_server_script(dummy_server_path)

    asyncio.run(test_stdio_client())
