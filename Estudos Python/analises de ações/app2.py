from selenium import webdriver

from selenium.webdriver import Keys

from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options

from time import sleep

from selenium.webdriver.common.by import By

from datetime import datetime

import pandas as pd

options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)

empresas = ['PETR4', 'VIIA3', 'BBDC4']
# , 'WEGE3', 'LEVE3', 'AZUL4','GOLL4', 'CEAB3', 'BRML3', 'COGN3', 'CVCB3', 'GGBR4', 'MDNE3']
cotacao = list()
data_hora = list()

driver.get(
    'https://br.advfn.com/')
sleep(2)

for empresa in empresas:
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

    #print(f'Valor da cotação da {empresa}: {cotacao_valor} reais')

    cotacao.append(cotacao_valor)
    data_hora.append(datetime.now().strftime('%d/%m/%y %H:%M:%S'))
    print(f'Buscando cotação da {empresa} ...')


dados = {
    'Empresa': empresas,
    'Cotação': cotacao,
    'Data/Hora': data_hora,
}

#print(dados)

pd_empresas = pd.DataFrame(dados)
print(pd_empresas)
pd_empresas.to_excel('./ Cotações empresas.xlsx', index=False)

input('')
