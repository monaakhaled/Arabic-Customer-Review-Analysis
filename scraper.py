from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_reviews(url, max_reviews=20):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get(url)
    time.sleep(5)

    reviews = []
    elements = driver.find_elements(By.TAG_NAME, "p")

    for el in elements:
        text = el.text.strip()
        if len(text) > 40:
            reviews.append(text)
        if len(reviews) >= max_reviews:
            break

    driver.quit()
    return reviews