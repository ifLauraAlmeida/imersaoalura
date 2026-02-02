def novosnomes(df):
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

def novas_sub_categorias(df):
    subs_senioridade = {
        "SE": "Senior",
        "MI": "Pleno",
        "EN": "Junior",
        "EX": "Executivo"
    }
    df["senioridade"] = df["senioridade"].map(subs_senioridade)
    
    subs_contrato = {
        "FT": "Tempo Integral",
        "PT": "Tempo Parcial",
        "FL": "Freelancer",
        "CT": "Contrato"
    }
    df["contrato"] = df["contrato"].map(subs_contrato)
    
    subs_remoto = {
        0: "Presencial",
        50: "Híbrido",
        100: "Remoto"
    }
    df["remoto"] = df["remoto"].map(subs_remoto)
    
    subs_tamanho = {
        "S": "Pequena",
        "M": "Média",
        "L": "Grande"
    }
    df["tamanho"] = df["tamanho"].map(subs_tamanho)

