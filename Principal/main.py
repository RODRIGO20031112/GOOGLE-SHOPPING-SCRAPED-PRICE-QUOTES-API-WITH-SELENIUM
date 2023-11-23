from webScrapingAndProcess import choice
from flask import Flask, request

app = Flask(__name__)

@app.route('/api/processNaturalLanguage/LowestPrice', methods=['POST'])
def pnllp():
    data = request.json
    res = choice(data["product"], data["option"])
    return res

# def main():
#     product = str(input("Digite o produto que deseja procurar: "))
#     print("Você deseja o maior custo benefício (Usamos IA para te ajudar!) ou menor preço ? ")
#     option = int(input("Digite 0 para Custo Benefício ou 1 para Menor preço: "))
#     choice(product, option)

if __name__ == '__main__':
    app.run(debug=True)
