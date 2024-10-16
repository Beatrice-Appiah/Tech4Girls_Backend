#!/bin/bash
# this script is to update the package list and upgrade all install packages

brew softwareupdate --list
brew softwareupdate --install --all
brew upgrade installed packages