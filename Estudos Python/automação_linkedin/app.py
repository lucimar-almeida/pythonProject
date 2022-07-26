# Biblioteca instaladas: selenium, pandas

import login

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.linkedin.com/login/')

senha = login.password()
email = login.email()








Print(senha)
Print(email)