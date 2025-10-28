import pandas as pd
import mysql.connector

# === CONFIGURAÇÕES ===
# Caminho do arquivo que contém a tabela (ex: CSV ou Excel)
CAMINHO_ARQUIVO = "Ola.xlsx"
NOME_TABELA_BANCO = "b2b_vivo_rede_ok"   # Nome da tabela no MySQL

# Credenciais do banco
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "vivob2b_bases_mirelle"
}

# === 1️⃣ Ler a tabela (arquivo local) ===
def ler_colunas_arquivo(caminho):
    if caminho.endswith(".csv"):
        df = pd.read_csv(caminho)
    elif caminho.endswith(".xlsx") or caminho.endswith(".xls"):
        df = pd.read_excel(caminho)
    else:
        raise ValueError("Formato de arquivo não suportado. Use CSV ou Excel.")
    return list(df.columns)

# === 2️⃣ Buscar colunas no banco de dados ===
def buscar_colunas_banco(nome_tabela):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    query = f"""
        SELECT COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = '{nome_tabela}'
          AND TABLE_SCHEMA = '{DB_CONFIG['database']}';
    """
    cursor.execute(query)
    colunas_banco = [linha[0] for linha in cursor.fetchall()]
    cursor.close()
    conn.close()
    return colunas_banco

# === 3️⃣ Comparar colunas ===
#def comparar_colunas(colunas_arquivo, colunas_banco):
   # faltando = [c for c in colunas_arquivo if c not in colunas_banco]
  #  extras = [c for c in colunas_banco if c not in colunas_arquivo]
    #return faltando, extras

# === 4️⃣ Execução ===
if __name__ == "__main__":
    colunas_arquivo = ler_colunas_arquivo(CAMINHO_ARQUIVO)
    colunas_banco = buscar_colunas_banco(NOME_TABELA_BANCO)

    ##faltando, extras = comparar_colunas(colunas_arquivo, colunas_banco)

    #print("📄 Colunas no arquivo:", colunas_arquivo)
    print("🏦 Colunas no banco:", colunas_banco)
    ##print("\n🚨 Colunas que FALTAM no banco:", faltando)
    #print("⚠️ Colunas que EXISTEM no banco mas NÃO estão no arquivo:", extras)
