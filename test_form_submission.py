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
        driver.get(BASE_URL)  # go to python.org

        # Find the search box
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )

        search_box.send_keys(SEARCH_QUERY)
        search_box.send_keys(Keys.RETURN)

        # Wait until results show
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "content"))
        )

        # Save a screenshot
        save_screenshot(driver, SCREENSHOT_NAME)
        print("Test Passed.")

    except Exception as e:
        print(f"Test Failed: {e}")

    finally:
        time.sleep(2)
        driver.quit()  # Close browser

if __name__ == "__main__":
    main()
