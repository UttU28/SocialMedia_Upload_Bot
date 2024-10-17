import subprocess 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromeDriverPath = 'C:/Users/utsav/OneDrive/Desktop/SocialMedia_Upload_Bot/chromeDriver/chromedriver.exe'

options = Options()
options.add_experimental_option("debuggerAddress", "localhost:8989")
options.add_argument(f"webdriver.chrome.driver={chromeDriverPath}")
options.add_argument("--disable-notifications")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
options.add_argument("window-size=1920x1080")


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