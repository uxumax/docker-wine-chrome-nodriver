import os
import asyncio

async def run(driver):
    url = os.getenv("BROWSER_CHECKER_URL")
    await driver.get(url)
    while True: 
        asyncio.sleep(60)  # keep browser open
