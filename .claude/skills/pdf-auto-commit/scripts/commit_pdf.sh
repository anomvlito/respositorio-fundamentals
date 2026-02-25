#!/bin/bash

# Configuration
DEFAULT_MSG="Update PDF document(s)"
CUSTOM_MSG="$1"
COMMIT_MSG="${CUSTOM_MSG:-$DEFAULT_MSG}"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}Checking for modified PDF files...${NC}"

# Check for modified or untracked PDF files
PDF_CHANGES=$(git status --porcelain | grep ".pdf$")

if [ -z "$PDF_CHANGES" ]; then
    echo -e "${GREEN}No PDF changes detected.${NC}"
    exit 0
fi

echo -e "${BLUE}Detected changes:${NC}"
echo "$PDF_CHANGES"

# Stage PDF files
echo -e "${BLUE}Staging PDF files...${NC}"
git add *.pdf **/*.pdf

# Commit
echo -e "${BLUE}Committing...${NC}"
git commit -m "$COMMIT_MSG"

# Push
echo -e "${BLUE}Pushing to remote...${NC}"
git push

if [ $? -eq 0 ]; then
    echo -e "${GREEN}Successfully updated PDFs!${NC}"
else
    echo -e "${RED}Error pushing changes.${NC}"
    exit 1
fi
