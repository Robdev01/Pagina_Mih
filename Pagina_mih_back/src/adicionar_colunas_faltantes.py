import pymysql

# ⚙️ CONFIGURAÇÕES DO BANCO
config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "vivob2b_bases_mirelle"
}

# 🧱 NOME DA TABELA ONDE AS COLUNAS DEVEM SER ADICIONADAS
tabela = "b2b_vivo_ola_analitico"

# 📋 LISTA DE COLUNAS A ADICIONAR
colunas = [
    'Cadeia_Pendencias', 'Sub_Cadeia_Pendencias', 'Cadeia_Pendencias_Descricao',
    'Cadeia_Pendencias_Macro_SAE', 'DATA_SLA_RFS', 'SLA_RFS', 'SLA_RFS_Resumo',
    'DATA_SLA_CONTRATO', 'Data_RFB', 'SLA_RFB', 'SLA', 'SLA_Contrato', 'Sinergia',
    'Classificacao_Atual_Vivo_2', 'Sub_Status_Vivo_2', 'Ofensor_Tecnico_Vivo_2',
    'OS_SCD', 'OS_TBS', 'TBS_Task_Status_DD', 'TBS_Grupo_Usuario', 'TBS_Task_Ready',
    'Data_Emissão_OS', 'Data_Prevista_PTA', 'Motivo_PTA_Cod', 'Componente_HDSL',
    'Componente_Juntor', 'Portabilidade', 'Data_Abertura_WCD', 'Num_WCD', 'Data_ATP',
    'Num_ATP', 'Setor', 'Pilares', 'SubProcessos', 'SubWCD', 'escopo_PE', 'Status_OSP',
    'ID_Draft', 'DraftEncontrado', 'DataCriaçãoDraft', 'IdInternal', 'TarefaAtualDraft',
    'DiasNaFilaAtual', 'EntradaFilaAtualDraft', 'Status_Pedido_STAR', 'Tecnologia_Venda',
    'Num_LP', 'Tratativa_Monitora', 'Router_Cliente', 'Tipo_Router', 'Router_Atual',
    'Caixa_Unica', 'Combo', 'Revenda_VGR', 'ProjRouter', 'RedeNeutra', 'Vantive_Anterior',
    'OSX_Anterior', 'Operadora_Anterior', 'Tecnologia_Anterior', 'Router_Anterior',
    'Velocidade_Anterior', 'Expurgo', 'TM_PCC', 'TM_Pcc_Total', 'TM_Aprovisionamento',
    'TM_Planejamento', 'TM_Vistoria', 'TM_TI', 'TM_Rede', 'TM_Transporte',
    'TM_Engenharia', 'TM_MetroConfig', 'TM_LastMile', 'TM_Implantacao', 'TM_Ativacao',
    'Faixa_UltimoPCC', 'Vivo', 'BaixaSistemica', 'LiberacaoPCC', 'WCD_Tarefa_Rede',
    'MODELO_ATRIBUTOS', 'AT', 'Aging Atual', 'Aging Tec Total', 'Aging Resumo',
    'Aging Pcc Total', 'NovosPedidos', 'Regional Desc', 'Envolve Campo',
    'Bradesco_Prioritario', 'Capacitacao_ERB', 'TipoCapacitacaoSWA', 'Codigo',
    'AgendaTecMes', 'CidadeGPON', 'Agenda_Otimizada', 'BaseCongelada', 'Origem Pend.',
    'Flag_AltoValor', 'RESERVA', 'Designador_Acesso', 'Delta_Pos_Neg',
    'Data_Planejada_Status', 'Data_Agendamento_Cliente', 'Erb_Flash', 'DsnCorpStatus',
    'DsnCorp_Retrabalho', 'Dt_Liberado_Operadora', 'Passagem_PCC', 'Passagem_Viabilidade',
    'Passagem_Planejamento', 'Passagem_Vistoria', 'Passagem_TI', 'Passagem_Rede',
    'Passagem_Transporte', 'Passagem_Engenharia', 'Passagem_MetroConfig',
    'Passagem_LastMile', 'Passagem_Implantacao', 'Passagem_Ativacao',
    'Passagem_FaltaRFB', 'ResponsavelPE', 'DATA_PRAZO', 'Nome_Shopping',
    'CadeiaEstoqueDias', 'Projetos_LoteNum', 'Status_STAR_Principal', 'TRONCO_SIP',
    'AGING_BSC', 'BSC_SEGMENTO', 'BSC_DT_PRAZO_FIM', 'Raia Remoto'
]

# 🚀 CONEXÃO COM O BANCO
con = pymysql.connect(**config)
cursor = con.cursor()

# 🔎 VERIFICA QUAIS COLUNAS EXISTEM
cursor.execute(f"SHOW COLUMNS FROM {tabela}")
colunas_existentes = [col[0] for col in cursor.fetchall()]

# 🧮 ADICIONA AS FALTANTES
for coluna in colunas:
    if coluna not in colunas_existentes:
        try:
            sql = f"ALTER TABLE {tabela} ADD COLUMN `{coluna}` TEXT;"
            cursor.execute(sql)
            print(f"[OK] Coluna adicionada: {coluna}")
        except Exception as e:
            print(f"[ERRO] Falha ao adicionar '{coluna}': {e}")
    else:
        print(f"[=] Coluna já existe: {coluna}")

# 💾 CONFIRMA AS ALTERAÇÕES
con.commit()
cursor.close()
con.close()

print("\n✅ Todas as colunas faltantes foram verificadas/adicionadas com sucesso!")
