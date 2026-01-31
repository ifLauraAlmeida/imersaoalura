from utils import *
import pandas as pd
import numpy as np

# LIMPAR E PREPARAR OS DADOS
pd.set_option("display.max_columns", None)
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

print(df.isnull().sum())
print(df['work_year'].unique()) #nan - not a number
print(df[df.isnull().any(axis=1)])

# Por que é importante identificar dados nulos?
# Eles são falta de informação, ignorá-los quebra
# conclusões, gera estatísticas erradas, modelos
# falham ou aprendem errado e geram erros silenciosos.
# Numa média entre 3 valores de salário onde um desses
# é nulo, você calcula a média dividindo por três,
# mas o valor de um deles existe, apenas não está
# lá o que gera uma média errada, trazem conclusões
# erradas e de forma lógica, decisões erradas.

df_salarios = pd.DataFrame(
    {
        "nome": ["Ana", "Bruno", "Carlos", "Daniele", "Val"],
        "salario": [4000, np.nan, 5000, np.nan, 100000],
    }
)

# para arrumar nulos com MÉDIA

cabecalho("PREENCHENDO NULOS COM MEDIA")

df_salarios["salario_media"] = df_salarios["salario"].fillna(
    df_salarios["salario"].mean().round(2)
)
# fillna - preencher no
# mean - média
# round(2) - arrendondar com duas casas decimais

print(df_salarios)
divisoria()

# para arrumar nulos com MEDIANA

cabecalho("PREENCHENDO NULOS COM MEDIA")

# se tiver um valor muito destoante, como outliers, podem apresentar um erro
# no calculo da média pra preencher os dados nulos, nesse caso aplica-se a
# mediana.

df_salarios["salario_mediana"] = df_salarios["salario"].fillna(
    df_salarios["salario"].median().round(2)
)
print(df_salarios)
divisoria()

#EMPLORANDO ARRUMAR NULOS

df_temperaturas = pd.DataFrame(
    {
        "Dia": ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"],
        "Temperatura": [30, np.nan, np.nan, 28, 27],
    }
)

cabecalho("PREENCHENDO COM O VALOR ANTERIOR")
df_temperaturas["preenchido_ffill"] = df_temperaturas["Temperatura"].ffill()
print(df_temperaturas)
divisoria()

cabecalho("PREENCHENDO COM O VALOR POSTERIOR")
df_temperaturas["preenchido_bfill"] = df_temperaturas["Temperatura"].bfill()
print(df_temperaturas)
divisoria()

#PREENCHENDO COM "NÃO INFORMADO"

df_cidades = pd.DataFrame({
    "nome": ["Ana", "Bruno", "Carlos", "Daniele", "Val"],
    "cidade":["São Paulo",np.nan,"Curitiba",np.nan,"Belém"]
})

df_cidades["cidade_preenchida"] = df_cidades["cidade"].fillna("não informado")
print(df_cidades)

#Temos no DF principal 130mil dados, nesse caso não é penoso se deletarmos
#os 10 dados nulos.
#Criaremos uma nova variavel para armazenar esse dataframe limpo

df_limpo = df.dropna() #dropna - remove dados nulos
print(df_limpo.isnull().sum())
print(df_limpo.head())

#O campo WORK YEAR é tipo float64, mas o ano não precisa ser float64, pode
#ser inteiro, como fazer essa conversão?
print(df_limpo.info()) #verifica os dtype 
df_limpo = df_limpo.assign(work_year = df_limpo['work_year'].astype('int64'))
print(df_limpo['work_year'])


