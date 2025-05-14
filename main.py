from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def scrape():
    options = Options()
    options.add_argument('--headless')  # Run in headless mode
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.github.com/vasantharan')  # Replace with your target URL
    time.sleep(2)  # Wait for page to load
    # Example: scraping all <h3> tags
    headers = driver.find_elements(By.TAG_NAME, "h3")
    for h in headers:
        print("Header found:", h.text)
    driver.quit()

if __name__ == "__main__":
    scrape()
