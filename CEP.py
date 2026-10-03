import requests

CEP = input("digite seu CEP: ")

url = f"https://viacep.com.br/ws/{CEP}/json/"

dados = requests.get(url)

resposta= dados.json()

print(f"você mora na rua {resposta["logradouro"]}. no bairro {resposta["bairro"]}. na cidade de {resposta["localidade"]}")

