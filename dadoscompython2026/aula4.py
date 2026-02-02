import streamlit as st
import pandas as pd
import plotly.express as px

# --- Configuração da Página ---
st.set_page_config(
    page_title="Dashboard de Salários na Área de Dados",
    page_icon="📊",
    layout="wide",
)

# --- Carregamento dos dados ---
df = pd.read_csv("https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv")

# --- Barra Lateral (Filtros) ---
st.sidebar.header("🔍 Filtros")

anos_disponiveis = sorted(df['ano'].unique())
anos_selecionados = st.sidebar.multiselect("Ano", anos_disponiveis, default=anos_disponiveis)

senioridades_disponiveis = sorted(df['senioridade'].unique())
senioridades_selecionadas = st.sidebar.multiselect("Senioridade", senioridades_disponiveis, default=senioridades_disponiveis)

contratos_disponiveis = sorted(df['contrato'].unique())
contratos_selecionados = st.sidebar.multiselect("Tipo de Contrato", contratos_disponiveis, default=contratos_disponiveis)

tamanhos_disponiveis = sorted(df['tamanho_empresa'].unique())
tamanhos_selecionados = st.sidebar.multiselect("Tamanho da Empresa", tamanhos_disponiveis, default=tamanhos_disponiveis)

# --- Filtragem ---
df_filtrado = df[
    (df['ano'].isin(anos_selecionados)) &
    (df['senioridade'].isin(senioridades_selecionadas)) &
    (df['contrato'].isin(contratos_selecionados)) &
    (df['tamanho_empresa'].isin(tamanhos_selecionados))
]

# --- Conteúdo Principal ---
st.title("🎲 Dashboard de Análise de Salários na Área de Dados")
st.markdown("Explore os dados salariais na área de dados. Use os filtros à esquerda para refinar sua análise.")

# --- Métricas Principais (KPIs) ---
st.subheader("📊 Métricas Gerais")

if not df_filtrado.empty:
    salario_medio = df_filtrado['usd'].mean()
    salario_mediano = df_filtrado['usd'].median()
    desvio = df_filtrado['usd'].std()
    perc25 = df_filtrado['usd'].quantile(0.25)
    perc75 = df_filtrado['usd'].quantile(0.75)
    total_registros = df_filtrado.shape[0]
    cargo_mais_frequente = df_filtrado["cargo"].mode()[0]
    
    # Salário médio remoto x presencial
    salarios_remoto = df_filtrado.groupby('remoto')['usd'].mean()
else:
    salario_medio = salario_mediano = desvio = perc25 = perc75 = 0
    total_registros = 0
    cargo_mais_frequente = ""
    salarios_remoto = pd.Series(dtype=float)

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Salário médio", f"${salario_medio:,.0f}")
col2.metric("Salário mediano", f"${salario_mediano:,.0f}")
col3.metric("Desvio padrão", f"${desvio:,.0f}")
col4.metric("Total de registros", f"{total_registros:,}")
col5.metric("Cargo mais frequente", cargo_mais_frequente)

# Insights automáticos
if salario_medio > 100000:
    st.info("💡 Salário médio alto! Compare cargos e senioridades para insights detalhados.")

st.markdown("---")

# --- Tabs para gráficos ---
tab1, tab2, tab3 = st.tabs(["📈 Salários", "🧰 Cargos", "🌍 Países"])

# --- Tab Salários ---
with tab1:
    if not df_filtrado.empty:
        # Distribuição e Boxplot
        col1, col2 = st.columns(2)
        with col1:
            fig_hist = px.histogram(df_filtrado, x='usd', nbins=30,
                                    title="Distribuição de salários anuais",
                                    labels={'usd': 'Faixa salarial (USD)', 'count': ''})
            fig_hist.update_layout(title_x=0.1)
            st.plotly_chart(fig_hist, use_container_width=True)
        with col2:
            fig_box = px.box(df_filtrado, x='cargo', y='usd', title="Boxplot por cargo", points="all")
            fig_box.update_layout(title_x=0.1)
            st.plotly_chart(fig_box, use_container_width=True)
        
        # Evolução temporal
        if len(anos_selecionados) > 1:
            evolucao = df_filtrado.groupby('ano')['usd'].mean().reset_index()
            fig_line = px.line(evolucao, x='ano', y='usd', title="Evolução do salário médio por ano")
            fig_line.update_layout(title_x=0.1)
            st.plotly_chart(fig_line, use_container_width=True)

        # Salário médio remoto x presencial
        st.subheader("Remoto x Presencial")
        fig_remoto = px.bar(salarios_remoto.reset_index(), x='remoto', y='usd',
                            labels={'remoto':'Tipo de trabalho','usd':'Salário médio (USD)'},
                            color='remoto', text='usd')
        st.plotly_chart(fig_remoto, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir nesta aba.")

# --- Tab Cargos ---
with tab2:
    if not df_filtrado.empty:
        top_cargos = df_filtrado.groupby('cargo')['usd'].mean().nlargest(10).sort_values().reset_index()
        fig_cargos = px.bar(top_cargos, x='usd', y='cargo', orientation='h',
                            title="Top 10 cargos por salário médio",
                            labels={'usd':'Média salarial anual (USD)','cargo':''})
        fig_cargos.update_layout(title_x=0.1, yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig_cargos, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir nesta aba.")

# --- Tab Países ---
with tab3:
    if not df_filtrado.empty:
        df_ds = df_filtrado[df_filtrado['cargo'] == 'Data Scientist']
        media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()
        fig_paises = px.choropleth(media_ds_pais,
                                   locations='residencia_iso3',
                                   color='usd',
                                   color_continuous_scale='rdylgn',
                                   title='Salário médio de Data Scientist por país',
                                   labels={'usd':'Salário médio (USD)','residencia_iso3':'País'})
        fig_paises.update_layout(title_x=0.1)
        st.plotly_chart(fig_paises, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir nesta aba.")

st.markdown("---")
st.subheader("📋 Dados Detalhados")
st.dataframe(df_filtrado)

# --- Botão de Download ---
st.download_button("💾 Baixar CSV filtrado", df_filtrado.to_csv(index=False), "dados_filtrados.csv")
