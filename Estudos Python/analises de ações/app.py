from selenium import webdriver

from selenium.webdriver import Keys

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from time import sleep

from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get('https://economia.uol.com.br/cotacoes/bolsas/')

input_busca = driver.find_element(By.ID, 'filled-normal')
input_busca.send_keys('PETR4.SA')
sleep(2)

input_busca.send_keys(Keys.ENTER)

span_val = driver.find_element(By.XPATH, '//span[@class="chart-info-val ng-binding"]')
cotacao_valor = span_val.text
print(f'Valor da cotação da PETR4: {cotacao_valor} reais')

input('')