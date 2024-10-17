import json
import time
from utils.setupSelenium import prepareChromeAndSelenium

from utils.linkedInPost import makePostOnLinkedIn
from utils.instagramPost import makePostOnInstagram


chromeProcess, driver = prepareChromeAndSelenium()
linkedInPostData = {'content': 'Contenr hERE!', 'imageLocation': ''}
makePostOnLinkedIn(driver, linkedInPostData)
