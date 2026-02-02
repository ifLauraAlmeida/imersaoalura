from utils import *
from tratamento import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

plt.figure(figsize=(8,5))
sns.barplot(data=df_limpo, x='senioridade', y='usd', order=ordem)
plt.title("Media Salarial Por Senioridade")
plt.xlabel("Nível de Senioridade")
plt.ylabel("Sálario Médio Anual (USD)")
plt.show()

