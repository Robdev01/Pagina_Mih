from flask import jsonify

from src.pedidos.models import (models_insert_pedidos_ola_lote,
models_insert_pedido_estoque_melhoria,
models_insert_pedido_b2b_pendentes,
models_insert_pedido_b2b_rede_ok


)

import unidecode

def normalize_key(key: str) -> str:
    """
    Normaliza as chaves recebidas do frontend (remove acentos, espaços, símbolos e deixa MAIÚSCULO).
    Isso garante compatibilidade com o Excel e o dicionário Python.
    """
    key = unidecode.unidecode(key.strip())
    key = key.replace(" ", "_").replace(".", "").replace("(", "").replace(")", "")
    return key.upper()

def controller_create_pedidos_ola(data):
    """
    Controla o cadastro em lote de pedidos OLA.
    """
    if not isinstance(data, list):
        return {"message": "O corpo da requisição deve ser uma lista de objetos JSON"}, 400

    pedidos_preparados = []
    for row in data:
        # 🔧 Normaliza todas as chaves da linha
        row_norm = {normalize_key(k): v for k, v in row.items()}

        # Agora os .get() funcionam, pois as chaves batem com o banco
        pedido = {
            "Pedido": row_norm.get("PEDIDO"),
            "ID_Vantive": row_norm.get("ID_VANTIVE"),
            "ID_Associado": row_norm.get("ID_ASSOCIADO"),
            "ID_Cliente": row_norm.get("ID_CLIENTE"),
            "Cliente": row_norm.get("CLIENTE"),
            "CNPJ": row_norm.get("CNPJ"),
            "UF": row_norm.get("UF"),
            "Cidade": row_norm.get("CIDADE"),
            "CEP": row_norm.get("CEP"),
            "Numero": row_norm.get("NUMERO"),
            "Regional": row_norm.get("REGIONAL"),
            "RegionalRampa": row_norm.get("REGIONALRAMPA"),
            "Esteira": row_norm.get("ESTEIRA"),
            "Esteira_Regionalizada": row_norm.get("ESTEIRA_REGIONALIZADA"),
            "SegResumo": row_norm.get("SEGRESUMO"),
            "Produto": row_norm.get("PRODUTO"),
            "Servico": row_norm.get("SERVICO"),
            "Tipo_Venda_Detalhes": row_norm.get("TIPO_VENDA_DETALHES"),
            "Familia": row_norm.get("FAMILIA"),
            "Oportunidade": row_norm.get("OPORTUNIDADE"),
            "Data_Entrada": row_norm.get("DATA_ENTRADA"),
            "Data_Assinatura_Contrato": row_norm.get("DATA_ASSINATURA_CONTRATO"),
            "Classificacao_Resumo_Atual": row_norm.get("CLASSIFICACAO_RESUMO_ATUAL"),
            "Carteira": row_norm.get("CARTEIRA"),
            "Dias_CarteiraAtual": row_norm.get("DIAS_CARTEIRAATUAL"),
            "Dias_UltimoPCC": row_norm.get("DIAS_ULTIMOPCC"),
            "Ativ_Central": row_norm.get("ATIV_CENTRAL"),
            "DataTecnica": row_norm.get("DATATECNICA"),
            "Data_RFS": row_norm.get("DATA_RFS"),
            "DATA_SLA_RFS": row_norm.get("DATA_SLA_RFS"),
            "SLA_RFS": row_norm.get("SLA_RFS"),
            "SLA_RFS_Resumo": row_norm.get("SLA_RFS_RESUMO"),
            "DATA_SLA_CONTRATO": row_norm.get("DATA_SLA_CONTRATO"),
            "Data_RFB": row_norm.get("DATA_RFB"),
            "SLA_RFB": row_norm.get("SLA_RFB"),
            "SLA": row_norm.get("SLA"),
            "SLA_Contrato": row_norm.get("SLA_CONTRATO"),
            "Data_Planejada": row_norm.get("DATA_PLANEJADA"),
            "Data_Expectativa_Cliente": row_norm.get("DATA_EXPECTATIVA_CLIENTE"),
            "DataRede": row_norm.get("DATAREDE"),
            "Data_Prevista_OSP": row_norm.get("DATA_PREVISTA_OSP"),
            "Data_Inicio_Rede": row_norm.get("DATA_INICIO_REDE"),
            "Data_Fim_Rede": row_norm.get("DATA_FIM_REDE"),
            "Aging_Rede": row_norm.get("AGING_REDE"),
            "Tecnologia_Report": row_norm.get("TECNOLOGIA_REPORT"),
            "Velocidade": row_norm.get("VELOCIDADE"),
            "Nome_Operadora": row_norm.get("NOME_OPERADORA"),
            "Quebra_Esteira": row_norm.get("QUEBRA_ESTEIRA"),
            "Tipo_Alta_Macro": row_norm.get("TIPO_ALTA_MACRO"),
            "Delta_REC_LIQ": row_norm.get("DELTA_REC_LIQ"),
            "Delta_REC_TOTAL": row_norm.get("DELTA_REC_TOTAL"),
            "Escritorio": row_norm.get("ESCRITORIO"),
            "Status_SGOS": row_norm.get("STATUS_SGOS"),
            "Gestor_Atual": row_norm.get("GESTOR_ATUAL"),
            "Parceiro": row_norm.get("PARCEIRO"),
            "Classificacao_rede": row_norm.get("CLASSIFICACAO_REDE"),
            "SLA_TECNICA": row_norm.get("SLA_TECNICA"),
            "LOCALIDADE": row_norm.get("LOCALIDADE"),
            "Data_Atualizacao": row_norm.get("DATA_ATUALIZACAO"),
            "Natureza_Desc": row_norm.get("NATUREZA_DESC"),
            "Projetos": row_norm.get("PROJETOS"),
            "Projetos_Lote": row_norm.get("PROJETOS_LOTE"),
            "ConsolidadoEstoque": row_norm.get("CONSOLIDADOESTOQUE"),
            "ConsolidadoClassificacao": row_norm.get("CONSOLIDADOCLASSIFICACAO"),
            "ConfigStatus": row_norm.get("CONFIGSTATUS"),
            "Config_Retrabalho": row_norm.get("CONFIG_RETRABALHO"),
            "Endereco_Completo": row_norm.get("ENDERECO_COMPLETO"),
            "Descricao_TarefaSWA": row_norm.get("DESCRICAO_TAREFASWA"),
            "ATIVDESCR": row_norm.get("ATIVDESCR"),
            "Router_Desc": row_norm.get("ROUTER_DESC"),
            "Router_Desc_Anterior": row_norm.get("ROUTER_DESC_ANTERIOR"),
            "ISIS_MOTIVO_PENDENCIA": row_norm.get("ISIS_MOTIVO_PENDENCIA"),
            "ISIS_SUB_MOTIVO_PENDENCIA": row_norm.get("ISIS_SUB_MOTIVO_PENDENCIA"),
            "Origem_Pend": row_norm.get("ORIGEM_PEND"),
            "Status_Voz": row_norm.get("STATUS_VOZ"),
            "Produto_SIP": row_norm.get("PRODUTO_SIP"),
            "Marca_PABX": row_norm.get("MARCA_PABX"),
            "Alta_Planta": row_norm.get("ALTA_PLANTA"),
            "Canais": row_norm.get("CANAIS"),
            "TM_Tramitacao": row_norm.get("TM_TRAMITACAO"),
            "TM_Tec_Total": row_norm.get("TM_TEC_TOTAL"),
            "TM_Total": row_norm.get("TM_TOTAL"),
            "Faixa_Pcc": row_norm.get("FAIXA_PCC"),
            "Faixa_Tec": row_norm.get("FAIXA_TEC"),
            "Faixa_Total": row_norm.get("FAIXA_TOTAL"),
            "Projeto_Especial": row_norm.get("PROJETO_ESPECIAL"),
            "Flag_Grandes_Projetos": row_norm.get("FLAG_GRANDES_PROJETOS"),
            "PRODUTO_STAR": row_norm.get("PRODUTO_STAR"),
            "Segmento_V3": row_norm.get("SEGMENTO_V3"),
            "Label_ERB": row_norm.get("LABEL_ERB"),
            "Bucle": row_norm.get("BUCLE"),
            "Bucle_Contratada": row_norm.get("BUCLE_CONTRATADA"),
            "GRUPO_BSC": row_norm.get("GRUPO_BSC"),
            "AGING_BSC": row_norm.get("AGING_BSC"),
            "PRAZO_BSC": row_norm.get("PRAZO_BSC"),
            "BSC_SEGMENTO": row_norm.get("BSC_SEGMENTO"),
            "BSC_DT_PRAZO_FIM": row_norm.get("BSC_DT_PRAZO_FIM"),
            "Efika_GIS": row_norm.get("EFIKA_GIS"),
            "Raia_Remoto": row_norm.get("RAIA_REMOTO"),
            "LP_13": row_norm.get("LP_13"),
            "OSX": row_norm.get("OSX"),
        }

        pedidos_preparados.append(pedido)

    sucesso = models_insert_pedidos_ola_lote(pedidos_preparados)

    if sucesso:
        return {"message": f"{len(pedidos_preparados)} registros inseridos com sucesso!"}, 201
    else:
        return {"message": "Erro ao inserir registros"}, 500


