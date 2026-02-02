from utils import *
from tratamento import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

pd.set_option("display.max_columns", None)

df = pd.read_csv(
    "https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv"
)

novosnomes(df)
novas_sub_categorias(df)

df_limpo = df.dropna()

df_limpo = df_limpo.assign(ano=df_limpo["ano"].astype("int64"))

# df_limpo["senioridade"].value_counts().plot(
#     kind="bar", title="Distribuição de Senioridade"
# )
# plt.show()

# sns.barplot(data=df_limpo, x='senioridade', y='usd')
# plt.title("Media Salarial Por Senioridade")
# plt.show()

ordem = df_limpo.groupby("senioridade")["usd"].mean().sort_values(ascending=False).index

# plt.figure(figsize=(8,5))
# sns.barplot(data=df_limpo, x='senioridade', y='usd', order=ordem)
# plt.title("Media Salarial Por Senioridade")
# plt.xlabel("Nível de Senioridade")
# plt.ylabel("Sálario Médio Anual (USD)")
# plt.show()

# plt.figure(figsize=(8,5))
# sns.histplot(df_limpo['usd'],bins=40,kde=True) #bins - largura das barras kde - linha 
# plt.title("Distribuição dos Salários Anuais")
# plt.xlabel("Sálario em USD")
# plt.ylabel("Frequência")
# plt.show()

# plt.figure(figsize=(8,5))
# sns.boxplot(x=df_limpo['usd']) 
# plt.title("Boxplot Salário")
# plt.xlabel("Sálario em USD")
# plt.show()

# ordem_senioridade = ['Junior', 'Pleno', 'Senior', 'Executivo']
# plt.figure(figsize=(8,5))
# sns.boxplot(x='senioridade',y='usd', data=df_limpo, order=ordem_senioridade, palette='Set2', hue='senioridade')
# plt.title("Boxplot Distribuição Salarial por Senioridade")
# plt.xlabel("Sálario em USD")
# plt.show()

# senioridade_media_salario = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).reset_index()
# fig = px.bar(senioridade_media_salario,
#              x='senioridade',
#              y='usd',
#              title='Média Salarial por Senioridade',
#              labels={'senioridade': 'Nível de Senioridade', 'usd': 'Média Salarial Anual (USD)'})
# fig.show()

# remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
# remoto_contagem.columns = ['tipo_trabalho','quantidade']

# fig = px.pie(remoto_contagem,
#              names='tipo_trabalho',
#              values='quantidade',
#              title='Proporção dos Tipos de Trabalho',
#              hole=0.5)
# fig.update_traces(textinfo='percent+label')
# fig.show()
##########################DESAFIO FIM DA AULA3
# 1️⃣ Filtrar apenas Data Scientists
ds = df[df['cargo'] == 'Data Scientist']

# 2️⃣ Agrupar por país e calcular o salário médio
salarios_por_pais = ds.groupby('empresa')['salario'].mean()

# 3️⃣ Mostrar o salário médio por país
print("Salário médio por país:\n", salarios_por_pais)

# 4️⃣ Calcular e mostrar a diferença entre o país com maior e menor salário
dif_max_min = salarios_por_pais.max() - salarios_por_pais.min()
print("\nDiferença de salário entre países (máx - mín):", dif_max_min)

# 5️⃣ Plotar gráfico de barras
salarios_por_pais.sort_values().plot(kind='bar', figsize=(10,6), color='skyblue')
plt.ylabel('Salário médio (USD)')
plt.title('Salário médio de Data Scientists por país')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
