from selenium import webdriver

from selenium.webdriver import Keys

from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from time import sleep

from selenium.webdriver.common.by import By

import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

lista_empresas = ['PETR4', 'VIIA3', 'BBDC4', 'WEGE3', 'LEVE3', 'AZUL4',
                  'GOLL4', 'CEAB3', 'BRML3', 'COGN3', 'CVCB3', 'GGBR4', 'MDNE3']

driver.get(
    'https://br.advfn.com/')
sleep(2)

empresas_cotacao = list()

for empresa in lista_empresas:
    #driver.find_element(By.XPATH, '//*[@id="header__search"]').click()
    input_busca = driver.find_element(
        By.XPATH, '//*[@id="headerQuickQuoteSearch"]')
    input_busca.send_keys(empresa)
    sleep(2)
    input_busca.send_keys(Keys.ENTER)
    sleep(2)

    span_val = driver.find_element(
        By.XPATH, '//*[@id="quoteElementPiece1"]')

    cotacao_valor = span_val.text
 
    print(f'Valor da cotação da {empresa}: {cotacao_valor} reais')

    dados = list()
    dados.append(empresa)
    dados.append(cotacao_valor)
    empresas_cotacao.append(dados[:])
    dados.clear()

print(empresas_cotacao)

planilha = pd.DataFrame(empresas_cotacao)

print(planilha)

planilha.to_excel('./planilha.xlsx')

input('')
