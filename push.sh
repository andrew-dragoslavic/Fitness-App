#!/bin/bash
repo="origin"
commit="New Changes"
branch="main"

git add .

git commit -m "$commit"
git push "$repo $branch"
