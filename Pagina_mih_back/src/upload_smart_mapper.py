import pymysql
import pandas as pd
import unidecode
import json

# ⚙️ CONFIGURAÇÕES DO BANCO
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "vivob2b_bases_mirelle"
}

TABELA = "b2b_vivo_ola_analitico"
ARQUIVO_EXCEL = "Ola.xlsx"

# 🔤 Função para normalizar chaves (remove acentos e símbolos)
def normalize_key(key: str) -> str:
    key = unidecode.unidecode(key.strip())
    key = key.replace(" ", "_").replace(".", "").replace("(", "").replace(")", "")
    return key.upper()

# 🧱 1️⃣ Lê colunas do banco
def get_db_columns():
    con = pymysql.connect(**DB_CONFIG)
    cur = con.cursor()
    cur.execute(f"SHOW COLUMNS FROM {TABELA}")
    cols = [col[0].upper() for col in cur.fetchall()]
    cur.close()
    con.close()
    return cols

# 📊 2️⃣ Lê dados da planilha
def read_excel(path):
    df = pd.read_excel(path, dtype=str).fillna("")
    df.columns = [normalize_key(c) for c in df.columns]
    return df.to_dict(orient="records")

# 🔗 3️⃣ Cria o mapeamento automático
def map_columns(row, valid_columns):
    mapped = {}
    for k, v in row.items():
        if k in valid_columns:
            mapped[k] = v
        else:
            # tenta encontrar por similaridade simples
            match = next((col for col in valid_columns if col.replace("_", "") == k.replace("_", "")), None)
            if match:
                mapped[match] = v
    # adiciona colunas ausentes como vazio
    for c in valid_columns:
        if c not in mapped:
            mapped[c] = ""
    return mapped

# 🚀 4️⃣ Execução principal
def process_upload():
    db_cols = get_db_columns()
    dados = read_excel(ARQUIVO_EXCEL)
    print(f"🧩 Colunas no banco: {len(db_cols)} | Colunas na planilha: {len(dados[0])}")

    dados_mapeados = [map_columns(linha, db_cols) for linha in dados]

    # salva resultado para envio ao backend
    with open("dados_mapeados.json", "w", encoding="utf-8") as f:
        json.dump(dados_mapeados, f, ensure_ascii=False, indent=2)

    print(f"✅ Mapeamento concluído! Gerado arquivo 'dados_mapeados.json' pronto para envio.")

if __name__ == "__main__":
    process_upload()