def controller_create_pedido_estoque_melhoria(data):
    """
    Recebe lista de pedidos em JSON, normaliza as chaves e envia para o model de inserção.
    """
    if not isinstance(data, list):
        return {"message": "O corpo da requisição deve ser uma lista de objetos JSON"}, 400

    pedidos_preparados = []

    for row in data:
        # 🔧 Normaliza as chaves (por exemplo: "DATA ENTRADA" → "DATA_ENTRADA")
        row_norm = {normalize_key(k): v for k, v in row.items()}

        pedido = {
            "Produto": row_norm.get("PRODUTO"),
            "Pedido": row_norm.get("PEDIDO"),
            "ID_Vantive": row_norm.get("ID_VANTIVE"),
            "Cliente": row_norm.get("CLIENTE"),
            "Status_Vantive": row_norm.get("STATUS_VANTIVE"),
            "Data_Entrada": row_norm.get("DATA_ENTRADA"),
            "Data_RFS": row_norm.get("DATA_RFS"),
            "OSX": row_norm.get("OSX"),
            "Natureza_Desc": row_norm.get("NATUREZA_DESC"),
            "Status_SGOS": row_norm.get("STATUS_SGOS"),
            "Codigo": row_norm.get("CODIGO"),
            "Gestor_Atual": row_norm.get("GESTOR_ATUAL"),
            "Data_Prevista_PTA": row_norm.get("DATA_PREVISTA_PTA"),
            "Tecnologia": row_norm.get("TECNOLOGIA"),
            "Endereco": row_norm.get("ENDERECO"),
            "Cidade": row_norm.get("CIDADE"),
            "AT": row_norm.get("AT"),
            "Escritorio": row_norm.get("ESCRITORIO"),
            "Cluster": row_norm.get("CLUSTER"),
            "SPE": row_norm.get("SPE"),
            "Num_ATP": row_norm.get("NUM_ATP"),
            "Status_SPE": row_norm.get("STATUS_SPE"),
            "WCD_Grupo_Pendencia": row_norm.get("WCD_GRUPO_PENDENCIA"),
            "WCD_Sub_Grupo_Pendencia": row_norm.get("WCD_SUB_GRUPO_PENDENCIA"),
            "WCD_Grupo_Pendencia_Detalhe": row_norm.get("WCD_GRUPO_PENDENCIA_DETALHE"),
            "Velocidade": row_norm.get("VELOCIDADE"),
            "ID_Anterior": row_norm.get("ID_ANTERIOR"),
            "ST_VTV_Anterior": row_norm.get("ST_VTV_ANTERIOR"),
            "Data_RFS_Anterior": row_norm.get("DATA_RFS_ANTERIOR"),
            "LP_Anterior_15": row_norm.get("LP_ANTERIOR_15"),
            "LP_Anterior_13": row_norm.get("LP_ANTERIOR_13"),
            "Tronco_SIP": row_norm.get("TRONCO_SIP"),
            "Tecnologia_Atual": row_norm.get("TECNOLOGIA_ATUAL"),
            "Status": row_norm.get("STATUS"),
            "Substatus": row_norm.get("SUBSTATUS"),
            "Data_Agenda": row_norm.get("DATA_AGENDA"),
            "Tipo": row_norm.get("TIPO"),
            "Tipo_Alteracao": row_norm.get("TIPO_ALTERACAO"),
        }

        pedidos_preparados.append(pedido)

    # 🔄 Tenta inserir no banco via model
    sucesso = models_insert_pedido_estoque_melhoria(pedidos_preparados)

    if sucesso:
        return {"message": f"{len(pedidos_preparados)} pedidos inseridos com sucesso"}, 201
    else:
        return {"message": "Erro ao cadastrar pedidos"}, 500

