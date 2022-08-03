
from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

from time import sleep

from selenium.webdriver import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.linkedin.com/login/')
sleep(2)

email = driver.find_element(By.XPATH, '// *[@id="session_key"]')
email.send_keys('lucimar.a.s@hotmail.com')
sleep(2)

senha = driver.find_element(By.XPATH, '//*[@id="session_password"]')
email.send_keys('Pcp101161')
sleep(2)

btn_login = driver.find_element(
    By.XPATH, '//*[@id="session_password"]')
btn_login.click()

print("")
