from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import random

options = Options()
options.headless = True

# Configure o WebDriver para o Firefox em modo headless
driver = webdriver.Firefox(options=options)
url_do_formulario = 'https://qa-01.receiv.it/testeqa.php'


