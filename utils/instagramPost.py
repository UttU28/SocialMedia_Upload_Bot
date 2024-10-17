from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from utils.setupSelenium import prepareChromeAndSelenium
from utils.guiHelper import selectTheMedia
import json, os
import pyperclip
import pyautogui as pi

def removeBMP(text):
    return ''.join(char for char in text if ord(char) <= 0xFFFF)

_,thisDriver = prepareChromeAndSelenium()

def makePostOnInstagram(thisDriver, postData):
    thisDriver.get("https://www.instagram.com/")
    thisCaption = """CAPTION HERE!"""

    sleep(2)
    createButton = WebDriverWait(thisDriver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Create']")))
    createButton.click()
    sleep(2)
    postButton = WebDriverWait(thisDriver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Post']")))
    postButton.click()
    sleep(2)
    selectButton = WebDriverWait(thisDriver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Select from computer']")))
    selectButton.click()
    # <button class=" _acan _acap _acas _aj1- _ap30" type="button"></button>
    contentLocation = postData['imageLocation']
    selectTheMedia(contentLocation)
    try:
        selectButton = WebDriverWait(thisDriver, 3).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='OK']")))
        selectButton.click()
    except:
        print("IDK")

    # ratioButton = WebDriverWait(thisDriver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "._acan._acao._acas._aj1-._ap30")))
    # ratioButton = WebDriverWait(thisDriver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, '_acan') and contains(@class, '_acao') and contains(@class, '_acas') and contains(@class, '_aj1-') and contains(@class, '_ap30')]")))
    sleep(5)

    try:
        element = thisDriver.find_element(By.CSS_SELECTOR, "._abfz._abg1")
        print("Element found.")
        element.click()
    except NoSuchElementException:
        print("Element not found.")
    # ratioButton.click()

    selectRatio = WebDriverWait(thisDriver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='9:16']")))
    selectRatio.click()

    nextButton = WebDriverWait(thisDriver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Next']")))
    nextButton.click()
    sleep(1)
    nextButton = WebDriverWait(thisDriver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Next']")))
    nextButton.click()

    currentWord = contentLocation.split("/")[-1].replace(".mp4","")
    print(currentWord)
    thisCaption += f"\n\nCurrent Word: {currentWord} \nFollow to learn New English Words everyday.\n\n#vocab #grevocabulary #grewords #grevocab #ielts #vocab #learning #english #word #wordofgod #wordgasm #wordoftheday #wordofday #meme"
    print(thisCaption)

    captionText = WebDriverWait(thisDriver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".xw2csxc.x1odjw0f.x1n2onr6.x1hnll1o.xpqswwc.xl565be.x5dp1im.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x1w2wdq1.xen30ot.x1swvt13.x1pi30zi.xh8yej3.x5n08af.notranslate")))
    captionText.click()
    captionText.send_keys(removeBMP(thisCaption))

    nextButton = WebDriverWait(thisDriver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Share']")))
    nextButton.click()