def controller_create_pedido_b2b_pendentes(data):
    """
    Recebe lista de pedidos em JSON, normaliza as chaves e envia para o model de inserção.
    """
    if not isinstance(data, list):
        return {"message": "O corpo da requisição deve ser uma lista de objetos JSON"}, 400

    pedidos_preparados = []

    for row in data:
        # 🔧 Normaliza as chaves (por exemplo: "DATA EMISSAO" → "DATA_EMISSAO")
        row_norm = {normalize_key(k): v for k, v in row.items()}

        pedido = {
            "COD": row_norm.get("COD"),
            "NUM_ATP": row_norm.get("NUM_ATP"),
            "SLA": row_norm.get("SLA"),
            "Equip_Grande_Porte": row_norm.get("EQUIP_GRANDE_PORTE"),
            "PRIORIDADE": row_norm.get("PRIORIDADE"),
            "Tecnologia": row_norm.get("TECNOLOGIA"),
            "STATUS": row_norm.get("STATUS"),
            "Area": row_norm.get("AREA"),
            "DATA_EMISSAO": row_norm.get("DATA_EMISSAO"),
            "WCD": row_norm.get("WCD"),
            "Delta_REC_LIQ": row_norm.get("DELTA_REC_LIQ"),
            "Situacao_Geral": row_norm.get("SITUACAO_GERAL"),
            "Data_Vistoria": row_norm.get("DATA_VISTORIA"),
            "Lancamento_Interno": row_norm.get("LANCAMENTO_INTERNO"),
            "Data_Agenda_Cabo": row_norm.get("DATA_AGENDA_CABO"),
            "Gestor_Rubia": row_norm.get("GESTOR_RUBIA"),
            "SEGMENTO": row_norm.get("SEGMENTO"),
            "CLIENTE": row_norm.get("CLIENTE"),
            "ENDERECO": row_norm.get("ENDERECO"),
            "AREA_AT": row_norm.get("AREA_AT"),
            "CONTRATADA": row_norm.get("CONTRATADA"),
            "CONTRATADA2": row_norm.get("CONTRATADA2"),
            "AGING": row_norm.get("AGING"),
            "ID_OSP": row_norm.get("ID_OSP"),
            "STATUS_OSP": row_norm.get("STATUS_OSP"),
            "D_1": row_norm.get("D_1"),
            "DATA": row_norm.get("DATA"),
            "Total_Obra": row_norm.get("TOTAL_OBRA"),
            "Total_Metros": row_norm.get("TOTAL_METROS"),
            "Custo_Por_Km": row_norm.get("CUSTO_POR_KM"),
            "Observacoes": row_norm.get("OBSERVACOES"),
            "ID_Vantive": row_norm.get("ID_VANTIVE"),
            "DATA_PROJETO": row_norm.get("DATA_PROJETO"),
            "AGING_PROJ": row_norm.get("AGING_PROJ"),
            "OBRA_APROVADA": row_norm.get("OBRA_APROVADA"),
            "AGING_EMISSAO": row_norm.get("AGING_EMISSAO"),
            "ALTO_VALOR": row_norm.get("ALTO_VALOR"),
            "VIP": row_norm.get("VIP"),
            "Status_Proj_Icomon": row_norm.get("STATUS_PROJ_ICOMON"),
            "GRUPO_BSC": row_norm.get("GRUPO_BSC"),
            "ConsolidadoEstoque": row_norm.get("CONSOLIDADOESTOQUE"),
            "SegResumo": row_norm.get("SEGRESUMO"),
        }

        pedidos_preparados.append(pedido)

    # 🔄 Envia para o model para inserção em lote
    sucesso = models_insert_pedido_b2b_pendentes(pedidos_preparados)

    if sucesso:
        return {"message": f"{len(pedidos_preparados)} registros inseridos com sucesso"}, 201
    else:
        return {"message": "Erro ao cadastrar registros"}, 500

