# Biblioteca instaladas: selenium, pandas

import login

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

# Abrir o navegador e abrir a pagina do Linkedin
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.linkedin.com/login/')

# Logar na minha conta
senha = login.password()
email = login.email()

# Pesquisar na barra de buscar por "Python"

# Selecionar pessoas no filtro de busca

# Mandar convite para cada pessoa que esteja na pesquisa


Print(senha)
Print(email)
