import os
from core import WebDriver

async def run(driver: WebDriver):
    url = os.getenv("BROWSER_CHECKER_URL")
    await driver.get(url)
