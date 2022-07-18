from selenium import webdriver

from selenium.webdriver import Keys

from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from time import sleep

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

lista_empresas = ['PETR4', 'VIIA3', 'BBDC4', 'WEGE3', 'LEVE3', 'AZUL4',
                  'GOLL4', 'CEAB3', 'BRML3', 'COGN3', 'CVCB3', 'GGBR4', 'MDNE3']

driver.get(
    'https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/cotacoes/')
sleep(5)
for empresa in lista_empresas:
    driver.find_element(By.XPATH, '//*[@id="sb-search-open"]/span').click()
    input_busca = driver.find_element(
        By.XPATH, '//*[@id="query"]')
    input_busca.send_keys(empresa)
    sleep(5)
    input_busca.send_keys(Keys.ENTER)
    sleep(5)

    span_val = driver.find_element(
        By.XPATH, '//*[@id="quotes-container"]/div/span/span')

    cotacao_valor = span_val.text

    print(f'Valor da cotação da {empresa}: {cotacao_valor} reais')


input('')
