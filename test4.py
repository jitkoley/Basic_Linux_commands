import time
from playwright.sync_api import sync_playwright

def navigate_and_load_all_models():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Step 1: Open the AI Hub site
        page.goto("https://aihub.qualcomm.com/")
        time.sleep(3)

        # Step 2: Open the Explore menu
        explore_xpath = "/html/body/header/div[1]/div/nav/ul/li[1]/button"
        page.locator(f"xpath={explore_xpath}").click()
        time.sleep(2)

        # Step 3: Click on "IoT"
        iot_xpath = "/html/body/header/div[2]/div[2]/div/div/div[1]/div/div[1]/div[1]/ul/li[4]/a/span[2]"
        page.locator(f"xpath={iot_xpath}").click()
        time.sleep(2)

        # Step 4: Click on "Quantized"
        quantized_xpath = "/html/body/main/div[3]/div[1]/div/div[4]/div/div/div/fieldset/span[2]/label/span/span"
        page.locator(f"xpath={quantized_xpath}").click()
        time.sleep(2)

        # Step 5: Repeatedly click "Load More" as long as it's visible & enabled
        load_more_xpath = "/html/body/main/div[3]/div[2]/div[2]/button/span/span"
        load_more_button = page.locator(f"xpath={load_more_xpath}")

        click_count = 0
        while True:
            try:
                # Wait a moment for button to appear (if needed)
                time.sleep(2)

                if load_more_button.is_visible() and load_more_button.is_enabled():
                    load_more_button.click()
                    click_count += 1
                    print(f"✅ Clicked Load More ({click_count})")
                    time.sleep(2)
                else:
                    print("🚫 Load More button not clickable anymore.")
                    break
            except Exception as e:
                print(f"⚠️ Error clicking Load More: {e}")
                break

        print(f"✅ Done. Load More was clicked {click_count} times.")
        input("Press Enter to close the browser...")
        browser.close()

if __name__ == "__main__":
    navigate_and_load_all_models()
