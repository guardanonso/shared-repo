from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import requests
from bs4 import BeautifulSoup

year = int(input())

chrome_driver = ChromeDriverManager().install()
chrome_service = Service(chrome_driver)
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = Chrome(service=chrome_service, options = options)
driver.get("https://basketball.realgm.com/nba/players/2024")
driver.implicitly_wait(10)
a = driver.find_element(By.XPATH, "//div/button[@class='Button__StyledButton-a1qza5-0 fLZgds']")
a.click()
driver.implicitly_wait(10)
b = driver.find_element(By.XPATH, "//div/select[@onchange='open_network(this.options[this.selectedIndex].value)']")
b.click()
driver.implicitly_wait(10)
c = driver.find_element(By.XPATH, f"//select/option[@value='/nba/players/{year}']")
c.click()
player_name_elements = driver.find_elements(By.XPATH, '//tbody/tr/td[@data-th="Player"]')

player_names = [element.text for element in player_name_elements]

for name in player_names:
    print(name)

driver.quit()
time.sleep(10000)
html = driver.page_source


