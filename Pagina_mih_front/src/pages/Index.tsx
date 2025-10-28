import { useState, useRef } from "react";
import { Download, Trash2, Upload } from "lucide-react";
import * as XLSX from "xlsx";

const endpointMap = {
  ola: "/api/upload/pedidos_ola",
  estoque: "/api/upload/pedidos_estoque_melhoria",
  pendentes: "/api/upload/pedidos_pendentes",
  rede_ok: "/api/upload/pedidos_b2b_rede_ok",
};

const Index = () => {
  const uploadCards = [
    {
      title: "Base OLA",
      description: "Envie a planilha Excel da base OLA para atualização no banco de dados.",
      tipo: "ola",
    },
    {
      title: "Base Melhoria",
      description: "Envie a planilha de controle de estoque (Melhoria) em formato Excel.",
      tipo: "estoque",
    },
    {
      title: "Base Pendentes",
      description: "Envie a planilha com os registros pendentes para processamento.",
      tipo: "pendentes",
    },
    {
      title: "Base Rede OK",
      description: "Envie a planilha da base Rede OK em formato Excel para integração.",
      tipo: "rede_ok",
    },
  ];
  ;

  const [selectedFiles, setSelectedFiles] = useState({});
  const [progress, setProgress] = useState({});
  const [messages, setMessages] = useState({});
  const [loading, setLoading] = useState({});
  const fileRefs = useRef({});

  const handleFileChange = (e, tipo) => {
    const file = e.target.files[0];
    setSelectedFiles((prev) => ({ ...prev, [tipo]: file || null }));
  };

  const handleClearFile = (tipo) => {
    setSelectedFiles((prev) => ({ ...prev, [tipo]: null }));
    if (fileRefs.current[tipo]) fileRefs.current[tipo].value = "";
    setProgress((prev) => ({ ...prev, [tipo]: 0 }));
    setMessages((prev) => ({ ...prev, [tipo]: "" }));
  };

  const handleDownloadExample = (tipo) => {
    const links = {
      ola: "/exemplos/exemplo_ola.xlsx",
      estoque: "/exemplos/exemplo_estoque.xlsx",
      pendentes: "/exemplos/exemplo_pendentes.xlsx",
      rede_ok: "/exemplos/exemplo_rede_ok.xlsx",
    };
    const link = links[tipo];
    if (link) {
      const a = document.createElement("a");
      a.href = link;
      a.download = link.split("/").pop();
      a.click();
    }
  };

  const normalizeKey = (key) =>
    key
      .trim()
      .replace(/\s+/g, "_")
      .replace(/[.()]/g, "")
      .replace(/[ÁÀÂÃáàâã]/g, "A")
      .replace(/[ÉÈÊéèê]/g, "E")
      .replace(/[ÍÌÎíìî]/g, "I")
      .replace(/[ÓÒÔÕóòôõ]/g, "O")
      .replace(/[ÚÙÛúùû]/g, "U")
      .replace(/[Çç]/g, "C")
      .toUpperCase();

  const handleSendToDatabase = async (tipo) => {
    const file = selectedFiles[tipo];
    if (!file) {
      alert("Por favor, selecione um arquivo antes de enviar.");
      return;
    }

    const endpoint = endpointMap[tipo];
    if (!endpoint) {
      alert("Tipo de upload não reconhecido.");
      return;
    }

    setLoading((prev) => ({ ...prev, [tipo]: true }));
    setProgress((prev) => ({ ...prev, [tipo]: 0 }));
    setMessages((prev) => ({ ...prev, [tipo]: "" }));

    try {
      // Lê e converte o Excel
      const data = await file.arrayBuffer();
      const workbook = XLSX.read(data, { type: "array" });
      const sheet = workbook.Sheets[workbook.SheetNames[0]];
      const rawData = XLSX.utils.sheet_to_json(sheet, { defval: "" });

      const jsonData = rawData.map((row: Record<string, any>) => {
        const normalized: Record<string, any> = {};
        for (const key in row) {
          if (Object.prototype.hasOwnProperty.call(row, key)) {
            const norm = normalizeKey(key);
            normalized[norm] = row[key];
          }
        }
        return normalized;
      });

      console.log("🔎 Exemplo de linha normalizada:", jsonData[0]);


      const CHUNK_SIZE = 500;
      const totalChunks = Math.ceil(jsonData.length / CHUNK_SIZE);
      let totalSucesso = 0;

      for (let i = 0; i < totalChunks; i++) {
        const chunk = jsonData.slice(i * CHUNK_SIZE, (i + 1) * CHUNK_SIZE);

        const resp = await fetch(`${import.meta.env.VITE_API_URL}${endpoint}`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(chunk),
        });

        if (resp.ok) {
          totalSucesso += chunk.length;
        } else {
          const erro = await resp.text();
          console.error("Erro no bloco", i + 1, erro);
        }

        setProgress((prev) => ({
          ...prev,
          [tipo]: Math.round(((i + 1) / totalChunks) * 100),
        }));
      }

      setMessages((prev) => ({
        ...prev,
        [tipo]: `✅ Upload concluído com sucesso! ${totalSucesso} registros enviados.`,
      }));
    } catch (err) {
      console.error(err);
      setMessages((prev) => ({
        ...prev,
        [tipo]: `❌ Erro: ${err.message}`,
      }));
    } finally {
      setLoading((prev) => ({ ...prev, [tipo]: false }));
    }
  };

  return (
    <main
      className="min-h-screen bg-cover bg-center bg-no-repeat relative p-6 md:p-12"
      style={{
        backgroundImage: "url('/imagens/BG_01_Paixao_Purpura_.jpg')",
      }}
    >
      {/* Overlay translúcido */}
      <div className="absolute inset-0 bg-gradient-to-b from-black/70 via-purple-950/80 to-black/80 backdrop-blur-sm"></div>

      <section className="relative z-10 max-w-7xl mx-auto text-center text-white">
        <header className="mb-12">
          <h1 className="text-5xl font-bold mb-4 bg-gradient-to-r from-purple-400 via-fuchsia-500 to-purple-700 bg-clip-text text-transparent drop-shadow-lg">
            Upload de Bases Vivo B2B – Mirelle
          </h1>
          <p className="text-lg text-gray-200 max-w-2xl mx-auto">
            Envie os arquivos Excel correspondentes a cada categoria para
            atualização no banco de dados.
          </p>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {uploadCards.map((card) => (
            <article
              key={card.tipo}
              className="p-6 bg-black/70 border border-purple-800 rounded-2xl shadow-lg hover:shadow-fuchsia-700/40 transition-all duration-300 text-left"
            >
              <h3 className="text-xl font-semibold mb-1 text-white">
                {card.title}
              </h3>
              <p className="text-sm text-gray-300 mb-3">{card.description}</p>

              <input
                type="file"
                accept=".xls,.xlsx"
                ref={(el) => (fileRefs.current[card.tipo] = el)}
                onChange={(e) => handleFileChange(e, card.tipo)}
                className="block w-full text-sm text-white file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-semibold file:bg-fuchsia-700 file:text-white hover:file:bg-fuchsia-600 transition"
              />

              <p className="text-xs text-gray-400 mt-2 truncate">
                {selectedFiles[card.tipo]?.name || "Nenhum arquivo escolhido"}
              </p>

              <div className="flex flex-wrap gap-2 mt-4">
                <button
                  onClick={() => handleSendToDatabase(card.tipo)}
                  disabled={loading[card.tipo]}
                  className="flex items-center gap-1 px-3 py-2 text-sm bg-green-600 text-white rounded-md hover:bg-green-700 transition disabled:opacity-50"
                >
                  <Upload className="w-4 h-4" />
                  {loading[card.tipo] ? "Enviando..." : "Enviar"}
                </button>

                <button
                  onClick={() => handleClearFile(card.tipo)}
                  className="flex items-center gap-1 px-3 py-2 text-sm bg-red-600 text-white rounded-md hover:bg-red-700 transition"
                >
                  <Trash2 className="w-4 h-4" />
                  Limpar
                </button>

                <button
                  onClick={() => handleDownloadExample(card.tipo)}
                  className="flex items-center gap-1 px-3 py-2 text-sm bg-fuchsia-700 text-white rounded-md hover:bg-fuchsia-600 transition"
                >
                  <Download className="w-4 h-4" />
                  Baixar Exemplo
                </button>
              </div>

              {loading[card.tipo] && (
                <div className="mt-4">
                  <div className="w-full bg-gray-800 h-3 rounded-lg overflow-hidden">
                    <div
                      className="bg-gradient-to-r from-fuchsia-500 to-purple-600 h-3 rounded-lg transition-all"
                      style={{ width: `${progress[card.tipo] || 0}%` }}
                    ></div>
                  </div>
                  <p className="text-xs text-gray-300 mt-1">
                    {progress[card.tipo] || 0}%
                  </p>
                </div>
              )}

              {!loading[card.tipo] && messages[card.tipo] && (
                <p
                  className={`mt-3 text-sm ${
                    messages[card.tipo].startsWith("✅")
                      ? "text-green-400"
                      : "text-red-400"
                  }`}
                >
                  {messages[card.tipo]}
                </p>
              )}
            </article>
          ))}
        </div>
      </section>
    </main>
  );
};

export default Index;