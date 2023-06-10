#!/bin/bash
repo="https://github.com/andrew-dragoslavic/Fitness-App.git"
commit="New Changes"
branch="main"

git add .

git commit -m "$commit"

git push $repo $branch:$branch
