#!/bin/bash

env_vars="# CONFIG 

# Browser profile name to start
PROFILE_NAME=profile1
SCRIPT_NAME=check_browser

# Browser Fingerprint Checkers
# Uncomment your preferred
BROWSER_CHECKER_URL=https://abrahamjuliot.github.io/creepjs/
# BROWSER_CHECKER_URL=https://www.nowsecure.nl
# BROWSER_CHECKER_URL=https://antcpt.com/score_detector/
# BROWSER_CHECKER_URL=https://browserleaks.com/

# Wine Windows Natural Fonts
# 1. Upload native Windows fonts from some C:\\Windows\\Fonts to ./wine/fonts 
# 2. Set 'USE_NATIVE_WINDOWS_FONTS=true' for more natural font fingerprint
USE_NATIVE_WINDOWS_FONTS=false
WINE_SYSTEM_UI_FONT_NAME=Segoe UI
WINE_MONOSPACE_FONT_NAME=Consolas
"

echo -e "$env_vars" > .env
echo "The .env file gas been generated."
