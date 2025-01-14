# para instalar a biblioteca panda no vs
# pip install pandas
'''
import pandas as pd // e preciso disso aqui para mexer na biblioteca

'''
import pandas as pd

# lendo arquivo
df = pd.read_csv('AULA/aula09/dados_vendas.csv')

'''
# mostrar o arquivo
print(df.head())#mostra as 5 primeiras linhas do arquivo
print(df.info())
print(df.describe()) #descrição da tabela um pouco mais detalhada

=====================================================================

# vamos aqui acessar a coluna e eu to fltrando a data depois e igual a essa data
vendas_fevereiro = df[df['Data de Venda'] >= '2023-02-01']

# mostra
print(vendas_fevereiro)

# agrupar os itens
# aqui vai agrupar por categoria e depois soma com sum
vendas_por_categoria = df.groupby("Categoria")['Quantidade Vendida'].sum()
print(vendas_por_categoria)

# se quiser mais de 1 coluna
vendas_por_categoria = df.groupby(["Categoria", "Produto"])['Quantidade Vendida'].sum()
print(vendas_por_categoria)

=========================================================================================

# criar uma nova coluna
df['Receita'] = df['Quantidade Vendida'] * df['Preço Unitário']

# criar uma nova coluna
df['Receita'] = df['Quantidade Vendida'] * df['Preço Unitário']

receita_categoria = df.groupby(['Categoria', 'Produto'])['Receita'].sum()

print(receita_categoria)

# para mostra quantas vezes aparece
receita_categoria = df.groupby(['Categoria', 'Produto'])['Receita'].count()

# criar uma pagina com apenas a categoria escolhida
receita_categoria.to_csv("Agrupamento", index=False)
'''

