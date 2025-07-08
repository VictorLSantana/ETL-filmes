# 🎬 Projeto ETL de Filmes IMDb + OMDb API

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/6/69/IMDB_Logo_2016.svg" height="80" />
  &nbsp;&nbsp;&nbsp;
  <img src="https://www.omdbapi.com/src/omdbapi.png" height="80" />
</p>

> Pipeline completo de **Engenharia de Dados** usando Python e SQL para extrair, transformar e carregar dados dos 250 melhores filmes segundo o IMDb, com enriquecimento via OMDb API.

---

## 📌 Visão Geral

Este projeto demonstra um pipeline **ETL (Extract, Transform, Load)** aplicado ao domínio de filmes. Os dados são extraídos via **web scraping**, enriquecidos com uma **API pública**, transformados com `pandas` e armazenados em um banco **MySQL**. Por fim, é possível acessar os dados por meio de uma **interface interativa empacotada como `.exe`**.

---

## 🚀 Tecnologias Utilizadas

- 🐍 Python (Selenium, Pandas, Requests, SQLAlchemy)
- 🗃️ MySQL (com `mysql-connector-python`)
- 🌐 OMDb API ([omdbapi.com](https://www.omdbapi.com/))
- 🛠️ PyInstaller (criação do `.exe`)
- 🔐 dotenv (.env para variáveis de ambiente)

---

## 🔄 Pipeline ETL

### 1. **Extração**
- Web scraping do site [IMDb Top 250](https://www.imdb.com/chart/top) com Selenium.
- Coleta dos títulos dos 250 filmes mais bem avaliados.

### 2. **Transformação**
- Limpeza e normalização dos nomes dos filmes.
- Requisições para a **OMDb API** para coletar metadados dos filmes.
- Dados transformados em DataFrame do Pandas e tratados.

### 3. **Carga**
- Dados carregados em uma tabela MySQL usando SQLAlchemy.

---

## 🖥️ Interface Interativa (modo CLI)

Com a interface empacotada em `.exe`, o usuário pode:

1. Escolher um **gênero** e um **diretor**.
2. Visualizar os filmes disponíveis no banco de dados com esse filtro.
3. Selecionar um filme da lista.
4. Receber os detalhes do filme, como:
   - Título, Data de lançamento, Duração
   - Gênero, Diretor, Roteirista, Atores
   - Sinopse, Idioma, País, Prêmios
   - Metascore, Avaliação IMDb, Votos IMDb, Bilheteria

---

## 🧪 Como Executar Localmente

### Pré-requisitos

- Python 3.10+
- MySQL Server
- Biblioteca Selenium + driver do navegador (ex: ChromeDriver)
- Conta e chave da [OMDb API](https://www.omdbapi.com/apikey.aspx)

### Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/etl-filmes.git
cd etl-filmes
