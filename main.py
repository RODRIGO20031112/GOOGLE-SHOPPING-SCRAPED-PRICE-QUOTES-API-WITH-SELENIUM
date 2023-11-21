from selenium.webdriver.chrome.service import Service as ChromeService
from processNaturalLanguage import processNaturalLanguage
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless")

chrome_service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service, options=options)

product = str(input("Digite o produto que deseja procurar: "))
pedido = ""

driver.get(f"https://www.google.com/search?q={product}&tbm=shop")

titulos = driver.find_elements(By.CLASS_NAME, "sh-np__product-title.translate-content")
lojas = driver.find_elements(By.CLASS_NAME, "sh-np__seller-container")
fretes = driver.find_elements(By.CLASS_NAME, "U6puSd")
precos = driver.find_elements(By.CLASS_NAME, "hn9kf")

for titulo, preco, loja, frete in zip(titulos, precos, lojas, fretes):
    pedido += f"Título: {titulo.text}\nPreço: {preco.text}\nLoja: {loja.text}\nFrete: {frete.text}\n"

driver.quit()

# print(pedido + "Me de a melhor opção")

print(processNaturalLanguage(pedido + "Me de a melhor opção"))