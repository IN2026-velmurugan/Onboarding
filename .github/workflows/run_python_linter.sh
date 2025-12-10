# issues_found will be true when any errors
# are catched by the below packages
issues_found=false

# Ruff
printf "\nRuff Checking........."
result=$(poetry run ruff check src)
if [[ "$result" != *"All checks passed!"* && ! -z "$result" ]]; then
    printf "\e[41mIssues Found\e[0m"
    printf "\n\n$result\n"
    issues_found=true
else
    printf "\e[42mNo Issues Found\e[0m\n"
fi

# MyPy
printf "\nMyPy Checking..........."
result=$(poetry run mypy --pretty src)
if [[ $result =~ ^Success:\ no\ issues\ found\ in\ [0-9]+\ source\ (file|files)$ ]]; then
    printf "\e[42mNo Issues Found\e[0m\n"
else
    printf "\e[41mIssues Found\e[0m\n"
    printf "\n\n$result\n"
    issues_found=true
fi
