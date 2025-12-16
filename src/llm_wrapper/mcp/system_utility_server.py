# src/llm_wrapper/mcp/system_utility_server.py

import asyncio
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
import os

from mcp.server.stdio import StdioServer
from mcp.types import Tool, CallToolResult
from pydantic import BaseModel, Field

# Define a sandbox root to restrict file operations
# This should ideally be configured via an environment variable or config file
# For now, we'll use a default relative path
DEFAULT_SANDBOX_ROOT = Path("./llm_sandbox").resolve() 

class SafeWriteInput(BaseModel):
    """Input schema for the safe_write tool."""
    file_path: str = Field(..., description="The path to the file to write (relative to sandbox).")
    content: str = Field(..., description="The content to write to the file.")
    overwrite: bool = Field(False, description="Whether to overwrite the file if it exists.")

class ReadPathInput(BaseModel):
    """Input schema for the read_path tool."""
    file_path: str = Field(..., description="The path to the file to read (relative to sandbox).")
    limit: Optional[int] = Field(None, description="Optional: Maximum number of lines to read for text files.")
    offset: Optional[int] = Field(None, description="Optional: 0-based line number to start reading from.")

class SystemUtilityServer:
    """
    An MCP server providing basic sandboxed system utilities to LLMs.
    Includes file operations (read/write) within a designated sandbox root.
    """
    def __init__(self, sandbox_root: Optional[Path] = None):
        self.sandbox_root = (sandbox_root or DEFAULT_SANDBOX_ROOT).resolve()
        self.sandbox_root.mkdir(parents=True, exist_ok=True) # Ensure sandbox root exists
        print(f"SystemUtilityServer initialized with sandbox root: {self.sandbox_root}")

        self.mcp_server = StdioServer(
            name="system_utility",
            description="Provides sandboxed system utilities, like file operations.",
            tools=[
                Tool(
                    name="safe_write",
                    description="Writes content to a file within the designated sandbox root.",
                    input_schema=SafeWriteInput.model_json_schema()
                ),
                Tool(
                    name="read_path",
                    description="Reads content from a file within the designated sandbox root.",
                    input_schema=ReadPathInput.model_json_schema()
                ),
            ]
        )
        self.mcp_server.register_tool_function("safe_write", self._safe_write_tool)
        self.mcp_server.register_tool_function("read_path", self._read_path_tool)

    def _get_safe_path(self, relative_path: str) -> Optional[Path]:
        """
        Validates that the target path is within the sandbox root.
        Returns the absolute Path if safe, None otherwise.
        """
        try:
            target_path = (self.sandbox_root / relative_path).resolve()
        except Exception: # Handle cases where path is invalid, e.g., contains null bytes
            return None
        
        # Ensure the resolved path is still a subpath of the sandbox root
        if not target_path.is_relative_to(self.sandbox_root):
            print(f"SECURITY ALERT: Attempt to access path outside sandbox: {target_path}")
            return None
        return target_path

    async def _safe_write_tool(self, input: SafeWriteInput) -> CallToolResult:
        """MCP tool to write content to a file within the sandbox."""
        safe_path = self._get_safe_path(input.file_path)
        if not safe_path:
            return CallToolResult(content=f"Error: Path '{input.file_path}' is outside sandbox or invalid.", success=False)
        
        if safe_path.exists() and not input.overwrite:
            return CallToolResult(content=f"Error: File '{input.file_path}' already exists and overwrite is false.", success=False)

        try:
            safe_path.parent.mkdir(parents=True, exist_ok=True) # Ensure parent directories exist
            safe_path.write_text(input.content, encoding='utf-8')
            return CallToolResult(content=f"Successfully wrote to '{input.file_path}'.", success=True)
        except Exception as e:
            return CallToolResult(content=f"Error writing to '{input.file_path}': {e}", success=False)

    async def _read_path_tool(self, input: ReadPathInput) -> CallToolResult:
        """MCP tool to read content from a file within the sandbox."""
        safe_path = self._get_safe_path(input.file_path)
        if not safe_path:
            return CallToolResult(content=f"Error: Path '{input.file_path}' is outside sandbox or invalid.", success=False)
        
        if not safe_path.is_file():
            return CallToolResult(content=f"Error: File '{input.file_path}' not found or is not a file.", success=False)

        try:
            with open(safe_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            start_line = input.offset if input.offset is not None else 0
            end_line = start_line + (input.limit if input.limit is not None else len(lines))
            
            content_lines = lines[start_line:end_line]
            content = "".join(content_lines)

            truncated = len(lines) > len(content_lines)
            
            return CallToolResult(
                content=f"Successfully read from '{input.file_path}'. {"(Truncated)" if truncated else ''}", 
                success=True,
                resources=[CallToolResult(data=content, mime_type="text/plain")]
            )
        except Exception as e:
            return CallToolResult(content=f"Error reading from '{input.file_path}': {e}", success=False)

    async def run_forever(self):
        """Starts the MCP StdioServer."""
        print(f"System Utility Server starting, Sandbox Root: {self.sandbox_root}")
        await self.mcp_server.run_forever()


if __name__ == "__main__":
    import shutil

    async def main():
        print("--- Testing SystemUtilityServer ---")
        temp_sandbox_root = Path("./temp_llm_sandbox").resolve() # Use a different name for temp sandbox
        
        if temp_sandbox_root.exists():
            shutil.rmtree(temp_sandbox_root) # Clean up previous test run
        temp_sandbox_root.mkdir()

        server = SystemUtilityServer(sandbox_root=temp_sandbox_root)

        try:
            # Test safe_write
            print("\nCalling safe_write tool:")
            write_input = SafeWriteInput(file_path="test_dir/hello.txt", content="Hello, LLM!", overwrite=True)
            write_result = await server._safe_write_tool(write_input)
            print(f"Write Result: {write_result.content}, Success: {write_result.success}")

            # Test read_path
            print("\nCalling read_path tool:")
            read_input = ReadPathInput(file_path="test_dir/hello.txt")
            read_result = await server._read_path_tool(read_input)
            print(f"Read Result: {read_result.content}, Success: {read_result.success}")
            if read_result.resources:
                print(f"Read Content: {read_result.resources[0].data}")

            # Test safe_write (no overwrite)
            print("\nCalling safe_write tool (no overwrite):")
            write_input_no_overwrite = SafeWriteInput(file_path="test_dir/hello.txt", content="New content.")
            write_result_no_overwrite = await server._safe_write_tool(write_input_no_overwrite)
            print(f"Write (no overwrite) Result: {write_result_no_overwrite.content}, Success: {write_result_no_overwrite.success}")

            # Test safe_write (outside sandbox - should fail)
            print("\nCalling safe_write tool (outside sandbox):")
            write_input_unsafe = SafeWriteInput(file_path="../../../unsafe.txt", content="Malicious content.", overwrite=True)
            write_result_unsafe = await server._safe_write_tool(write_input_unsafe)
            print(f"Unsafe Write Result: {write_result_unsafe.content}, Success: {write_result_unsafe.success}")

            # Test read_path (outside sandbox - should fail)
            print("\nCalling read_path tool (outside sandbox):")
            read_input_unsafe = ReadPathInput(file_path="../../../some_system_file.txt")
            read_result_unsafe = await server._read_path_tool(read_input_unsafe)
            print(f"Unsafe Read Result: {read_result_unsafe.content}, Success: {read_result_unsafe.success}")
            
            # Test reading with limit and offset
            print("\nCreating multi-line file for limit/offset test:")
            multi_line_content = "\n".join([f"Line {i}" for i in range(20)])
            write_input_multi = SafeWriteInput(file_path="multi_line.txt", content=multi_line_content, overwrite=True)
            await server._safe_write_tool(write_input_multi)

            print("\nReading multi_line.txt with limit=5, offset=10:")
            read_input_limited = ReadPathInput(file_path="multi_line.txt", limit=5, offset=10)
            read_result_limited = await server._read_path_tool(read_input_limited)
            print(f"Read Limited Result: {read_result_limited.content}, Success: {read_result_limited.success}")
            if read_result_limited.resources:
                print(f"Read Limited Content:\n{read_result_limited.resources[0].data}")


        except Exception as e:
            print(f"An error occurred during SystemUtilityServer test: {e}")
        finally:
            if temp_sandbox_root.exists():
                shutil.rmtree(temp_sandbox_root)
                print(f"Cleaned up temporary sandbox: {temp_sandbox_root}")
            
    asyncio.run(main())
