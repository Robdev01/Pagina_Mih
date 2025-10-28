-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: vivob2b_bases_mirelle
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.32-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `b2b_vivo_estoque_melhoria`
--

DROP TABLE IF EXISTS `b2b_vivo_estoque_melhoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `b2b_vivo_estoque_melhoria` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Produto` varchar(255) DEFAULT NULL,
  `Pedido` varchar(255) DEFAULT NULL,
  `ID_Vantive` varchar(255) DEFAULT NULL,
  `Cliente` varchar(255) DEFAULT NULL,
  `Status_Vantive` varchar(255) DEFAULT NULL,
  `Data_Entrada` date DEFAULT NULL,
  `Data_RFS` date DEFAULT NULL,
  `OSX` varchar(255) DEFAULT NULL,
  `Natureza_Desc` varchar(255) DEFAULT NULL,
  `Status_SGOS` varchar(255) DEFAULT NULL,
  `Codigo` varchar(255) DEFAULT NULL,
  `Gestor_Atual` varchar(255) DEFAULT NULL,
  `Data_Prevista_PTA` date DEFAULT NULL,
  `Tecnologia` varchar(255) DEFAULT NULL,
  `Endereco` varchar(255) DEFAULT NULL,
  `Cidade` varchar(255) DEFAULT NULL,
  `AT` varchar(255) DEFAULT NULL,
  `Escritorio` varchar(255) DEFAULT NULL,
  `Cluster` varchar(255) DEFAULT NULL,
  `SPE` varchar(255) DEFAULT NULL,
  `Num_ATP` varchar(255) DEFAULT NULL,
  `Status_SPE` varchar(255) DEFAULT NULL,
  `WCD_Grupo_Pendencia` varchar(255) DEFAULT NULL,
  `WCD_Sub_Grupo_Pendencia` varchar(255) DEFAULT NULL,
  `WCD_Grupo_Pendencia_Detalhe` varchar(255) DEFAULT NULL,
  `Velocidade` varchar(255) DEFAULT NULL,
  `ID_Anterior` varchar(255) DEFAULT NULL,
  `ST_VTV_Anterior` varchar(255) DEFAULT NULL,
  `Data_RFS_Anterior` date DEFAULT NULL,
  `LP_Anterior_15` varchar(255) DEFAULT NULL,
  `LP_Anterior_13` varchar(255) DEFAULT NULL,
  `Tronco_SIP` varchar(255) DEFAULT NULL,
  `Tecnologia_Atual` varchar(255) DEFAULT NULL,
  `Status` varchar(255) DEFAULT NULL,
  `Substatus` varchar(255) DEFAULT NULL,
  `Data_Agenda` date DEFAULT NULL,
  `Tipo` varchar(255) DEFAULT NULL,
  `Tipo_Alteracao` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `b2b_vivo_estoque_melhoria`
--

