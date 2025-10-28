import pymysql
import os

def get_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT")),
        cursorclass=pymysql.cursors.DictCursor
    )



def models_insert_pedidos_ola_lote(pedidos):
    """
    Insere múltiplos registros na tabela b2b_vivo_ola_analitico em lote.
    Ignora colunas inexistentes no banco e realiza inserção segura.
    """
    # 🔹 Colunas realmente existentes no banco (com base no seu dump)
    colunas_banco = [
        'Pedido', 'ID_Vantive', 'ID_Associado', 'ID_Cliente', 'Cliente', 'CNPJ', 'UF', 'Cidade', 'CEP', 'Numero',
        'Regional', 'RegionalRampa', 'Esteira', 'Esteira_Regionalizada', 'SegResumo', 'Produto', 'Servico',
        'Tipo_Venda_Detalhes', 'Familia', 'Oportunidade', 'Data_Entrada', 'Data_Assinatura_Contrato',
        'Classificacao_Resumo_Atual', 'Carteira', 'Dias_CarteiraAtual', 'Dias_UltimoPCC', 'Ativ_Central',
        'DataTecnica', 'Data_RFS', 'DATA_SLA_RFS', 'SLA_RFS', 'SLA_RFS_Resumo', 'DATA_SLA_CONTRATO', 'Data_RFB',
        'SLA_RFB', 'SLA', 'SLA_Contrato', 'Data_Planejada', 'Data_Expectativa_Cliente', 'DataRede',
        'Data_Prevista_OSP', 'Data_Inicio_Rede', 'Data_Fim_Rede', 'Aging_Rede', 'Tecnologia_Report', 'Velocidade',
        'Nome_Operadora', 'Quebra_Esteira', 'Tipo_Alta_Macro', 'Delta_REC_LIQ', 'Delta_REC_TOTAL', 'Escritorio',
        'Status_SGOS', 'Gestor_Atual', 'Parceiro', 'Classificacao_rede', 'SLA_TECNICA', 'LOCALIDADE',
        'Data_Atualizacao', 'Natureza_Desc', 'Projetos', 'Projetos_Lote', 'ConsolidadoEstoque',
        'ConsolidadoClassificacao', 'ConfigStatus', 'Config_Retrabalho', 'Endereco_Completo',
        'Descricao_TarefaSWA', 'ATIVDESCR', 'Router_Desc', 'Router_Desc_Anterior', 'ISIS_MOTIVO_PENDENCIA',
        'ISIS_SUB_MOTIVO_PENDENCIA', 'Origem_Pend', 'Status_Voz', 'Produto_SIP', 'Marca_PABX', 'Alta_Planta',
        'Canais', 'TM_Tramitacao', 'TM_Tec_Total', 'TM_Total', 'Faixa_Pcc', 'Faixa_Tec', 'Faixa_Total',
        'Projeto_Especial', 'Flag_Grandes_Projetos', 'PRODUTO_STAR', 'Segmento_V3', 'Label_ERB', 'Bucle',
        'Bucle_Contratada', 'GRUPO_BSC', 'PRAZO_BSC', 'Efika_GIS', 'Raia_Remoto', 'LP_13', 'Cadeia_Pendencias',
        'Sub_Cadeia_Pendencias', 'Cadeia_Pendencias_Descricao', 'Cadeia_Pendencias_Macro_SAE', 'Sinergia',
        'Classificacao_Atual_Vivo_2', 'Sub_Status_Vivo_2', 'Ofensor_Tecnico_Vivo_2', 'OS_SCD', 'OS_TBS',
        'TBS_Task_Status_DD', 'TBS_Grupo_Usuario', 'TBS_Task_Ready', 'Data_Emissão_OS', 'OSX', 'Data_Prevista_PTA',
        'Motivo_PTA_Cod', 'Componente_HDSL', 'Componente_Juntor', 'Portabilidade', 'Data_Abertura_WCD', 'Num_WCD',
        'Data_ATP', 'Num_ATP', 'Setor', 'Pilares', 'SubProcessos', 'SubWCD', 'escopo_PE', 'Status_OSP', 'ID_Draft',
        'DraftEncontrado', 'DataCriaçãoDraft', 'IdInternal', 'TarefaAtualDraft', 'DiasNaFilaAtual',
        'EntradaFilaAtualDraft', 'Status_Pedido_STAR', 'Tecnologia_Venda', 'Num_LP', 'Tratativa_Monitora',
        'Router_Cliente', 'Tipo_Router', 'Router_Atual', 'Caixa_Unica', 'Combo', 'Revenda_VGR', 'ProjRouter',
        'RedeNeutra', 'Vantive_Anterior', 'OSX_Anterior', 'Operadora_Anterior', 'Tecnologia_Anterior',
        'Router_Anterior', 'Velocidade_Anterior', 'Expurgo', 'TM_PCC', 'TM_Pcc_Total', 'TM_Aprovisionamento',
        'TM_Planejamento', 'TM_Vistoria', 'TM_TI', 'TM_Rede', 'TM_Transporte', 'TM_Engenharia', 'TM_MetroConfig',
        'TM_LastMile', 'TM_Implantacao', 'TM_Ativacao', 'Faixa_UltimoPCC', 'Vivo', 'BaixaSistemica',
        'LiberacaoPCC', 'WCD_Tarefa_Rede', 'MODELO_ATRIBUTOS', 'AT', 'Aging Atual', 'Aging Tec Total',
        'Aging Resumo', 'Aging Pcc Total', 'NovosPedidos', 'Regional Desc', 'Envolve Campo', 'Bradesco_Prioritario',
        'Capacitacao_ERB', 'TipoCapacitacaoSWA', 'Codigo', 'AgendaTecMes', 'CidadeGPON', 'Agenda_Otimizada',
        'BaseCongelada', 'Flag_AltoValor', 'RESERVA', 'Designador_Acesso', 'Delta_Pos_Neg',
        'Data_Planejada_Status', 'Data_Agendamento_Cliente', 'Erb_Flash', 'DsnCorpStatus', 'DsnCorp_Retrabalho',
        'Dt_Liberado_Operadora', 'Passagem_PCC', 'Passagem_Viabilidade', 'Passagem_Planejamento',
        'Passagem_Vistoria', 'Passagem_TI', 'Passagem_Rede', 'Passagem_Transporte', 'Passagem_Engenharia',
        'Passagem_MetroConfig', 'Passagem_LastMile', 'Passagem_Implantacao', 'Passagem_Ativacao', 'Passagem_FaltaRFB',
        'ResponsavelPE', 'DATA_PRAZO', 'Nome_Shopping', 'CadeiaEstoqueDias', 'Projetos_LoteNum',
        'Status_STAR_Principal', 'TRONCO_SIP', 'AGING_BSC', 'BSC_SEGMENTO', 'BSC_DT_PRAZO_FIM'
    ]

    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # 🔹 Filtra colunas existentes com base no dicionário de entrada
            colunas_existentes = [c for c in colunas_banco if any(c in p for p in pedidos)]
            placeholders = ', '.join([f"%({c})s" for c in colunas_existentes])
            colunas_sql = ', '.join(colunas_existentes)

            sql = f"""
                INSERT INTO b2b_vivo_ola_analitico ({colunas_sql})
                VALUES ({placeholders})
            """

            cursor.executemany(sql, pedidos)
        conn.commit()
        print(f"✅ Inserção concluída com sucesso ({len(pedidos)} registros).")
        return True
    except Exception as e:
        print("❌ Erro ao inserir pedidos OLA:", e)
        conn.rollback()
        return False
    finally:
        conn.close()

