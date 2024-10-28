import logging
import os
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


class WebDriver:
    def __init__(self, profile_name):
        self._args = {
            "chrome_stdout_file": "{}/chrome.logs".format(
                config["log_dir_path"]
            ),
            "browser_executable_path": config["browser"]["executable_path"],
            "browser_args": config["browser"]["args"],
            "user_data_dir": config["browser"]["profiles_dir_path"] + f"\\{profile_name}",
        }
        load_dotenv(config["nodriver_env_path"])

    async def start(self, **kwargs):
        combined_args = {**self._args, **kwargs}
        driver = await nodriver.start(**combined_args)
        return driver

