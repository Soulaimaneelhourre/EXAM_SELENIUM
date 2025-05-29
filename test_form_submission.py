from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from utils import get_driver, save_screenshot
from test_config import BASE_URL, SEARCH_QUERY, SCREENSHOT_NAME

def main():
    driver = get_driver()

    try:
        # Step 1: Navigate to python.org
        driver.get(BASE_URL)

        # Step 2: Find search box
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )

        # Step 3: Search for "selenium"
        search_box.send_keys(SEARCH_QUERY)
        search_box.send_keys(Keys.RETURN)

        # Step 4: Wait for results to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "content"))
        )

        # Step 5: Screenshot
        save_screenshot(driver, SCREENSHOT_NAME)
        print("Test Passed.")

    except Exception as e:
        print(f"Test Failed: {e}")

    finally:
        time.sleep(2)
        driver.quit()

if __name__ == "__main__":
    main()
 