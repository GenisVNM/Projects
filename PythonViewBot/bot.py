#Selenium Webdriver must be installed for this to work

import time;
from selenium import webdriver;

#time to refresh page (seconds)
Timer = 120

#youtube link
link = 'https://www.youtube.com/watch?v=mZBvCV2eT4c&ab_channel=GenisVNM'

#number of views
views = 1000

driver = webdriver.Chrome()
driver.get(link)

for i in range(views):
    time.sleep(Timer)
    driver.refresh()
    print(i)
