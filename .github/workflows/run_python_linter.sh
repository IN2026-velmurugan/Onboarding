#!/usr/bin/env bash

# Track whether any tool reports issues
issues_found=false

echo
printf "Running Black + MyPy checks...\n"

# -----------------------
# Black
# -----------------------
printf "\nBlack Checking.........\n"

# Run Black in check mode (does NOT modify files)
poetry run black --check src
black_status=$?

if [[ $black_status -ne 0 ]]; then
    printf "\e[41mFormatting Issues Found (Black)\e[0m\n"
    issues_found=true
else
    printf "\e[42mNo Formatting Issues Found (Black)\e[0m\n"
fi


# -----------------------
# MyPy
# -----------------------
printf "\nMyPy Checking...........\n"

mypy_output=$(poetry run mypy --pretty src)
mypy_status=$?

if [[ $mypy_status -ne 0 ]]; then
    printf "\e[41mType Checking Issues Found (MyPy)\e[0m\n"
    printf "\n$mypy_output\n"
    issues_found=true
else
    printf "\e[42mNo Issues Found (MyPy)\e[0m\n"
fi


# -----------------------
# Final summary
# -----------------------
printf "\n==================== Summary ====================\n"

if [[ "$issues_found" == true ]]; then
    printf "\e[41mSome checks failed. Fix issues above.\e[0m\n"
    exit 1
else
    printf "\e[42mAll checks passed.\e[0m\n"
    exit 0
fi
