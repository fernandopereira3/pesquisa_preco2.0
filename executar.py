from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True 

navegador = webdriver.Firefox()
navegador.get('https://www.olx.com.br')

# elemento = navegador.find_elements(By.CSS_SELECTOR, 'div')
# print(elemento)