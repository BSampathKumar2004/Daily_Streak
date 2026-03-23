#!/bin/bash

# Move to your repo
cd ~/Documents/Coding/Daily_Streak_GitHub/Daily_Streak || exit

# Current date
date=$(date +"%Y-%m-%d %H:%M:%S")

# Create/update daily file
file="day_$(date +%Y_%m_%d).md"

echo "## Update on $date" >> $file

# Git operations
git add .

# Check if there are changes
if ! git diff --cached --quiet; then
    git commit -m "daily: update on $date"
else
    git commit --allow-empty -m "streak: $date"
fi

git push origin main