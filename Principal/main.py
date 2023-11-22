from webScrapingAndProcess import choice

def main():
    product = str(input("Digite o produto que deseja procurar: "))
    print("Você deseja o maior custo benefício (Usamos IA para te ajudar!) ou menor preço ? ")
    option = int(input("Digite 0 para Custo Benefício ou 1 para Menor preço: "))

    choice(product, option)

if __name__ == "__main__":
    main()
