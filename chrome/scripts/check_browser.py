import os
from time import sleep

async def run(driver):
    url = os.getenv("BROWSER_CHECKER_URL")
    await driver.get(url)
    while True:  # keep browser open
        sleep(60)  # use sync sleep coz more easy to interupt  
