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

# Pyrefly
printf "\nPyrefly Checking....."
result=$(poetry run pyrefly check src)
if [ ! -z "$result" ]; then
    printf "\e[41mIssues Found\e[0m"
    printf "\n\n$result\n"
    issues_found=true
else
    printf "\e[42mNo Issues Found\e[0m\n"
fi

if [ $issues_found == true ]; then
    printf "\nIssues Found in your code...\nPlease format your code based on the above suggestions given...\n"
    exit 1
fi