def controller_create_pedido_b2b_rede_ok(data):
    """
    Recebe lista de pedidos em JSON, normaliza as chaves e envia para o model de inserção.
    """
    if not isinstance(data, list):
        return {"message": "O corpo da requisição deve ser uma lista de objetos JSON"}, 400

    pedidos_preparados = []

    for row in data:
        # 🔧 Normaliza as chaves (por exemplo: "PRAZO REDE" → "PRAZO_REDE")
        row_norm = {normalize_key(k): v for k, v in row.items()}

        pedido = {
            "COD": row_norm.get("COD"),
            "ETP": row_norm.get("ETP"),
            "PRIORIDADE": row_norm.get("PRIORIDADE"),
            "TIPO": row_norm.get("TIPO"),
            "CLIENTE": row_norm.get("CLIENTE"),
            "AREA_AT": row_norm.get("AREA_AT"),
            "CONTRATO": row_norm.get("CONTRATO"),
            "Prazo_Rede": row_norm.get("PRAZO_REDE"),
            "ID_OSP": row_norm.get("ID_OSP"),
            "STATUS_OSP": row_norm.get("STATUS_OSP"),
            "INTERNO_REDE": row_norm.get("INTERNO_REDE"),
            "ID_VANTIVE": row_norm.get("ID_VANTIVE"),
        }

        pedidos_preparados.append(pedido)

    # 🔄 Envia para o model de inserção em lote
    sucesso = models_insert_pedido_b2b_rede_ok(pedidos_preparados)

    if sucesso:
        return {"message": f"{len(pedidos_preparados)} registros inseridos com sucesso"}, 201
    else:
        return {"message": "Erro ao cadastrar registros"}, 500
