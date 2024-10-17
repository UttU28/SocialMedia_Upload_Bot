from time import sleep
import pyautogui as pi
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.guiHelper import selectTheMedia


def makePostOnLinkedIn(thisDriver, postData):
    thisDriver.get("https://www.linkedin.com/feed/")
    startPost = WebDriverWait(thisDriver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'share-box-feed-entry__trigger'))
    )
    startPost.click()

    mainPostBox = WebDriverWait(thisDriver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'share-box-v2__modal-phoenix-redesign'))
    )

    ulList = mainPostBox.find_element(By.CSS_SELECTOR, "ul.artdeco-carousel__slider.ember-view")
    addImageButton = ulList.find_elements(By.TAG_NAME, 'li')
    addImageButton[1].click()

    # os.system("xdotool key ctrl+l")
    imageLocation = postData['imageLocation']
    selectTheMedia(imageLocation)


    boxFooter = mainPostBox.find_element(By.CLASS_NAME, 'share-box-footer')
    footerButtons = boxFooter.find_elements(By.TAG_NAME, 'button')

    for button in footerButtons:
        if button.text.lower() == 'next':
            button.click()
            sleep(0.5)
            break
    webdriver.ActionChains(thisDriver).send_keys(postData['content']).perform()

    postThePostFooter = WebDriverWait(thisDriver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'share-creation-state__footer'))
    )
    # postThePostButton = postThePostFooter.find_element(By.CLASS_NAME, 'share-box_actions').click()


if __name__ == '__main__':
    from utils.setupSelenium import prepareChromeAndSelenium
    chromeProcess, driver = prepareChromeAndSelenium()
    postData = {'content': 'Contenr hERE!', 'imageLocation': 'C:/Users/utsav/OneDrive/Desktop/SocialMedia_Upload_Bot/images/Strategies for Success.png'}
    makePostOnLinkedIn(driver, postData)