def models_insert_pedido_estoque_melhoria(pedidos):

    colunas= [
        'Produto', 'Pedido', 'ID_Vantive', 'Cliente', 'Status_Vantive', 'Data_Entrada',
        'Data_RFS', 'OSX', 'Natureza_Desc', 'Status_SGOS', 'Codigo', 'Gestor_Atual',
        'Data_Prevista_PTA', 'Tecnologia', 'Endereco', 'Cidade', 'AT', 'Escritorio',
        'Cluster', 'SPE', 'Num_ATP', 'Status_SPE', 'WCD_Grupo_Pendencia', 'WCD_Sub_Grupo_Pendencia',
        'WCD_Grupo_Pendencia_Detalhe', 'Velocidade', 'ID_Anterior', 'ST_VTV_Anterior', 'Data_RFS_Anterior',
        'LP_Anterior_15', 'LP_Anterior_13', 'Tronco_SIP', 'Tecnologia_Atual', 'Status', 'Substatus',
        'Data_Agenda', 'Tipo', 'Tipo_Alteracao']

    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # 🔹 Filtra colunas existentes com base no dicionário de entrada
            colunas_existentes = [c for c in colunas if any(c in p for p in pedidos)]
            placeholders = ', '.join([f"%({c})s" for c in colunas_existentes])
            colunas_sql = ', '.join(colunas_existentes)

            sql = f"""
                   INSERT INTO b2b_vivo_estoque_melhoria ({colunas_sql})
                   VALUES ({placeholders})
               """

            cursor.executemany(sql, pedidos)
        conn.commit()
        print(f"✅ Inserção concluída com sucesso ({len(pedidos)} registros).")
        return True
    except Exception as e:
        print("❌ Erro ao inserir pedidos OLA:", e)
        conn.rollback()
        return False
    finally:
        conn.close()

