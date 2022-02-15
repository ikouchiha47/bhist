#!/bin/sh

os=$(uname -a) 

is_darwin=$(echo "$os" | grep -i darwin) 
is_linux=$(echo "$os" | grep -i linux) 

copy_chrome_bookmarks() {
    if [ ! -z "$is_darwin" ]; then
        cp "$HOME/Library/Application Support/Google/Chrome/Default/Bookmarks" tmp/
    elif [ ! -z "$is_linux" ]; then
        cp "$HOME/.config/chromium/Default/Bookmarks" tmp/
    fi
}


copy_firefox_bookmarks() {
    if [ ! -z "$is_linux" ]; then
        x=$(find ~/.mozilla/firefox/ -type f -name places.sqlite)

        if [ -z "$x" ]; then
            echo "Firefox no bookmarks"
            return
        fi

        profile=$(cat ~/.mozilla//firefox/profiles.ini | grep -B2 Locked=1 | tail -n2 | grep Default | cut -d= -f2)

        cp "$HOME/.mozilla/firefox/$profile/places.sqlite" tmp/
    fi
}

copy_chrome_bookmarks
copy_firefox_bookmarks

python3 -m py "$@" 
