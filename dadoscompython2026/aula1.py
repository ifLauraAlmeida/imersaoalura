from utils import *
import pandas as pd

pd.set_option("display.max_columns", None)

df = pd.read_csv(
    "https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv"
)

# print(df.head())
# print(df.info())
# print(df.describe())
# print(df.shape)
# linhas, colunas = df.shape[0], df.shape[1]
# print(f'Esse database tem {linhas} linhas e {colunas} colunas.')
# print(df.columns)
novos_nomes = {
    "work_year": "ano",
    "experience_level": "senioridade",
    "employment_type": "contrato",
    "job_title": "cargo",
    "salary": "salario",
    "salary_currency": "moeda",
    "salary_in_usd": "usd",
    "employee_residence": "residencia",
    "remote_ratio": "remoto",
    "company_location": "empresa",
    "company_size": "tamanho",
}
df.rename(columns=novos_nomes, inplace=True)


cabecalho("INDEX E TÍTULO DE COLUNAS")
for i, l in enumerate(df.columns):
    print(f"{i:<22}{l:>3}")
divisoria()

cabecalho("DATABASE 3 PRIMEIROS VALORES")
print(df.head(3))
divisoria()

#      => EXPLORANDO VÁRIAVEIS CATEGÓRICAS
# Váriaveis categóricas são colunas que guardam categorias/rótulos,
# e não números para cálculo, elas representam tipos, grupos ou classes.
# É interessante para avaliar a frequência de certos tipos, por exemplo
# quantos juniors tem nesse banco e por assim adiante.

cabecalho("EXPLORANDO SENIORIDADE")
explorar(df, "senioridade")
divisoria()

cabecalho("EXPLORANDO CONTRATO")
explorar(df, "contrato")
divisoria()

cabecalho("EXPLORANDO REMOTO")
explorar(df, "remoto")
divisoria()

cabecalho("TAMANHO DA EMPRESA")
explorar(df, "tamanho")
divisoria()

#      => RENOMEANDO AS CATEGORIAS DAS COLUNAS
# Utiliza-se novamente o replace. Iremos criar um dicionário com
# a chave pertencente anteriormente e as novas.

subs_senioridade = {
  "SE": "Senior", 
  "MI": "Pleno", 
  "EN": "Junior", 
  "EX": "Executivo"
}
df["senioridade"] = df["senioridade"].map(subs_senioridade)  
# map faz a função do replace
cabecalho("RE-EXPLORANDO SENIORIDADE")
explorar(df, "senioridade")
divisoria()

subs_contrato = {
    "FT": "Tempo Integral",
    "PT": "Tempo Parcial",
    "FL": "Freelancer",
    "CT": "Contrato",
}
df["contrato"] = df["contrato"].map(subs_contrato)
cabecalho("REEXPLORANDO CONTRATO")
explorar(df, "contrato")
divisoria()

subs_remoto= {
  0: 'Presencial',
  50: 'Híbrido',
  100: 'Remoto'
}
df['remoto']=df['remoto'].map(subs_remoto)
cabecalho('REEXPLORANDO REMOTO')
explorar(df,'remoto')
divisoria()

subs_tamanho = {
    "S": "Pequena",
    "M": "Média",
    "L": "Grande",
}
df["tamanho"] = df["tamanho"].map(subs_tamanho)
cabecalho("REEXPLORANDO TAMANHO")
explorar(df, "tamanho")
divisoria()

print(df.describe(include="object"))
#count = quantidade de valores por coluna
#unique = quantos tipos tem
#top = os que mais se repetem
#freq = quantas vezes o top se repete
