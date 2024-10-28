#!/bin/bash

# NOTE
# If chrome run with black window try restart X window manager
sudo systemctl restart display-manager
xhost +local:docker
# Source: https://askubuntu.com/questions/1220/how-to-restart-x-window-server-from-command-line
