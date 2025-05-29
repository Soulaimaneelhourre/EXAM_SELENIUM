from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
import os

def get_driver():
    """Initialize and return a Chrome WebDriver."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    service = Service(EdgeChromiumDriverManager().install())
    return webdriver.Chrome(service=service, options=options)

def save_screenshot(driver, file_name):
    """Take a screenshot and save it in the screenshots folder."""
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    path = f"screenshots/{file_name}_{timestamp}.png"
    driver.save_screenshot(path)
    print(f"Screenshot saved: {path}")
