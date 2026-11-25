
import csv
import os

# troque para o caminho do seu arquivo
arquivo = r"C:\exemplo\raw\Dados_Estatisticos_ANAC.csv"

print("Tamanho:")
print(round(os.path.getsize(arquivo) / (1024 ** 2), 2), "MB")

with open(
    arquivo,
    "r",
    encoding="utf-8-sig",
    newline=""
) as f:

    leitor = csv.reader(f, delimiter=";")

    # Ignorar a linha de atualização
    next(leitor)

    # Ler a linha com os nomes das colunas
    colunas = next(leitor)

print("\nQuantidade de colunas:", len(colunas))

print("\nColunas encontradas:")
for coluna in colunas:
    print(coluna)