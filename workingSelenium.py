import subprocess 
from time import sleep
import json
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup  # Ensure you have this import
import pyautogui as pi
import os

chromeDriverPath = 'C:/Users/utsav/OneDrive/Desktop/SocialMedia_Upload_Bot/chromeDriver/chromedriver.exe'

options = Options()
options.add_experimental_option("debuggerAddress", "localhost:8989")
options.add_argument(f"webdriver.chrome.driver={chromeDriverPath}")
options.add_argument("--disable-notifications")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
options.add_argument("window-size=1920x1080")

def getDataFromFile():
    try:
        with open('data/baseData.json', 'r') as jsonFile:
            allEventData = json.load(jsonFile)
    except FileNotFoundError:
        allEventData = {}
    return allEventData

def putDataToFile(taazaMaal):
    with open('data/baseData.json', 'w') as jsonFile:
        json.dump(taazaMaal, jsonFile, indent=4)

def prepareChromeAndSelenium():
    chromeProcess = subprocess.Popen([
        'C:/Program Files/Google/Chrome/Application/chrome.exe',
        '--remote-debugging-port=8989',
        '--user-data-dir=C:/Users/utsav/OneDrive/Desktop/LinkedIn_Reverse_Search/chromeData/'
        # '--user-data-dir=C:/Users/utsav/OneDrive/Desktop/SocialMedia_Upload_Bot/chromeData/'
    ])
    # chromeProcess = ''
    driver = webdriver.Chrome(options=options)
    return chromeProcess, driver

def runSelenium(thisDriver, mainLink):
    thisDriver.get(f"{mainLink}")
    sleep(random.uniform(0.5, 2.5))

def countParents(element):
    count = 0
    while element:
        element = element.find_element(By.XPATH(".."))
        if element.getAttribute('tagName') == 'section':
            return count
        count += 1
    return count

def scrapeDataFrom(thisDriver):
    runSelenium(thisDriver, f"https://www.linkedin.com/feed/")
    startPost = WebDriverWait(thisDriver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'share-box-feed-entry__trigger'))
    )
    startPost.click()

    mainPostBox = WebDriverWait(thisDriver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'share-box-v2__modal-phoenix-redesign'))
    )
    # textBox = mainPostBox.find_element(By.CLASS_NAME, "ql-editor")
    # textBox.click()
    sleep(2)

    ulList = mainPostBox.find_element(By.CSS_SELECTOR, "ul.artdeco-carousel__slider.ember-view")
    allLiButtons = ulList.find_elements(By.TAG_NAME, 'li')
    addImageButton = allLiButtons[1].click()

    # os.system("xdotool key ctrl+l")
    sleep(0.5)
    pi.hotkey('ctrl', 'l')
    sleep(1)
    pi.typewrite('C:/Users/utsav/OneDrive/Desktop/SocialMedia_Upload_Bot/images')
    sleep(0.5)
    pi.press('enter')
    for _ in range(6):
        sleep(0.2)
        pi.press('tab')
    sleep(0.3)
    pi.typewrite('Strategies for Success.png')
    sleep(0.3)
    pi.press('enter')

    sleep(1)

    boxFooter = mainPostBox.find_element(By.CLASS_NAME, 'share-box-footer')
    footerButtons = boxFooter.find_elements(By.TAG_NAME, 'button')

    for button in footerButtons:
        if button.text.lower() == 'next':
            button.click()
            sleep(0.5)
            break
    webdriver.ActionChains(thisDriver).send_keys("JKSHDGFV YFGBV JSHBVJHDNVBSDFVB KJSEBF\n\n jhgvsb jb\nsdlhj gb").perform()

    postThePostFooter = WebDriverWait(thisDriver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'share-creation-state__footer'))
    )

    # postThePostButton = postThePostFooter.find_element(By.CLASS_NAME, 'share-box_actions').click()

    
    # os.system(f"xdotool type 'C:/Users/utsav/Downloads/Strategies For Success.png' && xdotool key Return")
    # addImageButton.click()

    # sleep(2)  # Wait for the file input to be ready
    # file_input = WebDriverWait(thisDriver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
    # )
    # file_input.send_keys("C:\\Users\\utsav\\Downloads\\Strategies For Success.png")
    # sleep(0.5)
    # # webdriver.ActionChains(thisDriver).send_keys(Keys.ESCAPE).perform()
    # pi.press('esc')



chromeProcess, driver = prepareChromeAndSelenium()
scrapeDataFrom(driver)
