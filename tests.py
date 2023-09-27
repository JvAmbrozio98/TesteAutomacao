from selenium import webdriver
import random
import string

# Caminho para o GeckoDriver // Path to the GeckoDriver
gecko_driver_path = 'geckodriver'

# Configure the WebDriver for Firefox // Configuracao do WebDriver para Firefox
driver = webdriver.Firefox()

# URL of the app // URL do aplicativo 
form_url = "https://qa-01.receiv.it/testeqa.php"

# Open the Firefox browser and navigate to the form URL // Abrir o Navegador e ir ate o site 
driver.get(form_url)

# From fields // Campos dos formularios 
name_field = driver.find_element_by_id("nome")
cpf_field = driver.find_element_by_id("cpf")
age_field = driver.find_element_by_id("idade")
adrees_field = driver.find_element_by_id("endereco")
neigberhood_field = driver.find_element_by_id("bairro")
city_field = driver.find_element_by_id("cidade")
value_field = driver.find_element_by_id("valor")
fees_field = driver.find_element_by_id("juros")
month_field = driver.find_element_by_id("meses")
masculine_field = driver.find_element_by_name("masculino")
feminine_field = driver.find_element_by_name("feminino")
button = driver.find_element_by_tag_name("button")

random_name = ''.join(random.choices(string.ascii_letters, k=10))
random_cpf = f"{random.randint(100, 999):03}.{random.randint(100, 999):03}.{random.randint(100, 999):03}-{random.randint(10, 99):02}"
random_age = random.randint(18,100)
random_address = f" {random.choice(['Rua 0001', 'Rua 0002', 'RUa 0003'])}, {random.randint(1, 99999)}"
random_neigberhood = f" {random.choice(['Bairro 0001', 'Bairro 0002', 'Bairro 0003','Bairro 0004','Bairro 0005'])}"
random_city = f" {random.choice(['Cidade 0001', 'Cidade 0002', 'Cidade 0003','Cidade 0004','Cidade 0005'])}"
random_value = random.randint(1,1000000)
random_fees = random.randint(1,100)
random_month = random.randint(1,12)
random_gender = random.choice([masculine_field,feminine_field])




name_field.send_keys(random_name)
cpf_field.send_keys(random_cpf)
age_field.send_keys(random_age)
adrees_field.send_keys(random_address)
neigberhood_field.send_keys(random_neigberhood)
city_field.send_keys(random_city)
value_field.send_keys(random_value)
fees_field.send_key(random_fees)
month_field.send_keys(random_month)
click_choice = random_gender
click_choice.click()



# Submit the form // Enviar formulario

button.click()

# Close the browser // Fechar o navegador
driver.quit()