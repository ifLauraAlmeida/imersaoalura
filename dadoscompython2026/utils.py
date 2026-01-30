def cabecalho(txt):
    print("=" * 35)
    print(txt.upper().center(35))
    print("=" * 35)


def divisoria():
    print("-" * 35)

def explorar(df,coluna):
    for i, quantidade in df[coluna].value_counts().items():
        print(f'{i:<22}{quantidade:>3}')
