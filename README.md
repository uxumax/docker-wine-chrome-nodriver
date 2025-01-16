# Project Overview

This project facilitates running a Windows Chrome antidetect browser using the [nodriver](https://github.com/ultrafunkamsterdam/nodriver) automation library within a Docker Linux container with Wine. This setup eliminates the need for a Windows virtual machine, making the process easier, faster, and more efficient.

## Prerequisites

Ensure you have Docker Engine installed. If not, follow the installation guide [here](https://docs.docker.com/engine/install/). If you want run docker as non-root user do not forget about [this](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user)

## Setup Instructions

1. **Upload Antidetect Chrome Browser:**
   - Place your preferred antidetect Chrome browser in the `chrome/bin` directory.
   - Ensure `chrome.exe` is located at `chrome/bin/chrome.exe`.

2. **Create Dotenv File:**
   - Run the following bash script to generate `.env` file
     ```bash
     ./create_dotenv.sh
     ```
   - The `.env` contains: 
     - `PROFILE_NAME`: The name of the browser profile (`--user_data_dir` chrome arg). You can set any name, create profiles as needed, and reuse them. All profiles are stored in `chrome/profiles/`. Feel free to add or remove profiles as necessary. If you run `./run.sh` with a non-existent profile, a new blank one will be created.
     - `SCRIPT_NAME`: The name of the script to run. All scripts are located in `chrome/scripts/`. Each script should contain a `run()` function as the entry point.
     - Rest system env variables that accessible in Chrome Nodriver context

2. **Build and Run the Docker Container:**
   - Run the following command to build the container with Wine:
     ```bash
     ./build.sh
     ```
   - Execute the following command to run the container. This script will handle the post-build GUI Wine installation `wine-mono` and `python` on the first run. Subsequent runs will be ready for use:
     ```bash
     ./run.sh 
     ```

## Example Script

Below is an example of a Chrome nodriver script that demonstrates how to create your own scripts:

```python
import os
import asyncio

async def run(driver):
    url = os.getenv("BROWSER_CHECKER_URL")
    await driver.get(url)
    while True: 
        asyncio.sleep(60)  # keep browser open
```

This script opens an online browser fingerprint checker. The URL is retrieved from `.env`. By default, the file contains the following entries, with only one uncommented:

```env
BROWSER_CHECKER_URL=https://abrahamjuliot.github.io/creepjs/
```

You can manage these environment variables by setting new ones and accessing them using `os.getenv` in your automation scripts.

## Shared Directory

You can use the `./sharedir` directory for file uploads or downloads in your automation scripts. It is accessible at:
- `/home/wineuser/sharedir` inside the Linux container
- `Z:\\home\\wineuser\\sharedir` inside the Wine context

## Recommended Chrome Browser

You should use an antidetect Chrome browser. This involves modifying the original Chrome source code to make the browser undetectable. This mean spoof Canvas, WebGL, Audio, WebRTC (etc) detection and set these spoofing params with Wine environ variables in `.env`

## Possible issues
This project built and tested on Debian 12 (bookworm) Docker host. So here are known possible issues below

### Chrome black window
If chrome run with black window then try restart X window manager with this script
```bash
./debug/reset_display.sh
```

### Wine issues
If Wine broken you can resinstall it this way. Do not worry your browser profiles and nodriver scripts will NOT be deleted.
```bash
./debug/clear_wine_prefix.sh
```
Then just run you profile and script with `./run.sh` to reinstall

---
