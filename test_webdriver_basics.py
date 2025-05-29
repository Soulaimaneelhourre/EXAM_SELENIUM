from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
import time

# Initialize driver
service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)

try:
    # 1. Open https://www.python.org
    driver.get("https://www.python.org")

    # 2. Search for "selenium" in the search box
    search_box = driver.find_element(By.ID, "id-search-field")
    search_box.clear()
    search_box.send_keys("selenium")

    # 3. Click the search button
    search_button = driver.find_element(By.ID, "submit")
    search_button.click()

    time.sleep(2)  # Wait for results to load

    # 4. Print the number of search results found
    results = driver.find_elements(By.CSS_SELECTOR, ".list-recent-events.menu li")
    print(f"Number of search results found: {len(results)}")

    # 5. Take a screenshot
    driver.save_screenshot("search_results.png")
    print("Screenshot saved as 'search_results.png'.")

finally:
    # 6. Close the browser
    driver.quit()
