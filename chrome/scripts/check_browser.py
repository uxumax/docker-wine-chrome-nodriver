import os
from time import sleep

async def run(driver):
    url = os.getenv("BROWSER_CHECKER_URL")
    await driver.get(url)
    while True: 
        sleep(60)  # keep browser open
