### kdty

Search in your bookmarks

##### Requirements
- xapian and xapian-bindings (using your system package manager)
- python 3.9 or above
- nix, optional

If you are using nix. `nix-shell` should take care of all system setup

##### Usage
- ./kdty --init (to setup databases)
- ./kdty -c Bookmarks gather (to get all the bookmarks and store data. you can pass --init here as well)
- ./kdty index (indexed stored data)
- ./kdty search -t 'search term' -f url
- ./kdty --help


##### ToDo
- [ ] Linux support
- [ ] Firefox support
- [ ] Make gathering faster



##### Footnotes:

xapian installation instructions can be found [here](https://xapian.org/download)  

For macos:
- `brew install --build-from-source xapian --with-python`

For Linux, you can use your package manager.

You can also opt to use `nix`, in which case, `nix-shell`, should take care of all dependencies
