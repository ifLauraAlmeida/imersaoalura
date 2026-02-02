from utils import *
from tratamento import *
import pandas as pd

pd.set_option("display.max_columns", None)

df = pd.read_csv(
    "https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv"
)

novosnomes(df)
novas_sub_categorias(df)

df_limpo = df.dropna()

df_limpo = df_limpo.assign(ano = df_limpo["ano"].astype("int64"))



