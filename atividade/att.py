import pandas as pd
# Ler o arquivo "Alunos.csv"
df = pd.read_csv('atividade/alunos.csv')
# Printar todo o arquivo
print(df)
# printar as 5 primeiras linhas do arquivo
print(df.head())

# printar somente os alunos ativos
alunos_ativos = df[df['Status'] == 'Ativo']
print(alunos_ativos)

# printar o agrupamento por curso e a quantidade de alunos

venda_agrupada = df.groupby(["Curso"])["Aluno"].count()

print(venda_agrupada)

# criar um arquivo csv com o resultado do agrupamento
venda_agrupada.to_csv("Agrupamento", index=False)