def models_insert_pedido_b2b_pendentes(pedidos):

    colunas = [
        'COD', 'NUM_ATP', 'SLA', 'Equip_Grande_Porte', 'PRIORIDADE', 'Tecnologia', 'STATUS', 'Area', 'DATA_EMISSAO',
        'WCD', 'Delta_REC_LIQ', 'Situacao_Geral', 'Data_Vistoria', 'Lancamento_Interno', 'Data_Agenda_Cabo', 'Gestor_Rubia',
        'SEGMENTO', 'CLIENTE', 'ENDERECO', 'AREA_AT', 'CONTRATADA', 'CONTRATADA2', 'AGING', 'ID_OSP', 'STATUS_OSP', 'D_1',
        'DATA', 'Total_Obra', 'Total_Metros', 'Custo_Por_Km', 'Observacoes', 'ID_Vantive', 'DATA_PROJETO', 'AGING_PROJ',
        'OBRA_APROVADA', 'AGING_EMISSAO', 'ALTO_VALOR', 'VIP', 'Status_Proj_Icomon', 'GRUPO_BSC', 'ConsolidadoEstoque', 'SegResumo'
    ]
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # 🔹 Filtra colunas existentes com base no dicionário de entrada
            colunas_existentes = [c for c in colunas if any(c in p for p in pedidos)]
            placeholders = ', '.join([f"%({c})s" for c in colunas_existentes])
            colunas_sql = ', '.join(colunas_existentes)

            sql = f"""
                      INSERT INTO b2b_vivo_pendentes ({colunas_sql})
                      VALUES ({placeholders})
                  """

            cursor.executemany(sql, pedidos)
        conn.commit()
        print(f"✅ Inserção concluída com sucesso ({len(pedidos)} registros).")
        return True
    except Exception as e:
        print("❌ Erro ao inserir pedidos OLA:", e)
        conn.rollback()
        return False
    finally:
        conn.close()

def models_insert_pedido_b2b_rede_ok(pedidos):
    colunas = [
        'COD', 'ETP', 'PRIORIDADE', 'TIPO', 'CLIENTE', 'AREA_AT', 'CONTRATO', 'Prazo_Rede', 'ID_OSP', 'STATUS_OSP',
        'INTERNO_REDE', 'ID_VANTIVE'
    ]
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # 🔹 Filtra colunas existentes com base no dicionário de entrada
            colunas_existentes = [c for c in colunas if any(c in p for p in pedidos)]
            placeholders = ', '.join([f"%({c})s" for c in colunas_existentes])
            colunas_sql = ', '.join(colunas_existentes)

            sql = f"""
                         INSERT INTO b2b_vivo_rede_ok ({colunas_sql})
                         VALUES ({placeholders})
                     """

            cursor.executemany(sql, pedidos)
        conn.commit()
        print(f"✅ Inserção concluída com sucesso ({len(pedidos)} registros).")
        return True
    except Exception as e:
        print("❌ Erro ao inserir pedidos OLA:", e)
        conn.rollback()
        return False
    finally:
        conn.close()