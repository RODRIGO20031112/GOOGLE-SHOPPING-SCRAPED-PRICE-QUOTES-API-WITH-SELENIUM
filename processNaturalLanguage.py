from password import API_KEY
import requests 
import json

def processNaturalLanguage(pedido):
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    link = "https://api.openai.com/v1/chat/completions"
    id_modelo = "gpt-3.5-turbo"

    body_mensagem = {
        "model": id_modelo,
        "messages": [{"role": "user", "content": f"{pedido}"}]
    }
    body_mensagem = json.dumps(body_mensagem)

    requisicao = requests.post(link, headers=headers, data=body_mensagem)
    # print(requisicao)

    resposta = requisicao.json()
    
    try:
        mensagem = resposta
        return mensagem["choices"][0]["message"]["content"]
    except Exception:
        mensagem = resposta
        return mensagem['error']['message']

# pedido = input("Pedido: ")
# print(processNaturalLanguage(pedido))