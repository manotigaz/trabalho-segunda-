import pandas as pd
import plotly.express as px

# Carregar Dataset
df = pd.read_csv("iphone_sales_dataset.csv")

print("\nColunas encontradas no dataset:")
print(df.columns)

# Ajuste automático dos nomes das colunas
df.columns = [col.lower().strip() for col in df.columns]

# =========================
# OPÇÃO 1 - iPhones mais vendidos
# =========================

def iphones_mais_vendidos():
    coluna_modelo = "iphone_model"
    coluna_vendas = "quantity"

    top = (
        df.groupby(coluna_modelo, as_index=False)[coluna_vendas]
        .sum()
        .sort_values(by=coluna_vendas, ascending=False)
        .head(10)
    )

    fig = px.bar(
        top,
        x=coluna_modelo,
        y=coluna_vendas,
        color=coluna_vendas,
        title="Top 10 iPhones Mais Vendidos do Mundo"
    )

    fig.show()


# =========================
# OPÇÃO 2 - Comparar iPhones
# =========================

def comparar_iphones():

    coluna_modelo = "iphone_model"
    coluna_vendas = "quantity"

    iphone1 = input("Digite o primeiro iPhone: ")
    iphone2 = input("Digite o segundo iPhone: ")

    dados1 = df[df[coluna_modelo].str.lower() == iphone1.lower()]
    dados2 = df[df[coluna_modelo].str.lower() == iphone2.lower()]

    if dados1.empty or dados2.empty:
        print("\nUm dos modelos não foi encontrado. Verifique o nome e tente novamente.")
        return

    comparacao = pd.DataFrame({
        "iPhone": [iphone1, iphone2],
        "Vendas": [
            dados1[coluna_vendas].sum(),
            dados2[coluna_vendas].sum()
        ]
    })

    fig = px.bar(
        comparacao,
        x="iPhone",
        y="Vendas",
        color="iPhone",
        title="Comparação de Vendas"
    )

    fig.show()


# =========================
# OPÇÃO 3 - Gráfico Pizza
# =========================

def grafico_pizza():

    coluna_modelo = "iphone_model"
    coluna_vendas = "quantity"

    top = (
        df.groupby(coluna_modelo, as_index=False)[coluna_vendas]
        .sum()
        .sort_values(by=coluna_vendas, ascending=False)
        .head(5)
    )

    fig = px.pie(
        top,
        names=coluna_modelo,
        values=coluna_vendas,
        title="Participação dos iPhones Mais Vendidos"
    )

    fig.show()


# =========================
# OPÇÃO 4 - Tabela Completa
# =========================

def mostrar_tabela():

    print("\n===== DATASET =====\n")
    print(df.head(20))


# =========================
# MENU
# =========================

while True:

    print("\n========== MENU ==========")
    print("1 - Top 10 iPhones mais vendidos")
    print("2 - Comparar iPhones")
    print("3 - Gráfico pizza")
    print("4 - Mostrar tabela")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        iphones_mais_vendidos()

    elif opcao == "2":
        comparar_iphones()

    elif opcao == "3":
        grafico_pizza()

    elif opcao == "4":
        mostrar_tabela()

    elif opcao == "0":
        print("\nPrograma encerrado.")
        break

    else:
        print("\nOpção inválida!")
