#!/bin/bash

# Variables
REPO_DIR="./cicdpROJECT"   # Path to your local Git repository
DEPLOY_DIR="/var/www/html"      # Path to your Nginx document root
NGINX_SERVICE="nginx"           # Name of the Nginx service
BRANCH="main"                   # Change to your default branch if needed

# Function to update the website
update_website() {
    echo "Navigating to repository directory..."
    cd $REPO_DIR || { echo "Directory not found! Exiting."; exit 1; }

    echo "Pulling latest changes from GitHub..."
    git pull origin $BRANCH  # Pull changes

    echo "Deploying changes to Nginx directory..."
    rsync -av --exclude='.git/' . $DEPLOY_DIR/
    echo rsync -av --exclude='.git/' $REPO_DIR/ $DEPLOY_DIR/

    echo "Restarting Nginx service..."
    sudo systemctl restart $NGINX_SERVICE
    echo "Website updated and Nginx restarted."
}

# Execute the function
update_website
