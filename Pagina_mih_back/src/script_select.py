import pandas as pd
import mysql.connector

# === CONFIGURAÇÕES DO BANCO ===
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "vivob2b_bases_mirelle"
}

# === SEU SELECT PERSONALIZADO ===
QUERY = """
SELECT *
FROM b2b_vivo_ola_analitico
WHERE id = '2449';
"""

# === NOME DO ARQUIVO DE SAÍDA ===
ARQUIVO_EXCEL = "resultado_pedidos.xlsx"

# === CONEXÃO E EXECUÇÃO ===
try:
    # Conecta ao banco
    conn = mysql.connector.connect(**DB_CONFIG)
    print("✅ Conectado ao banco de dados!")

    # Lê o resultado do SELECT direto para um DataFrame
    df = pd.read_sql(QUERY, conn)

    # Fecha a conexão
    conn.close()

    # Salva o DataFrame em Excel
    df.to_excel(ARQUIVO_EXCEL, index=False)
    print(f"📊 Arquivo Excel gerado com sucesso: {ARQUIVO_EXCEL}")

except mysql.connector.Error as e:
    print(f"❌ Erro de banco: {e}")
except Exception as e:
    print(f"⚠️ Erro geral: {e}")
