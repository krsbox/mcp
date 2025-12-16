#!/bin/bash

# pre_edit_backup.sh: Creates a timestamped copy of a file before it's edited.
# This serves as a light, local backup to protect against accidental changes.

# Usage: ./pre_edit_backup.sh <file_to_backup>

FILE_TO_BACKUP="$1"

if [ -z "$FILE_TO_BACKUP" ]; then
    echo "Usage: ./pre_edit_backup.sh <file_to_backup>"
    exit 1
fi

if [ ! -f "$FILE_TO_BACKUP" ]; then
    echo "Error: File '$FILE_TO_BACKUP' not found."
    exit 1
fi

# Define the directory where backups will be stored.
# This directory should be listed in .gitignore.
BACKUP_DIR="backups/pre_edit_snapshots"
mkdir -p "$BACKUP_DIR"

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Get the directory and base name of the file
DIR_NAME=$(dirname "$FILE_TO_BACKUP")
BASE_NAME=$(basename "$FILE_TO_BACKUP")

# Determine the target backup path within BACKUP_DIR, preserving original directory structure
# This creates a subdirectory within BACKUP_DIR like backups/pre_edit_snapshots/path/to/
TARGET_BACKUP_SUBDIR="$BACKUP_DIR/$DIR_NAME"
mkdir -p "$TARGET_BACKUP_SUBDIR" # Ensure target subdirectory exists

RENAMED_FILE="$TARGET_BACKUP_SUBDIR/${BASE_NAME%.*}_${TIMESTAMP}${BASE_NAME##*.}"

# If the file has no extension
if [[ "$BASE_NAME" == "${BASE_NAME%.*}" ]]; then
    RENAMED_FILE="$TARGET_BACKUP_SUBDIR/${BASE_NAME}_${TIMESTAMP}"
fi

cp "$FILE_TO_BACKUP" "$RENAMED_FILE"
echo "Backup created: '$RENAMED_FILE' before editing '$FILE_TO_BACKUP'."
echo "Backup complete! You can now safely edit '$FILE_TO_BACKUP'."
