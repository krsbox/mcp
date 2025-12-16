#!/bin/bash

# simple_backup.sh: Creates timestamped copies of specified files/directories
# and places them in a local backup folder.
# This script is designed for light, local backup, allowing manual inspection/restoration.

# Define the directory where backups will be stored.
# This directory should be listed in .gitignore.
BACKUP_DIR="backups/simple_copies"
mkdir -p "$BACKUP_DIR"

# Define the files/directories to be "backed up" by copying.
# These should be critical configuration files or generated assets that
# change frequently but are not necessarily committed on every small change.
# Add/remove paths as needed.
declare -a ITEMS_TO_BACKUP=(
    "workspace-automation/file_registry.json"
    "SYSTEM_INVENTORY.md"
    "CHANGELOG.md"
    # Example: If there's a critical configuration file that gets updated by tooling
    # "config/mcp.json"
    # Example: If there's a directory of logs or data you want to snapshot
    # "data/important_logs"
)

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

echo "Starting light backup by creating timestamped copies..."

for ITEM_PATH in "${ITEMS_TO_BACKUP[@]}"; do
    if [ -e "$ITEM_PATH" ]; then # Check if the item exists
        # Determine the target backup path within BACKUP_DIR, preserving original directory structure
        DIR_NAME=$(dirname "$ITEM_PATH")
        BASE_NAME=$(basename "$ITEM_PATH")
        
        TARGET_BACKUP_SUBDIR="$BACKUP_DIR/$DIR_NAME"
        mkdir -p "$TARGET_BACKUP_SUBDIR" # Ensure target subdirectory exists
        
        if [ -f "$ITEM_PATH" ]; then
            # For files, copy and append timestamp before extension
            RENAMED_FILE="$TARGET_BACKUP_SUBDIR/${BASE_NAME%.*}_${TIMESTAMP}${BASE_NAME##*.}"
            # Handle files with no extension
            if [[ "$BASE_NAME" == "${BASE_NAME%.*}" ]]; then
                RENAMED_FILE="$TARGET_BACKUP_SUBDIR/${BASE_NAME}_${TIMESTAMP}"
            fi
            cp "$ITEM_PATH" "$RENAMED_FILE"
            echo "Copied file '$ITEM_PATH' to '$RENAMED_FILE'"
        elif [ -d "$ITEM_PATH" ]; then
            # For directories, copy recursively and append timestamp to directory name
            RENAMED_DIR="$TARGET_BACKUP_SUBDIR/${BASE_NAME}_${TIMESTAMP}"
            cp -r "$ITEM_PATH" "$RENAMED_DIR"
            echo "Copied directory '$ITEM_PATH' to '$RENAMED_DIR'"
        fi
    else
        echo "Warning: '$ITEM_PATH' not found, skipping."
    fi
done

echo "Light backup complete! Check the '$BACKUP_DIR' directory."