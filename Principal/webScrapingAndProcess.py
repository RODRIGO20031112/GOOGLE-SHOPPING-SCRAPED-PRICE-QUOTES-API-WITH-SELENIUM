from selenium.webdriver.chrome.service import Service as ChromeService
from processNaturalLanguage import processNaturalLanguage
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import re

options = webdriver.ChromeOptions()
options.add_argument("--headless")

chrome_service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service, options=options)

def choice(product, choice):

    pedido1 = ""
    pedido2 = ""

    driver.get(f"https://www.google.com/search?q={product}&tbm=shop")

    titulos_x = driver.find_elements(By.CLASS_NAME, "sh-np__product-title.translate-content")
    lojas_x = driver.find_elements(By.CLASS_NAME, "sh-np__seller-container")
    fretes_x = driver.find_elements(By.CLASS_NAME, "U6puSd")
    precos_x = driver.find_elements(By.CLASS_NAME, "hn9kf")

    titulos_y = driver.find_elements(By.CLASS_NAME, "tAxDx")
    lojas_y = driver.find_elements(By.CLASS_NAME, "aULzUe")
    fretes_y = driver.find_elements(By.CLASS_NAME, "vEjMR")
    precos_y = driver.find_elements(By.CLASS_NAME, "a8Pemb")

    soma = 0
    lista = []
    for titulo_x, preco_x, loja_x, frete_x, titulo_y, preco_y, loja_y, frete_y in zip(titulos_x, precos_x, lojas_x, fretes_x, titulos_y, precos_y, lojas_y, fretes_y):
        if frete_x.text and frete_y.text: soma += 1
        lista.append({
        "Título": titulo_x.text,
        "Preço": preco_x.text,
        "Loja": loja_x.text,
        "Frete": frete_x.text
        })
        lista.append({
        "Título": titulo_y.text,
        "Preço": preco_y.text,
        "Loja": loja_y.text,
        "Frete": frete_y.text
        }) 

        if soma % 2 == 0:
            pedido1 += f"Título: {titulo_x.text}\nPreço: {preco_x.text}\nLoja: {loja_x.text}\nFrete: {frete_x.text}\n"
            pedido1 += f"Título: {titulo_y.text}\nPreço: {preco_y.text}\nLoja: {loja_y.text}\nFrete: {frete_y.text}\n"
        else:
            pedido2 += f"Título: {titulo_x.text}\nPreço: {preco_x.text}\nLoja: {loja_x.text}\nFrete: {frete_x.text}\n"
            pedido2 += f"Título: {titulo_y.text}\nPreço: {preco_y.text}\nLoja: {loja_y.text}\nFrete: {frete_y.text}\n"

    driver.quit()

    if choice == 0:
        resp1 = processNaturalLanguage(pedido1 + "Baseado nos textos acima me de os dados do produto mais em conta") 
        print("Resposta 1 sendo processada. Aguarde...")
        print("Resposta 1 processada com sucesso")
        time.sleep(15)

        resp2 = processNaturalLanguage(pedido2 + "Baseado nos textos acima me de os dados do produto mais em conta")
        print("Resposta 2 sendo processada. Aguarde...")
        print("Resposta 2 processada com sucesso")
        time.sleep(15)

        resp3 = resp1 + resp2
        print("Resposta final sendo processada. Aguarde...")
        # print(processNaturalLanguage(resp3 + "Baseado nos textos acima me de os dados do produto mais em conta"))
        return processNaturalLanguage(resp3 + "Baseado nos textos acima me de os dados do produto mais em conta")
    elif(choice == 1):
        # lista.sort(key=lambda x: float(re.findall(r'[-+]?\d*[.,]\d+|\d+', x["Preço"])[0].replace('.', '').replace(',', '.')))
        lista = [x for x in lista if re.findall(r'[-+]?\d*[.,]\d+|\d+', x["Preço"])]
        lista.sort(key=lambda x: float(re.findall(r'[-+]?\d*[.,]\d+|\d+', x["Preço"])[0].replace('.', '').replace(',', '.')))
        
        data = []
        # for item in lista: print(f"Título: {item['Título']}\nPreço: {item['Preço']}\nLoja: {item['Loja']}\nFrete: {item['Frete']}\n")

        for item in lista:
            data.append({
                "Frete": item['Frete'],
                "Preço": item['Preço'],
                "Loja": item['Loja'],
                "Título": item['Título']
            })

        return data
    else:
        print("Essa opção não existe.")

# print(pedido1 + "Me de a melhor opção")
# print("\n")
# print(pedido2 + "Me de a melhor opção")

# print(processNaturalLanguage(pedido1 + "Me de a melhor opção"))
# print("\n")
# print(processNaturalLanguage(pedido2 + "Me de a melhor opção"))