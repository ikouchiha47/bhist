# { pkgs ? import (fetchTarball https://github.com/nixos/nixpkgs/archive/nixpkgs-unstable.tar.gz) {} }:
{ pkgs ? import <nixpkgs> {} }:
with pkgs;

pkgs.mkShell {
  buildInputs = [ python39Full xapian xapian-omega python39Packages.xapian ];
}
