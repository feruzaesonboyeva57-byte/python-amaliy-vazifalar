#!/bin/bash
# Simulation of a deployment check script
echo -e "\n~~ Safe Deploy Checker ~~\n"
STATUS_CODE=$(curl -s -o /dev/null -w "%{http_code}" https://google.com)

if [[ $STATUS_CODE -eq 200 ]]; then
  echo "Environment check PASSED ($STATUS_CODE). Ready to deploy!"
else
  echo "Environment check FAILED ($STATUS_CODE). Deployment aborted."
fi
