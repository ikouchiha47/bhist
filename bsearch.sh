#!/bin/sh

# os=$(uname -a) 

# is_darwin=$(echo "$os" | grep -i darwin) 
# is_linux=$(echo "$os" | grep -i linux) 

# function chrome() { 
    # if [[ ! -z "$is_darwin" ]]; then 
    # "/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome" "$@" 
    # fi 

    # if [[ ! -z "$is_linux" ]]; then 
    # echo "Linux" 
    # fi 
# }

# export -f chrome

function copy_bookmarks_file() {
    cp "$HOME/Library/Application Support/Google/Chrome/Default/Bookmarks" .
}


copy_bookmarks_file

python3 -m py "$@"
