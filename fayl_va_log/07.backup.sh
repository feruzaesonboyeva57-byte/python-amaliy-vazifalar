#!/bin/bash
# Simple directory backup script
echo -e "\n~~ Backup Script ~~\n"
SOURCE_DIR=${1:-"."}
BACKUP_NAME="backup_$(date +%Y%m%d_%H%M%S).tar.gz"
tar -czf $BACKUP_NAME $SOURCE_DIR 2>/dev/null
echo "Backup created successfully: $BACKUP_NAME"
