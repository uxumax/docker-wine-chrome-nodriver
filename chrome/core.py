import logging
import os
import json
import subprocess

from config import config
import nodriver
from dotenv import load_dotenv


def get_logger(name):
    # Configure the logger
    log_file = "{}/{}.log".format(config["log_dir_path"], name)
    try:
        logging.basicConfig(
            level=logging.INFO,  # Set the default logging level
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',   # Define log message format
            handlers=[                             
                logging.StreamHandler(),  # StreamHandler sends logs to stdout (terminal)
                logging.FileHandler(log_file, mode='a')  # FileHandler sends to `log_file` 
            ]
        )
    except FileNotFoundError:
        # Probably log dir has not created yet
        # Make it and start function again
        os.mkdir(config["log_dir_path"])
        return get_logger(name)
    logger = logging.getLogger(name)
    return logger


log = get_logger("main")


class Browser:
    def __init__(self, profile_name):
        profile_path = config["browser"]["profiles_dir_path"] + f"\\{profile_name}"
        self._args = {
            "chrome_stdout_file": "{}/chrome.logs".format(
                config["log_dir_path"]
            ),
            "browser_executable_path": config["browser"]["executable_path"],
            "browser_args": config["browser"]["args"],
            "user_data_dir": profile_path,
        }
        self._profile_preferenes_path = f"{profile_path}\\Default\\Preferences"

    def _is_browser_profile_exists(self):  
        return os.path.isdir(self._args["user_data_dir"])

    def _is_native_windows_fonts_used(self):
        return os.getenv("USE_NATIVE_WINDOWS_FONTS") == "true"

    def _get_monospace_font_name(self) -> str:
        return os.getenv("WINE_MONOSPACE_FONT_NAME")

    async def _create_browser_profile(self):
        # Create profile for make browser profile 
        # preferences changes before run script
        driver = await self._start(
            # headless=True  # TODO
            # Cannot use headless here coz get nodriver exception
        )
        driver.stop()

        preferences = {
            "webkit": {
                "webprefs": {
                    "fonts": {}
                }
            }
        }
        self._save_profile_preferences(preferences)
        log.info("Browser profile has been created")

    def _open_profile_preferences(self) -> dict:
        with open(self._profile_preferenes_path, 'r', encoding='utf-8') as file:
            preferences = json.load(file)
            return preferences

    def _save_profile_preferences(self, preferences: dict):
        with open(self._profile_preferenes_path, 'w', encoding='utf-8') as file:
            json.dump(preferences, file, indent=4)
            log.info(f"Saved {preferences} to {self._profile_preferenes_path}")

    def _set_monospace_font_to_profile(self):
        preferences = self._open_profile_preferences()
        # Set monospace font param
        log.info(f"Preferences {preferences}")
        preferences["webkit"]["webprefs"]["fonts"]["fixed"] = {
            "Zyyy": self._get_monospace_font_name()
            # yep just fuckin Zyyy %)
        }

        self._save_profile_preferences(preferences)
        log.info("Native monospace fixed-width Windows font set")
        
    async def _start(self, **kwargs):
        combined_args = {**self._args, **kwargs}
        driver = await nodriver.start(**combined_args)
        return driver

    async def start(self, **kwargs):
        if not self._is_browser_profile_exists():
            await self._create_browser_profile()

        if self._is_native_windows_fonts_used():
            self._set_monospace_font_to_profile() 

        return await self._start(**kwargs)


