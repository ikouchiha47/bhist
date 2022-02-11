#!/bin/sh

os=$(uname -a) 

is_darwin=$(echo "$os" | grep -i darwin) 
is_linux=$(echo "$os" | grep -i linux) 

copy_chrome_bookmarks() {
    if [ ! -z "$is_darwin" ]; then
        cp "$HOME/Library/Application Support/Google/Chrome/Default/Bookmarks" tmp/
    elif [ ! -z "$is_linux" ]; then
        echo "linux"
        cp "$HOME/.config/chromium/Default/Bookmarks" tmp/
    fi
}


copy_chrome_bookmarks

python3 -m py "$@"
