import os

async def run(driver):
    url = os.getenv("BROWSER_CHECKER_URL")
    await driver.get(url)
    while True: pass  # keep browser open
