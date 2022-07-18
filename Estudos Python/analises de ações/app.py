from selenium import webdriver

from selenium.webdriver import Keys

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from time import sleep

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

lista_empresas = ['PETR4', 'VIIA3', 'BBDC4', 'WEGE3', 'LEVE3', 'AZUL4',
                  'GOLL4', 'CEAB3', 'BRML3', 'COGN3', 'CVCB3', 'GGBR4', 'MDNE3']

driver.get('https://economia.uol.com.br/cotacoes/bolsas/')
sleep(3)
for empresa in lista_empresas:
    input_busca = driver.find_element(By.XPATH, '//*[@id="filled-normal"]')
    input_busca.send_keys(empresa)
    sleep(5)
    input_busca.send_keys(Keys.ENTER)
    sleep(3)

    span_val = driver.find_element(
        By.XPATH, '//span[@class="chart-info-val ng-binding"]')

    cotacao_valor = span_val.text

    print(f'Valor da cotação da {empresa}: {cotacao_valor} reais')


input('')
