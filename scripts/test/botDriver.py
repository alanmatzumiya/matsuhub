import geckodriver_autoinstaller
from selenium.webdriver import Firefox
from time import sleep

geckodriver_autoinstaller.install()  # Check if the current version of geckodriver exists
                                     # and if it doesn't exist, download it automatically,
                                     # then add geckodriver to path


browser = Firefox()
browser.get('http://127.0.0.1:5000/home/music')

while True:
    
    browser.save_screenshot('test.png')
    sleep(5)
