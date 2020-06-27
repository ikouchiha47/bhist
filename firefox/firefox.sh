#!/bin/bash

ff=$(command -v firefox)
ffd=$(command -v firefox-developer-edition)

[[ -x "$ff" || -x "$ffd" ]] &&  find ~/.mozilla/firefox/ -type f -name places.sqlite

