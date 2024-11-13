#!/bin/bash

env_vars="# CONFIG 

# Browser profile name to start
PROFILE_NAME=profile1
SCRIPT_NAME=check_browser

# Browser fingerprint checkers. Uncomment your preferred
BROWSER_CHECKER_URL=https://abrahamjuliot.github.io/creepjs/
# BROWSER_CHECKER_URL=https://www.nowsecure.nl
# BROWSER_CHECKER_URL=https://antcpt.com/score_detector/
# BROWSER_CHECKER_URL=https://browserleaks.com/

# Wine Windows system UI font
# Upload origin Windows fonts to ./wine/fonts 
# and set "Segoe UI" intead "Tahoma" for more natural font fingerprint
WINE_SYSTEM_UI_FONT_NAME=Tahoma
"


echo -e "$env_vars" > .env
echo "The .env file gas been generated."
