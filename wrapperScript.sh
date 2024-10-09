#!/bin/bash

#Execute the Python script to check for changes
python3 checkPipelineChanges.py

# Check the exit status of the Python script
if [ $? -eq 0 ]; then
        # If changes are detected, run the deploy script\
        echo "Deploying changes..."
        ./deployChanges.sh
else
        echo "No changes to deploy."
fi
