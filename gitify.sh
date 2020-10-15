#!/bin/bash

git init
find * -size +4M -type f -print >> .gitignore
git add -A
git commit -m "first commit"
git branch -M main
git remote add origin https://raychorn:f5ea04ef15a5cc7767fbf8459701af9570d32597@github.com/raychorn/svn_Python-2.5.1.git
git push -u origin main
