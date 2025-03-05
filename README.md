# 📘 WIKIBOT 1.0

## 📌 Descrição do Projeto
O **WIKIBOT 1.0** é um sistema interativo que permite ao usuário buscar informações extraídas automaticamente da Wikipedia. O bot oferece duas opções de armazenamento:
- **Memória Volátil**: As informações são armazenadas temporariamente na memória.
- **Memória Persistente**: Os dados são armazenados em um arquivo `.txt` para consultas futuras.

## 🛠️ Tecnologias Utilizadas
- **Python 3** 🐍
- **BeautifulSoup** 🏗 (para extração de dados da web)
- **Requests** 🌐 (para requisições HTTP)
- **Colorama** 🎨 (para interface colorida no terminal)
- **TQDM** ⏳ (barra de progresso para extração de dados)
- **Unidecode** 🔡 (normalização de caracteres)
- **Pyfiglet** 🎭 (exibição estilizada do título)

## 📂 Estrutura do Projeto
```
📁 WIKIBOT
│-- 📄 index.py             # Código principal do projeto
│-- 📄 arquivo.txt          # Arquivo para armazenamento persistente de informações
│-- 📂 Parametros/          # Pasta contendo arquivos de parâmetros
│   ├── Parametros.txt      # URLs de páginas a serem consultadas
```

## 🚀 Como Executar o Projeto

### 1️⃣ Instalar Dependências
```sh
pip install beautifulsoup4 requests tqdm pyfiglet colorama unidecode
```

### 2️⃣ Executar o Script
```sh
python index.py
```

### 3️⃣ Escolher o Tipo de Armazenamento
Ao iniciar, o bot solicitará que você escolha uma das opções:
- **Pressione [M]** para **Armazenar na Memória**.
- **Pressione [A]** para **Salvar em Arquivo `.txt`**.

### 4️⃣ Fazer Perguntas
Digite sua pergunta e o bot buscará respostas nos textos extraídos da Wikipedia.

## 🔍 Como Funciona o Código
### 🔹 Coleta de Informações
1. O bot lê URLs do arquivo `Parametros.txt`.
2. Acessa cada página da Wikipedia e extrai os parágrafos principais.
3. Salva os textos extraídos na memória ou em `arquivo.txt`.

### 🔹 Respostas Inteligentes
1. O usuário digita uma pergunta.
2. O bot identifica palavras-chave relevantes.
3. Busca e exibe os trechos mais relevantes do texto extraído.

## ⚠️ Possíveis Problemas e Soluções
| Erro | Solução |
|------|---------|
| `ModuleNotFoundError` | Execute `pip install -r requirements.txt` |
| `ConnectionError` | Verifique sua conexão com a internet |
| `Arquivo não encontrado` | Certifique-se de que `Parametros.txt` existe |

## 📝 Melhorias Futuras
- Adicionar suporte para múltiplas fontes de dados.
- Implementar salvamento de histórico de consultas.
- Melhorar o mecanismo de busca para respostas mais precisas.

---
🚀 **WIKIBOT 1.0** - Sua ferramenta para consultas automáticas na Wikipedia! 🌍

