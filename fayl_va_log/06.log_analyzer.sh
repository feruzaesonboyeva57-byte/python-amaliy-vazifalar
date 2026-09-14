#!/bin/bash
# Simple log analyzer script
echo -e "\n~~ Log Analyzer ~~\n"
LOG_FILE=$1
if [[ -f $LOG_FILE ]]; then
  echo "Total lines in log: $(wc -l < $LOG_FILE)"
  echo "Error entries count: $(grep -c -i "error" $LOG_FILE)"
else
  echo "Please provide a valid log file path."
fi
