#!/bin/bash

# pre_edit_backup.sh: Creates a timestamped copy of a file before it's edited.
# This script is designed as a crucial part of a "no-pypass" strategy for file modifications,
# providing a robust, local snapshot to protect against accidental changes or facilitate quick reverts.
# It is essential to run this script *before* making any changes to a file.

# Usage: ./pre_edit_backup.sh <file_to_backup>

FILE_TO_BACKUP="$1"

# --- Input Validation ---
if [ -z "$FILE_TO_BACKUP" ]; then
    echo "Error: Missing argument. Please provide the path to the file you want to back up."
    echo "Usage: ./pre_edit_backup.sh <file_to_backup>"
    exit 1
fi

if [ ! -f "$FILE_TO_BACKUP" ]; then
    echo "Error: File '$FILE_TO_BACKUP' not found or is not a regular file."
    exit 1
fi

# --- Backup Directory Setup ---
# Define the directory where pre-edit snapshots will be stored.
# This directory MUST be listed in .gitignore to prevent accidental commits.
BACKUP_DIR="backups/pre_edit_snapshots"

# Attempt to create the backup directory. Exit if creation fails.
if ! mkdir -p "$BACKUP_DIR"; then
    echo "Error: Failed to create backup directory '$BACKUP_DIR'."
    exit 1
fi

# --- Generate Timestamp ---
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# --- Determine Backup Path ---
# Get the directory and base name of the file to preserve original structure within backups.
DIR_NAME=$(dirname "$FILE_TO_BACKUP")
BASE_NAME=$(basename "$FILE_TO_BACKUP")

# Construct the target backup subdirectory (e.g., backups/pre_edit_snapshots/path/to/)
TARGET_BACKUP_SUBDIR="$BACKUP_DIR/$DIR_NAME"

# Ensure the target subdirectory within BACKUP_DIR exists. Exit if creation fails.
if ! mkdir -p "$TARGET_BACKUP_SUBDIR"; then
    echo "Error: Failed to create target backup subdirectory '$TARGET_BACKUP_SUBDIR'."
    exit 1
fi

# Formulate the new timestamped filename.
RENAMED_FILE="$TARGET_BACKUP_SUBDIR/${BASE_NAME%.*}_${TIMESTAMP}${BASE_NAME##*.}"

# Handle files with no extension (e.g., .gitignore)
if [[ "$BASE_NAME" == "${BASE_NAME%.*}" ]]; then
    RENAMED_FILE="$TARGET_BACKUP_SUBDIR/${BASE_NAME}_${TIMESTAMP}"
fi

# --- Perform the Copy ---
echo "Creating pre-edit snapshot for '$FILE_TO_BACKUP'..."
if cp "$FILE_TO_BACKUP" "$RENAMED_FILE"; then
    echo "SUCCESS: Snapshot created at '$RENAMED_FILE'."
    echo "Remember to always run this script before modifying crucial project files."
    echo "You can now safely edit '$FILE_TO_BACKUP'."
else
    echo "Error: Failed to create snapshot for '$FILE_TO_BACKUP'."
    exit 1
fi