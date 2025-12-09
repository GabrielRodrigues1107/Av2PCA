import pandas as pd
import os

ARQUIVO = "alunos.csv"

# --------------------------------------------------------------
# Carregar CSV ou criar dados vazios
# --------------------------------------------------------------
def carregar_dados():
    if os.path.exists(ARQUIVO):
        return pd.read_csv(ARQUIVO)
    else:
        return pd.DataFrame(columns=["Matricula", "Nome", "Rua", "Número", "Bairro",
                                     "Cidade", "UF", "Telefone", "Email"])

# --------------------------------------------------------------
# Salvar CSV
# --------------------------------------------------------------
def salvar_dados(df):
    df.to_csv(ARQUIVO, index=False)
    print("\n📁 Dados salvos com sucesso!\n")

# --------------------------------------------------------------
# Gerar nova matrícula
# --------------------------------------------------------------
def gerar_matricula(df):
    if df.empty:
        return 1
    return df["Matricula"].max() + 1

# --------------------------------------------------------------
# Inserir aluno
# --------------------------------------------------------------
def inserir(df):
    print("\n=== INSERIR NOVO ALUNO ===")

    matricula = gerar_matricula(df)
    print(f"Matrícula gerada: {matricula}")

    aluno = {
        "Matricula": matricula,
        "Nome": input("Nome: "),
        "Rua": input("Rua: "),
        "Número": input("Número: "),
        "Bairro": input("Bairro: "),
        "Cidade": input("Cidade: "),
        "UF": input("UF: "),
        "Telefone": input("Telefone: "),
        "Email": input("Email: ")
    }

    df.loc[len(df)] = aluno
    salvar_dados(df)
    print("Aluno inserido com sucesso!\n")

# --------------------------------------------------------------
# Pesquisar aluno
# --------------------------------------------------------------
def pesquisar(df):
    print("\n=== PESQUISAR ALUNO ===")
    termo = input("Digite nome ou matrícula: ").strip()

    if termo.isdigit():
        resultado = df[df["Matricula"] == int(termo)]
    else:
        resultado = df[df["Nome"].str.lower() == termo.lower()]

    if resultado.empty:
        print("\n❌ Nenhum aluno encontrado.\n")
    else:
        print("\nAluno encontrado:\n")
        print(resultado)

# --------------------------------------------------------------
# Editar aluno
# --------------------------------------------------------------
def editar(df):
    print("\n=== EDITAR ALUNO ===")
    termo = input("Digite a matrícula: ")

    if not termo.isdigit():
        print("❌ Digite apenas números.")
        return df

    termo = int(termo)
    indice = df[df["Matricula"] == termo].index

    if len(indice) == 0:
        print("❌ Matrícula não encontrada.")
        return df

    idx = indice[0]

    print("\nDados atuais:")
    print(df.loc[idx])
    print("\nDeixe em branco para manter o valor atual.\n")

    for col in df.columns:
        if col == "Matricula":
            continue
        novo = input(f"{col} ({df.loc[idx, col]}): ").strip()
        if novo != "":
            df.loc[idx, col] = novo

    salvar_dados(df)
    print("Aluno atualizado!\n")
    return df

# --------------------------------------------------------------
# Remover aluno (corrigido!)
# --------------------------------------------------------------
def remover(df):
    print("\n=== REMOVER ALUNO ===")
    matricula = input("Digite a matrícula: ")

    if not matricula.isdigit():
        print("❌ Digite apenas números.")
        return df

    # Verifica se existe
    if matricula in df["Matricula"].astype(str).values:
        df = df[df["Matricula"].astype(str) != matricula]
        salvar_dados(df)
        print("Aluno removido com sucesso!\n")
    else:
        print("❌ Matrícula não encontrada.\n")

    return df

# --------------------------------------------------------------
# Menu principal
# --------------------------------------------------------------
def menu():
    df = carregar_dados()

    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1 - INSERIR")
        print("2 - PESQUISAR")
        print("3 - EDITAR")
        print("4 - REMOVER")
        print("5 - SAIR")

        opc = input("Escolha: ")

        if opc == "1":
            inserir(df)
        elif opc == "2":
            pesquisar(df)
        elif opc == "3":
            df = editar(df)
        elif opc == "4":
            df = remover(df)
        elif opc == "5":
            print("Encerrando...")
            break
        else:
            print("❌ Opção inválida!")

# --------------------------------------------------------------
# Executar
# --------------------------------------------------------------
menu()
