import tabula

lista_tabelas = tabula.read_pdf("ResultadoVale.pdf", pages="10")
print(len(lista_tabelas))

for tabela in lista_tabelas:
    print(tabela)

lista_tabelas2 = tabula.read_pdf("ResultadoVale.pdf", pages="10")
print(len(lista_tabelas2))

for tabela in lista_tabelas2:
    tabela.columns = tabela.iloc[0]
    tabela[[0, 1]] = tabela["Variação percentual"].str.split(" ", expand=True)
    tabela = tabela[1:9]
    tabela = tabela.set_index("R$ milhões")
    tabela.columns = tabela.iloc[0]
    print(tabela)