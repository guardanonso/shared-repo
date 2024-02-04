from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Installa e configura automaticamente il ChromeDriver
chrome_driver = ChromeDriverManager().install()

# Crea un'istanza del servizio Chrome
chrome_service = Service(chrome_driver)
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# Avvia il browser Chrome utilizzando il servizio configurato
driver = Chrome(service=chrome_service, options = options)

# Naviga verso la pagina web desiderata
driver.get("https://basketball.realgm.com/nba/players/2024")
driver.implicitly_wait(10)
a = driver.find_element(By.XPATH, "//div/button[@class='Button__StyledButton-a1qza5-0 fLZgds']")
a.click()
driver.implicitly_wait(10)
b = driver.find_element(By.XPATH, "//div/select[@onchange='open_network(this.options[this.selectedIndex].value)']")
b.click()
driver.implicitly_wait(10)

time.sleep(10)
