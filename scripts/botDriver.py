import geckodriver_autoinstaller
from selenium.webdriver import Firefox, FirefoxOptions

def driverTube(search):
    geckodriver_autoinstaller.install()
    options = FirefoxOptions()
    options.headless = True
    browser = Firefox(options=options)

    browser.get('https://www.youtube.com/results?search_query=' + search)
    thumb = browser.find_element_by_id('thumbnail')
    url = str(thumb.get_attribute('href'))

    return url