LOCK TABLES `b2b_vivo_estoque_melhoria` WRITE;
/*!40000 ALTER TABLE `b2b_vivo_estoque_melhoria` DISABLE KEYS */;
/*!40000 ALTER TABLE `b2b_vivo_estoque_melhoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `b2b_vivo_ola_analitico`
--

DROP TABLE IF EXISTS `b2b_vivo_ola_analitico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `b2b_vivo_ola_analitico` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Pedido` varchar(50) DEFAULT NULL,
  `ID_Vantive` varchar(50) DEFAULT NULL,
  `ID_Associado` varchar(50) DEFAULT NULL,
  `ID_Cliente` varchar(50) DEFAULT NULL,
  `Cliente` varchar(200) DEFAULT NULL,
  `CNPJ` varchar(20) DEFAULT NULL,
  `UF` char(2) DEFAULT NULL,
  `Cidade` varchar(120) DEFAULT NULL,
  `CEP` varchar(20) DEFAULT NULL,
  `Numero` varchar(20) DEFAULT NULL,
  `Regional` varchar(80) DEFAULT NULL,
  `RegionalRampa` varchar(80) DEFAULT NULL,
  `Esteira` varchar(80) DEFAULT NULL,
  `Esteira_Regionalizada` varchar(80) DEFAULT NULL,
  `SegResumo` varchar(80) DEFAULT NULL,
  `Produto` varchar(150) DEFAULT NULL,
  `Servico` varchar(150) DEFAULT NULL,
  `Tipo_Venda_Detalhes` varchar(150) DEFAULT NULL,
  `Familia` varchar(100) DEFAULT NULL,
  `Oportunidade` varchar(100) DEFAULT NULL,
  `Data_Entrada` date DEFAULT NULL,
  `Data_Assinatura_Contrato` date DEFAULT NULL,
  `Classificacao_Resumo_Atual` varchar(150) DEFAULT NULL,
  `Carteira` varchar(80) DEFAULT NULL,
  `Dias_CarteiraAtual` smallint(6) DEFAULT NULL,
  `Dias_UltimoPCC` smallint(6) DEFAULT NULL,
  `Ativ_Central` varchar(100) DEFAULT NULL,
  `DataTecnica` date DEFAULT NULL,
  `Data_RFS` date DEFAULT NULL,
  `Data_Planejada` date DEFAULT NULL,
  `Data_Expectativa_Cliente` date DEFAULT NULL,
  `DataRede` date DEFAULT NULL,
  `Data_Prevista_OSP` date DEFAULT NULL,
  `Data_Inicio_Rede` date DEFAULT NULL,
  `Data_Fim_Rede` date DEFAULT NULL,
  `Aging_Rede` varchar(50) DEFAULT NULL,
  `Tecnologia_Report` varchar(100) DEFAULT NULL,
  `Velocidade` varchar(50) DEFAULT NULL,
  `Nome_Operadora` varchar(150) DEFAULT NULL,
  `Quebra_Esteira` varchar(100) DEFAULT NULL,
  `Tipo_Alta_Macro` varchar(100) DEFAULT NULL,
  `Delta_REC_LIQ` varchar(100) DEFAULT NULL,
  `Delta_REC_TOTAL` varchar(100) DEFAULT NULL,
  `Escritorio` varchar(150) DEFAULT NULL,
  `Status_SGOS` varchar(150) DEFAULT NULL,
  `Gestor_Atual` varchar(150) DEFAULT NULL,
  `Parceiro` varchar(150) DEFAULT NULL,
  `Classificacao_rede` varchar(150) DEFAULT NULL,
  `SLA_TECNICA` varchar(100) DEFAULT NULL,
  `LOCALIDADE` varchar(150) DEFAULT NULL,
  `Data_Atualizacao` datetime DEFAULT NULL,
  `Natureza_Desc` text DEFAULT NULL,
  `Projetos` text DEFAULT NULL,
  `Projetos_Lote` text DEFAULT NULL,
  `ConsolidadoEstoque` text DEFAULT NULL,
  `ConsolidadoClassificacao` text DEFAULT NULL,
  `ConfigStatus` text DEFAULT NULL,
  `Config_Retrabalho` text DEFAULT NULL,
  `Endereco_Completo` text DEFAULT NULL,
  `Descricao_TarefaSWA` text DEFAULT NULL,
  `ATIVDESCR` text DEFAULT NULL,
  `Router_Desc` text DEFAULT NULL,
  `Router_Desc_Anterior` text DEFAULT NULL,
  `ISIS_MOTIVO_PENDENCIA` text DEFAULT NULL,
  `ISIS_SUB_MOTIVO_PENDENCIA` text DEFAULT NULL,
  `Origem_Pend` text DEFAULT NULL,
  `Observacoes` text DEFAULT NULL,
  `Comentarios` text DEFAULT NULL,
  `Observacao_Extra` text DEFAULT NULL,
  `Justificativa` text DEFAULT NULL,
  `Status_Voz` varchar(100) DEFAULT NULL,
  `Produto_SIP` varchar(150) DEFAULT NULL,
  `Marca_PABX` varchar(100) DEFAULT NULL,
  `Alta_Planta` varchar(50) DEFAULT NULL,
  `Canais` varchar(50) DEFAULT NULL,
  `TM_Tramitacao` varchar(100) DEFAULT NULL,
  `TM_Tec_Total` varchar(100) DEFAULT NULL,
  `TM_Total` varchar(100) DEFAULT NULL,
  `Faixa_Pcc` varchar(50) DEFAULT NULL,
  `Faixa_Tec` varchar(50) DEFAULT NULL,
  `Faixa_Total` varchar(50) DEFAULT NULL,
  `Projeto_Especial` varchar(100) DEFAULT NULL,
  `Flag_Grandes_Projetos` varchar(100) DEFAULT NULL,
  `PRODUTO_STAR` varchar(100) DEFAULT NULL,
  `Segmento_V3` varchar(100) DEFAULT NULL,
  `Label_ERB` varchar(100) DEFAULT NULL,
  `Bucle` varchar(100) DEFAULT NULL,
  `Bucle_Contratada` varchar(100) DEFAULT NULL,
  `GRUPO_BSC` varchar(100) DEFAULT NULL,
  `PRAZO_BSC` varchar(100) DEFAULT NULL,
  `Efika_GIS` varchar(100) DEFAULT NULL,
  `Raia_Remoto` varchar(100) DEFAULT NULL,
  `LP_13` varchar(100) DEFAULT NULL,
  `Cadeia_Pendencias` text DEFAULT NULL,
  `Sub_Cadeia_Pendencias` text DEFAULT NULL,
  `Cadeia_Pendencias_Descricao` text DEFAULT NULL,
  `Cadeia_Pendencias_Macro_SAE` text DEFAULT NULL,
  `DATA_SLA_RFS` text DEFAULT NULL,
  `SLA_RFS` text DEFAULT NULL,
  `SLA_RFS_Resumo` text DEFAULT NULL,
  `DATA_SLA_CONTRATO` text DEFAULT NULL,
  `Data_RFB` text DEFAULT NULL,
  `SLA_RFB` text DEFAULT NULL,
  `SLA` text DEFAULT NULL,
  `SLA_Contrato` text DEFAULT NULL,
  `Sinergia` text DEFAULT NULL,
  `Classificacao_Atual_Vivo_2` text DEFAULT NULL,
  `Sub_Status_Vivo_2` text DEFAULT NULL,
  `Ofensor_Tecnico_Vivo_2` text DEFAULT NULL,
  `OS_SCD` text DEFAULT NULL,
  `OS_TBS` text DEFAULT NULL,
  `TBS_Task_Status_DD` text DEFAULT NULL,
  `TBS_Grupo_Usuario` text DEFAULT NULL,
  `TBS_Task_Ready` text DEFAULT NULL,
  `Data_Emissão_OS` text DEFAULT NULL,
  `Data_Prevista_PTA` text DEFAULT NULL,
  `Motivo_PTA_Cod` text DEFAULT NULL,
  `Componente_HDSL` text DEFAULT NULL,
  `Componente_Juntor` text DEFAULT NULL,
  `Portabilidade` text DEFAULT NULL,
  `Data_Abertura_WCD` text DEFAULT NULL,
  `Num_WCD` text DEFAULT NULL,
  `Data_ATP` text DEFAULT NULL,
  `Num_ATP` text DEFAULT NULL,
  `Setor` text DEFAULT NULL,
  `Pilares` text DEFAULT NULL,
  `SubProcessos` text DEFAULT NULL,
  `SubWCD` text DEFAULT NULL,
  `escopo_PE` text DEFAULT NULL,
  `Status_OSP` text DEFAULT NULL,
  `ID_Draft` text DEFAULT NULL,
  `DraftEncontrado` text DEFAULT NULL,
  `DataCriaçãoDraft` text DEFAULT NULL,
  `IdInternal` text DEFAULT NULL,
  `TarefaAtualDraft` text DEFAULT NULL,
  `DiasNaFilaAtual` text DEFAULT NULL,
  `EntradaFilaAtualDraft` text DEFAULT NULL,
  `Status_Pedido_STAR` text DEFAULT NULL,
  `Tecnologia_Venda` text DEFAULT NULL,
  `Num_LP` text DEFAULT NULL,
  `Tratativa_Monitora` text DEFAULT NULL,
  `Router_Cliente` text DEFAULT NULL,
  `Tipo_Router` text DEFAULT NULL,
  `Router_Atual` text DEFAULT NULL,
  `Caixa_Unica` text DEFAULT NULL,
  `Combo` text DEFAULT NULL,
  `Revenda_VGR` text DEFAULT NULL,
  `ProjRouter` text DEFAULT NULL,
  `RedeNeutra` text DEFAULT NULL,
  `Vantive_Anterior` text DEFAULT NULL,
  `OSX_Anterior` text DEFAULT NULL,
  `Operadora_Anterior` text DEFAULT NULL,
  `Tecnologia_Anterior` text DEFAULT NULL,
  `Router_Anterior` text DEFAULT NULL,
  `Velocidade_Anterior` text DEFAULT NULL,
  `Expurgo` text DEFAULT NULL,
  `TM_PCC` text DEFAULT NULL,
  `TM_Pcc_Total` text DEFAULT NULL,
  `TM_Aprovisionamento` text DEFAULT NULL,
  `TM_Planejamento` text DEFAULT NULL,
  `TM_Vistoria` text DEFAULT NULL,
  `TM_TI` text DEFAULT NULL,
  `TM_Rede` text DEFAULT NULL,
  `TM_Transporte` text DEFAULT NULL,
  `TM_Engenharia` text DEFAULT NULL,
  `TM_MetroConfig` text DEFAULT NULL,
  `TM_LastMile` text DEFAULT NULL,
  `TM_Implantacao` text DEFAULT NULL,
  `TM_Ativacao` text DEFAULT NULL,
  `Faixa_UltimoPCC` text DEFAULT NULL,
  `Vivo` text DEFAULT NULL,
  `BaixaSistemica` text DEFAULT NULL,
  `LiberacaoPCC` text DEFAULT NULL,
  `WCD_Tarefa_Rede` text DEFAULT NULL,
  `MODELO_ATRIBUTOS` text DEFAULT NULL,
  `AT` text DEFAULT NULL,
  `Aging Atual` text DEFAULT NULL,
  `Aging Tec Total` text DEFAULT NULL,
  `Aging Resumo` text DEFAULT NULL,
  `Aging Pcc Total` text DEFAULT NULL,
  `NovosPedidos` text DEFAULT NULL,
  `Regional Desc` text DEFAULT NULL,
  `Envolve Campo` text DEFAULT NULL,
  `Bradesco_Prioritario` text DEFAULT NULL,
  `Capacitacao_ERB` text DEFAULT NULL,
  `TipoCapacitacaoSWA` text DEFAULT NULL,
  `Codigo` text DEFAULT NULL,
  `AgendaTecMes` text DEFAULT NULL,
  `CidadeGPON` text DEFAULT NULL,
  `Agenda_Otimizada` text DEFAULT NULL,
  `BaseCongelada` text DEFAULT NULL,
  `Origem Pend.` text DEFAULT NULL,
  `Flag_AltoValor` text DEFAULT NULL,
  `RESERVA` text DEFAULT NULL,
  `Designador_Acesso` text DEFAULT NULL,
  `Delta_Pos_Neg` text DEFAULT NULL,
  `Data_Planejada_Status` text DEFAULT NULL,
  `Data_Agendamento_Cliente` text DEFAULT NULL,
  `Erb_Flash` text DEFAULT NULL,
  `DsnCorpStatus` text DEFAULT NULL,
  `DsnCorp_Retrabalho` text DEFAULT NULL,
  `Dt_Liberado_Operadora` text DEFAULT NULL,
  `Passagem_PCC` text DEFAULT NULL,
  `Passagem_Viabilidade` text DEFAULT NULL,
  `Passagem_Planejamento` text DEFAULT NULL,
  `Passagem_Vistoria` text DEFAULT NULL,
  `Passagem_TI` text DEFAULT NULL,
  `Passagem_Rede` text DEFAULT NULL,
  `Passagem_Transporte` text DEFAULT NULL,
  `Passagem_Engenharia` text DEFAULT NULL,
  `Passagem_MetroConfig` text DEFAULT NULL,
  `Passagem_LastMile` text DEFAULT NULL,
  `Passagem_Implantacao` text DEFAULT NULL,
  `Passagem_Ativacao` text DEFAULT NULL,
  `Passagem_FaltaRFB` text DEFAULT NULL,
  `ResponsavelPE` text DEFAULT NULL,
  `DATA_PRAZO` text DEFAULT NULL,
  `Nome_Shopping` text DEFAULT NULL,
  `CadeiaEstoqueDias` text DEFAULT NULL,
  `Projetos_LoteNum` text DEFAULT NULL,
  `Status_STAR_Principal` text DEFAULT NULL,
  `TRONCO_SIP` text DEFAULT NULL,
  `AGING_BSC` text DEFAULT NULL,
  `BSC_SEGMENTO` text DEFAULT NULL,
  `BSC_DT_PRAZO_FIM` text DEFAULT NULL,
  `Raia Remoto` text DEFAULT NULL,
  `ID_CPCC_DE_COD` varchar(50) DEFAULT NULL,
  `OSX` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `b2b_vivo_ola_analitico`
--

LOCK TABLES `b2b_vivo_ola_analitico` WRITE;
/*!40000 ALTER TABLE `b2b_vivo_ola_analitico` DISABLE KEYS */;
/*!40000 ALTER TABLE `b2b_vivo_ola_analitico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `b2b_vivo_pendentes`
--

DROP TABLE IF EXISTS `b2b_vivo_pendentes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `b2b_vivo_pendentes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `COD` varchar(255) DEFAULT NULL,
  `NUM_ATP` varchar(255) DEFAULT NULL,
  `SLA` varchar(255) DEFAULT NULL,
  `Equip_Grande_Porte` varchar(255) DEFAULT NULL,
  `PRIORIDADE` varchar(255) DEFAULT NULL,
  `Tecnologia` varchar(255) DEFAULT NULL,
  `STATUS` varchar(255) DEFAULT NULL,
  `Area` varchar(255) DEFAULT NULL,
  `DATA_EMISSAO` date DEFAULT NULL,
  `WCD` varchar(255) DEFAULT NULL,
  `Delta_REC_LIQ` varchar(255) DEFAULT NULL,
  `Situacao_Geral` varchar(255) DEFAULT NULL,
  `Data_Vistoria` date DEFAULT NULL,
  `Lancamento_Interno` varchar(255) DEFAULT NULL,
  `Data_Agenda_Cabo` date DEFAULT NULL,
  `Gestor_Rubia` varchar(255) DEFAULT NULL,
  `SEGMENTO` varchar(255) DEFAULT NULL,
  `CLIENTE` varchar(255) DEFAULT NULL,
  `ENDERECO` varchar(255) DEFAULT NULL,
  `AREA_AT` varchar(255) DEFAULT NULL,
  `CONTRATADA` varchar(255) DEFAULT NULL,
  `CONTRATADA2` varchar(255) DEFAULT NULL,
  `AGING` varchar(255) DEFAULT NULL,
  `ID_OSP` varchar(255) DEFAULT NULL,
  `STATUS_OSP` varchar(255) DEFAULT NULL,
  `D_1` varchar(255) DEFAULT NULL,
  `DATA` date DEFAULT NULL,
  `Total_Obra` varchar(255) DEFAULT NULL,
  `Total_Metros` varchar(255) DEFAULT NULL,
  `Custo_Por_Km` varchar(255) DEFAULT NULL,
  `Observacoes` text DEFAULT NULL,
  `ID_Vantive` varchar(255) DEFAULT NULL,
  `DATA_PROJETO` date DEFAULT NULL,
  `AGING_PROJ` varchar(255) DEFAULT NULL,
  `OBRA_APROVADA` varchar(255) DEFAULT NULL,
  `AGING_EMISSAO` varchar(255) DEFAULT NULL,
  `ALTO_VALOR` varchar(255) DEFAULT NULL,
  `VIP` varchar(255) DEFAULT NULL,
  `Status_Proj_Icomon` varchar(255) DEFAULT NULL,
  `GRUPO_BSC` varchar(255) DEFAULT NULL,
  `ConsolidadoEstoque` varchar(255) DEFAULT NULL,
  `SegResumo` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `b2b_vivo_pendentes`
--

LOCK TABLES `b2b_vivo_pendentes` WRITE;
/*!40000 ALTER TABLE `b2b_vivo_pendentes` DISABLE KEYS */;
/*!40000 ALTER TABLE `b2b_vivo_pendentes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `b2b_vivo_rede_ok`
--

DROP TABLE IF EXISTS `b2b_vivo_rede_ok`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `b2b_vivo_rede_ok` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `COD` varchar(255) DEFAULT NULL,
  `ETP` varchar(255) DEFAULT NULL,
  `PRIORIDADE` varchar(255) DEFAULT NULL,
  `TIPO` varchar(255) DEFAULT NULL,
  `CLIENTE` varchar(255) DEFAULT NULL,
  `AREA_AT` varchar(255) DEFAULT NULL,
  `CONTRATO` varchar(255) DEFAULT NULL,
  `Prazo_Rede` date DEFAULT NULL,
  `ID_OSP` varchar(255) DEFAULT NULL,
  `STATUS_OSP` varchar(255) DEFAULT NULL,
  `INTERNO_REDE` varchar(255) DEFAULT NULL,
  `ID_VANTIVE` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `b2b_vivo_rede_ok`
--

LOCK TABLES `b2b_vivo_rede_ok` WRITE;
/*!40000 ALTER TABLE `b2b_vivo_rede_ok` DISABLE KEYS */;
/*!40000 ALTER TABLE `b2b_vivo_rede_ok` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-28  8:56:18
