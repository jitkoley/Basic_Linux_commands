import time
from playwright.sync_api import sync_playwright

def navigate_to_models():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Step 1: Open the site
        page.goto("https://aihub.qualcomm.com/")
        time.sleep(3)

        # Step 2: Click on the "Explore" button
        menu_xpath = "/html/body/header/div[1]/div/nav/ul/li[1]/button"
        page.locator(f"xpath={menu_xpath}").click()
        time.sleep(2)

        # Step 3: Click on the "IoT" category
        iot_xpath = "/html/body/header/div[2]/div[2]/div/div/div[1]/div/div[1]/div[1]/ul/li[4]/a/span[2]"
        page.locator(f"xpath={iot_xpath}").click()
        time.sleep(2)

        # Step 4: Click on the "Quantized" filter
        quantized_xpath = "/html/body/main/div[3]/div[1]/div/div[4]/div/div/div/fieldset/span[2]/label/span/span"
        page.locator(f"xpath={quantized_xpath}").click()
        time.sleep(2)

        # Step 5: Click "Load More" 4 times
        load_more_xpath = "/html/body/main/div[3]/div[2]/div[2]/button/span/span"
        for i in range(4):
            try:
                print(f"Clicking Load More ({i+1}/4)...")
                page.locator(f"xpath={load_more_xpath}").click()
                time.sleep(2)
            except Exception as e:
                print(f"⚠️ Failed to click Load More on attempt {i+1}: {e}")
                break

        print("✅ Finished loading models on page:", page.url)
        input("Press Enter to close the browser...")

        browser.close()

if __name__ == "__main__":
    navigate_to_models()
