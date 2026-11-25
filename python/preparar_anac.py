
import duckdb
from pathlib import Path

# Altere para o caminho do seu arquivo
arquivo_csv = r"C:\exemplo\raw\Dados_Estatisticos_ANAC.csv"

# Arquivo reduzido que será criado
arquivo_saida = r"C:\exemplo\processed\anac_2019_2024.parquet"

Path(arquivo_saida).parent.mkdir(
    parents=True,
    exist_ok=True
)

con = duckdb.connect()

print("Iniciando processamento...")

consulta = f"""
COPY (
    SELECT *
    FROM read_csv_auto(
        '{arquivo_csv}',
        delim=';',
        header=true,
        sample_size=10000
    )
    WHERE TRY_CAST(ANO AS INTEGER)
          BETWEEN 2019 AND 2024
      AND NATUREZA = 'DOMÉSTICA'
      AND GRUPO_DE_VOO = 'REGULAR'
      AND EMPRESA_NACIONALIDADE = 'BRASILEIRA'
)
TO '{arquivo_saida}'
(FORMAT PARQUET, COMPRESSION ZSTD);
"""

con.execute(consulta)

print("Processamento concluído!")
print("Arquivo criado:", arquivo_saida)

con.close()
