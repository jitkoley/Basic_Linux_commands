import time
from playwright.sync_api import sync_playwright

def navigate_to_models():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Step 1: Open the site
        page.goto("https://aihub.qualcomm.com/")
        time.sleep(3)  # Wait for 5 seconds to allow the page to load

        # Step 2: Click on the "Explore" button
        explore_button_xpath = "/html/body/header/div[1]/div/nav/ul/li[1]/button"
        page.locator(f"xpath={explore_button_xpath}").click()
        time.sleep(2)  # Small delay to let menu open

        # Step 3: Click on the "iot" button
        explore_button_xpath = "/html/body/header/div[2]/div[2]/div/div/div[1]/div/div[1]/div[1]/ul/li[4]/a/span[2]"
        page.locator(f"xpath={explore_button_xpath}").click()
        time.sleep(2)  # Small delay to let menu open

        # Step 4: Click on the "Quantized" button
        explore_button_xpath = "/html/body/main/div[3]/div[1]/div/div[4]/div/div/div/fieldset/span[2]/label/span/span"
        page.locator(f"xpath={explore_button_xpath}").click()
        time.sleep(2)  # Small delay to let menu open

        # Step : Click on the "load more" button
        explore_button_xpath = "/html/body/main/div[3]/div[2]/div[2]/button/span/span"
        page.locator(f"xpath={explore_button_xpath}").click()
        time.sleep(2)  # Small delay to let menu open

        print("✅ Navigated to:", page.url)
        input("Press Enter to close the browser...")

        browser.close()

if __name__ == "__main__":
    navigate_to_models()
