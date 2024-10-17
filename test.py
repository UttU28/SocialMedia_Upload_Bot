from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
# chrome_options.add_argument("--headless")  # Uncomment to run in headless mode

driver = webdriver.Chrome(r'/usr/bin/chromedriver')

try:
    driver.get("https://www.google.com/")

    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    search_box.send_keys("HELLO")
    
    search_box.send_keys(Keys.RETURN)

finally:
    WebDriverWait(driver, 5).until(EC.title_contains("HELLO"))  # Wait for the results page to load
    driver.quit()
