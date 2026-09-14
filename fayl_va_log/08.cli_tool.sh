#!/bin/bash
# Basic CLI interface script
echo -e "\n~~ Basic CLI Tool ~~\n"
echo "1. Show System Date & Time"
echo "2. Show Disk Usage"
echo "3. Exit"
read -p "Choose an option [1-3]: " CHOICE

case $CHOICE in
  1) date ;;
  2) df -h ;;
  3) echo "Goodbye!" ;;
  *) echo "Invalid option." ;;
esac
