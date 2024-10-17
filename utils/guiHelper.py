from time import sleep
import pyautogui as pi

def splitTheData(thisData):
    fileDir = ''.join(thisData.split("/")[:-1])
    fileName = thisData.split("/")[-1]    
    return fileDir, fileName

def selectTheMedia(imageLocation):
    contentLocation, contentName = splitTheData(imageLocation)
    sleep(0.5)
    pi.hotkey('ctrl', 'l')
    sleep(1)
    pi.typewrite(contentLocation)
    sleep(0.5)
    pi.press('enter')
    for _ in range(6):
        sleep(0.2)
        pi.press('tab')
    sleep(0.3)
    pi.typewrite(contentName)
    sleep(0.3)
    pi.press('enter')
    sleep(1)