# Importando as bibliotecas necessárias
from bs4 import BeautifulSoup
import pandas as pd

# lendo o arquivo da página
caminho = "D:\\WebScraping_Pedidos.html"
with open(caminho, "r", encoding="utf-8") as arquivo:
    conteudo_html = arquivo.read()

# criando o objeto beautiful soup para entender o html
soup = BeautifulSoup(conteudo_html, "html.parser")

# criando uma variavel que armazena o que encontrar de <tabela>
tabela_pedidos = soup.find()

# Utilizando o pandas para ler o arquivo html
df = pd.read_html(str(tabela_pedidos))[0]

# criando arquivo JSON
df.to_json("pedidos.json", orient='records', lines=True, force_ascii=False, indent=4)
print("Pedidos salvos em 'pedidos.json'")

# crioando XLSX
df.to_excel("pedidos.xlsx", index=False)
print("Pedidos salvos em 'pedidos.xlsx'")

# Criando CSV
df.to_csv("pedidos.csv", index=False, encoding='utf-8')
print("Pedidos salvos em 'pedidos.csv'")
