# # selenium 4
# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#
# # Переход к странице курса
# driver.get("https://stepik.org/course/104774")
# time.sleep(5)

import time
from selenium import webdriver

url = 'https://stepik.org/course/104774'
browser = webdriver.Chrome()
browser.get(url)
time.sleep(5)