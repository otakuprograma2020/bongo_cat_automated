from selenium.webdriver import Chrome
from os import path, system
from webScrape import WebScrape
from time import sleep
dir = path.dirname(__file__)
chrome_path = path.join(dir, 'selenium','webdriver','chromedriver.exe')
webS = WebScrape()
url = 'https://bongo.cat/'
with Chrome(chrome_path,options=webS.optionsChrome(True)) as driver:
    driver.get(url)
    elmnt = driver.find_element_by_tag_name('html')
    while True:
        elmnt.send_keys('1')
        sleep(0.5)
        elmnt.send_keys('1')
        sleep(0.5)

        elmnt.send_keys('3')
        sleep(0.5)

        elmnt.send_keys('6')
        sleep(0.5)

        elmnt.send_keys('5')
        sleep(0.5)
#####################################
        elmnt.send_keys('1')
        sleep(0.5)
        elmnt.send_keys('1')
        sleep(0.5)

        elmnt.send_keys('3')
        sleep(0.5)

        elmnt.send_keys('8')
        sleep(0.5)

        elmnt.send_keys('6')
        sleep(0.5)
#####################################
        elmnt.send_keys('1')
        sleep(0.5)
        elmnt.send_keys('1')
        sleep(0.5)

        elmnt.send_keys('0')
        sleep(0.5)

        elmnt.send_keys('7')
        sleep(0.5)

        elmnt.send_keys('6')
        sleep(0.5)

        elmnt.send_keys('5')
        sleep(0.5)
        elmnt.send_keys('3')
        sleep(0.5)
#####################################
        elmnt.send_keys('9')
        sleep(0.5)
        elmnt.send_keys('9')
        sleep(0.5)

        elmnt.send_keys('7')
        sleep(0.5)

        elmnt.send_keys('4')
        sleep(0.5)

        elmnt.send_keys('6')
        sleep(0.5)

        elmnt.send_keys('4')
        sleep(0.5)

        