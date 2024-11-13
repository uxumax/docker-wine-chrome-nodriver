from importlib import import_module
import asyncio
import time
import os

import nodriver

from config import config
from scripts import check_browser
from core import (
    WebDriver, 
    get_logger,
)

log = get_logger(__name__)

async def run_chrome(profile_name: str, script_name: str):
    driver = await WebDriver(profile_name).start()
    script = import_module(f"scripts.{script_name}")
    await script.run(driver)


if __name__ == "__main__":
    profile_name = os.getenv("PROFILE_NAME")
    script_name = os.getenv("SCRIPT_NAME")
    asyncio.run(
        run_chrome(profile_name, script_name)
    )
    input("Waiting...")
