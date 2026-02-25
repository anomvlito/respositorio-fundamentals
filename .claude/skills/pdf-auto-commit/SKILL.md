---
name: pdf-auto-commit
description: Automates committing and pushing PDF changes to the repository with descriptive messages.
---

# PDF Auto-Commit Skill

## Description
This skill automates the process of saving PDF changes to the git repository. It detects modified PDF files, automatically stages them, and commits them with a standardized or custom message, then pushes to the remote branch.

## Usage
When you need to save a PDF file (e.g., after compilation or manual update), call the `run_command` tool with the provided script.

### Syntax
```bash
/path/to/script/commit_pdf.sh "[Optional Custom Message]"
```

### Examples
**1. Auto-detect and commit with default message:**
```bash
bash .agent/skills/pdf-auto-commit/scripts/commit_pdf.sh
```

**2. Commit with a specific message:**
```bash
bash .agent/skills/pdf-auto-commit/scripts/commit_pdf.sh "Updated Module 1 PDF with new exercises"
```

## Requirements
- Git must be initialized in the directory.
- Access to the remote repository (ssh/https) must be configured.
