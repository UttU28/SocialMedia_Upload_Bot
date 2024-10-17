import json
import time
from utils.setupSelenium import prepareChromeAndSelenium

from utils.linkedInPost import makePostOnLinkedIn
from utils.instagramPost import makePostOnInstagram


chromeProcess, driver = prepareChromeAndSelenium()
# linkedInPostData = {'content': 'Contenr hERE!', 'imageLocation': 'C:/Users/utsav/OneDrive/Desktop/SocialMedia_Upload_Bot/images/Strategies for Success.png'}
# makePostOnLinkedIn(driver, linkedInPostData)

instagramPostData = {'content': 'Contenr hERE!', 'imageLocation': 'C:/Users/utsav/OneDrive/Desktop/SocialMedia_Upload_Bot/images/Strategies for Success.png'}
makePostOnInstagram(driver, instagramPostData)