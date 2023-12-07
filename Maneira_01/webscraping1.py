# importando bibliotecas
import json
from bs4 import BeautifulSoup
import pandas as pd


# lendo o arquivo da página
caminho = "D:\\WebScraping_Pedidos.html"
with open(caminho, "r", encoding="utf-8") as arquivo:
    conteudo_html = arquivo.read()

# criando o objeto beautiful soup
soup = BeautifulSoup(conteudo_html, "html.parser")

# criando uma variavel que armazena o que encontrar de <tabela>
tabela_pedidos = soup.find('table')

# lista para armazenar o data frame
pedidos = []

# comando para salvar na variável todas as linhas da tabela que tem a tag 'tr' (linhas da tabela)
# a partir da segunda linha, pra n pegar o cabeçalho
linhas_tabela = tabela_pedidos.findAll('tr')[1:]

# for para definir onde vai ficar cada coisa na tabela
for linha in linhas_tabela:
    colunas = linha.find_all('td') # pega todas as tags td
    numero_pedido = colunas[0].text
    data = colunas[1].text
    itens = colunas[2].text
    quantidade = colunas[3].text
    preco = colunas[4].text
    total = colunas[5].text
    status = colunas[6].text

    # criando um dicionário para representar o pedido
    data_frame = {
        'N° do Pedido': numero_pedido,
        'Data': data,
        'Itens': itens,
        'Quantidade': quantidade,
        'Preço': preco,
        'Total': total,
        'Status': status}

    # adicionando os pedidos do data frame na lista
    pedidos.append(data_frame)

# criando um dataframe com os pedios
df_pedidos = pd.DataFrame(pedidos)
print(df_pedidos)

# criando arquivo JSON
with open('pedidos.json', 'w', encoding='utf-8') as arq_json:
    json.dump(pedidos, arq_json, ensure_ascii=False, indent=4)
    print("Pedidos salvos em 'pedidos.json'")

# crioando XLSX
df_pedidos.to_excel("pedidos.xlsx", index=False)
print("Pedidos salvos em 'pedidos.xlsx'")

# Criando CSV
df_pedidos.to_csv("pedidos.csv", index=False)
print("Pedidos salvos em 'pedidos.csv'")
