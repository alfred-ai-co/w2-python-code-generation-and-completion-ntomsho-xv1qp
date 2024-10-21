#!/bin/bash
# Activate the environment
if [ "$1" == "dev" ]; then
    echo "Starting in development mode..."
    # Add commands to start your application in dev mode
elif [ "$1" == "prod" ]; then
    echo "Starting in production mode..."
    # Add commands to start your application in prod mode
else
    echo "Please specify 'dev' or 'prod'."
fi
