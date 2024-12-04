from importlib import import_module
import asyncio
import time
import os

import atexit
import nodriver as uc

from config import config
from scripts import check_browser
from core import (
    Browser, 
    get_logger,
)

log = get_logger(__name__)

# Disable deconstruct_browser at exit
atexit.unregister(uc.core.util.deconstruct_browser) 

async def _graceful_stop_browser(driver):
    try:
        # Close all tabs
        for t in driver.tabs:
            await t.close()

        # Attempt to close the websocket connection manually
        if driver.connection:
            await driver.connection.aclose()

        # Close the browser
        driver.stop()

    except Exception as e:
        log.exception(f"Error during browser closure: {e}")

    finally:
        # Ensure the browser process is terminated
        if driver._process:
            log.info("Waiting graceful stop the browser proccesses...")
            driver._process.terminate()
            await driver._process.wait()
            log.info("Browser has been stopped gracefully")


async def _run_script(profile_name: str, script_name: str):
    driver = await Browser(profile_name).start()
    script = import_module(f"scripts.{script_name}")
    try:
        await script.run(driver)
    except KeyboardInterrupt:
        await _graceful_stop_browser(driver)


if __name__ == "__main__":
    profile_name = os.getenv("PROFILE_NAME")
    script_name = os.getenv("SCRIPT_NAME")
    uc.loop().run_until_complete(
        _run_script(profile_name, script_name)
    ) 

