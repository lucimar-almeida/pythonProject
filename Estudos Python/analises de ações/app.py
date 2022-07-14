from selenium import webdriver

from selenium.webdriver import Keys

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from time import sleep


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get('https://economia.uol.com.br/cotacoes/bolsas/')

input_busca = driver.find_element(by=id('filled-normal'))
input_busca.send_keys('PETR4.SA')
sleep(2)

input_busca.send_keys(Keys.ENTER)

input('')