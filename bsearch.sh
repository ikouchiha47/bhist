#!/bin/sh

os=$(uname -a) 

is_darwin=$(echo "$os" | grep -i darwin) 
is_linux=$(echo "$os" | grep -i linux) 

copy_chrome_bookmarks() {
    if [ ! -z "$is_darwin" ]; then
        cp "$HOME/Library/Application Support/Google/Chrome/Default/Bookmarks" .
    elif [ ! -z "$is_inux" ]; then
        cp "$HOME/.config/chromium/Default/Bookmarks" .
    fi
}


copy_chrome_bookmarks
python3 -m py "$@"
