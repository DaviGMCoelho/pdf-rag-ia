# 📚 RAG com IA para leitura de PDFs

Este projeto implementa um sistema de **Recuperação Aumentada por Geração (RAG)**, combinando **LangChain** e **ChromaDB** para permitir consultas inteligentes em documentos PDF.  

A solução lê arquivos PDF, gera embeddings de cada chunk do texto, armazena em um banco vetorial (**Chroma**), e utiliza um modelo LLM rodando no **LangChain** para responder perguntas com base no conteúdo dos documentos.

---

## 🚀 Tecnologias utilizadas
- [Python 3.13.2](https://www.python.org/) → linguagem back-end
- [LangChain](https://www.langchain.com/) → orquestração do pipeline RAG e execução do modelo 
- [Chroma](https://www.trychroma.com/) → banco vetorial para armazenamento dos embeddings
- Bibliotecas utilzadas → rag_project/requirements.txt

---

## ⚙️ Como funciona
1. O usuário coloca um ou mais arquivos PDF na pasta 'documents'.  
2. Os arquivos são transformados em texto.
3. O texto é dividido em chunks e convertido em **embeddings** por um modelo de geração de embeddings específico **nomic-embed-text-v1.5-multimodal**.  
4. Os embeddings são armazenados no **ChromaDB**.  
5. Ao fazer uma pergunta, o sistema busca os trechos mais relevantes no banco vetorial.  
6. O modelo LLM Ollama **Mistral** (via **LangChain**) gera a resposta usando os trechos recuperados como contexto.  

---

## 📥 Instalação

Baixe os arquivos do projeto e execute na usa IDE ou

Clone o repositório caso estiver com o Git instalado:

```bash
git clone https://github.com/seu-usuario/rag-pdf-ai.git
cd rag-pdf-ai
```

Crie e ative um ambiente virtual:

```bash
python -m venv venv
python -m .\venv\Scripts\activate # Windows
source venv/bin/activate # Linux/Mac
```

Instale as dependências:
```bash
python -m pip install -r requirements.txt
```

Certifique-se de ter o Ollama instalado e os modelos baixados:
```bash
ollama run mistral
ollama pull DC1LEX/nomic-embed-text-v1.5-multimodal
```

---

## ▶️ Como usar

1. Coloque seus arquivos PDF na pasta documents/.
2. Rode o programa na sua IDE
3. Vá em adicionar novos documentos e aguarde terminar
4. Vá em realizar perguntas e comece a usar
5. Qualquer dúvida, consulte o manual de intruções ou me chama!

## 📂 Estrutura do projeto

```bash
rag_project/
│── documents/           # PDFs para indexação
│── data/                
│   ├── database/        # Base vetorial do Chroma
│── src/
│   ├── controller/      # Lógica de controle
│   ├── service/         # Serviços de IA/RAG/Leitura
│   ├── validation/      # Regras de validação
│   ├── view/            # Interface
│── main.py              # Ponto de entrada
│── README.md            # Arquivo de introdução
│── requirements.txt     # Bibliotecas utilizadas
```

## 🔮 Melhorias futuras
- Adicionar suporte a outros formatos (Word, TXT).
- Interface gráfica (CustomTkinter).
- Escolha dinâmica de modelos via Ollama ou API.
- Resumo automático dos documentos.

## 👨‍💻 Autor
Projeto desenvolvido por [DaviGMCoelho](https://www.linkedin.com/in/DaviGMCoelho/) 🚀