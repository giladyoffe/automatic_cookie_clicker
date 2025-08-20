from selenium import webdriver
from selenium.webdriver.common.by import By
from time import time, sleep

#sel_path = "C:\CodingPython#Work#\selenium_chromedriver\chromedriver.exe"
url = 'http://orteil.dashnet.org/experiments/cookie/'
cookie_driver = webdriver.Chrome()
cookie_driver.get(url)
cookie = cookie_driver.find_element(By.CSS_SELECTOR, 'div#cookie')
upgrade_names = [(c.text.split('-')[0].strip())
                 for c in cookie_driver.find_elements(By.CSS_SELECTOR, '#store div b')[::-1] if len(c.text) > 1]
current_cookies = int(cookie_driver.find_element(By.CSS_SELECTOR, 'div#money').text)
check_purchasable = time() + 5
while True:
    cookie.click()
    if time() >= check_purchasable:
        upgrades_cost = [int(e.text.split('-')[1].strip().replace(',', ''))
                         for e in cookie_driver.find_elements(By.CSS_SELECTOR, '#store div b')[::-1] if len(e.text) > 1]
        for v in upgrades_cost:
            while int(cookie_driver.find_element(By.CSS_SELECTOR, 'div#money').text.replace(',', '')) >= v:
                upgrade = cookie_driver.find_element(By.CSS_SELECTOR, f'div#buy{upgrade_names[upgrades_cost.index(v)]}')
                upgrade.click()
                sleep(0.2)
        check_purchasable = time() + 5
