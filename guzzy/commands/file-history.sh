#!/bin/sh

# help: list all commits where file was changed and display diff for each one

file_name="$1"

git log --color=always --format="%C(auto)%h %s" "$file_name" |
    fzf --ansi --preview \
        "git diff --color=always {1}~ {1} -- $file_name 2>/dev/null || echo ..."
