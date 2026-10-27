<div align="center">

# 📚 Evolução API Flask

**API REST para gerenciamento de livros: consulte, organize, favorite e acompanhe suas leituras.**

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-orange?style=for-the-badge)

[Sobre](#-sobre-o-projeto) •
[Funcionalidades](#-funcionalidades) •
[Tecnologias](#-tecnologias) •
[Instalação](#-instalação-e-execução) •
[Endpoints](#-endpoints-planejados) •
[Estrutura](#-estrutura-do-projeto)

</div>

---

## 📖 Sobre o projeto

O **Evolução API Flask** é uma aplicação back-end desenvolvida com **Flask** para o gerenciamento de uma biblioteca pessoal. Cada livro possui informações como título, autor e descrição, além de indicadores de leitura que permitem ao usuário marcar seus livros como **favoritos**, **em leitura** ou **finalizados**.

O projeto adota uma arquitetura em camadas, com separação entre a aplicação (rotas), a instância do ORM, os modelos de dados e o controle de migrações do banco.

> 🚧 **Status:** o projeto está em evolução. A configuração base da aplicação, da conexão com o banco e do ORM já está definida; os endpoints listados abaixo compõem o escopo planejado.

---

## ✨ Funcionalidades

| Ícone | Funcionalidade | Descrição |
|:-----:|----------------|-----------|
| 🔍 | **Consultar** | Listar todos os livros ou buscar um livro específico |
| ➕ | **Cadastrar** | Adicionar novos livros à biblioteca |
| ✏️ | **Editar / Atualizar** | Alterar os dados de um livro existente |
| 🗑️ | **Deletar** | Remover um livro da biblioteca |
| ⭐ | **Favoritar** | Marcar ou desmarcar um livro como favorito |
| 📖 | **Em leitura** | Listar e controlar os livros que estão sendo lidos |
| ✅ | **Finalizados** | Listar e controlar os livros já concluídos |

---

## 🛠️ Tecnologias

| Tecnologia | Finalidade |
|------------|------------|
| **Python** | Linguagem principal |
| **Flask** | Framework web e definição dos endpoints |
| **Flask-SQLAlchemy** | ORM para mapeamento e acesso aos dados |
| **Flask-Migrate / Alembic** | Controle de migrações do esquema do banco |
| **psycopg** | Driver de conexão com PostgreSQL |
| **python-dotenv** | Carregamento de variáveis de ambiente (`.env`) |

---

## 🧱 Arquitetura

```mermaid
flowchart LR
    A[👤 Cliente<br/>HTTP/JSON] --> B[🌐 app.py<br/>Flask + Endpoints]
    B --> C[🧩 models/<br/>Modelos de dados]
    C --> D[🔌 db.py<br/>Instância SQLAlchemy]
    D --> E[(🗄️ Banco de dados)]
    F[📝 migrations.py<br/>Controle estrutural] -.-> E
    G[🔐 .env<br/>DATABASE_URL] -.-> B
```

---

## 🗂️ Estrutura do projeto

```text
evolucao-api-flask/
├── 📁 models/            # Modelos de dados (entidade Livro)
├── 📄 app.py             # Aplicação Flask e endpoints
├── 📄 db.py              # Instância do SQLAlchemy (ORM)
├── 📄 migrations.py      # Controle das alterações estruturais do banco
├── 📄 requirements.txt   # Dependências do projeto
└── 📄 README.md          # Documentação
```

| Arquivo | Responsabilidade |
|---------|------------------|
| `app.py` | Cria a aplicação Flask, carrega o `.env`, configura a `DATABASE_URL` e concentra os endpoints |
| `db.py` | Disponibiliza a variável `db`, instância do SQLAlchemy utilizada em toda a aplicação |
| `migrations.py` | Armazena o controle das alterações estruturais realizadas no banco |
| `models/` | Define as entidades persistidas no banco de dados |

---

## 🧾 Modelo de dados

Estrutura de um livro, conforme representação em JSON:

```json
{
    "id": "a9a77436-89ee-4573-a9a5-2171ec0eed2a",
    "title": "O Senhor dos Anéis: A Sociedade do Anel",
    "author": "J.R.R. Tolkien",
    "description": "O primeiro volume de uma das maiores obras de fantasia da literatura mundial.",
    "is_favorite": true,
    "is_reading": false,
    "is_finished": false
}
```

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `id` | `UUID` | Identificador único do livro |
| `title` | `string` | Título da obra |
| `author` | `string` | Autor da obra |
| `description` | `string` | Resumo ou sinopse |
| `is_favorite` | `boolean` | Indica se o livro é favorito |
| `is_reading` | `boolean` | Indica se o livro está em leitura |
| `is_finished` | `boolean` | Indica se a leitura foi concluída |

---

## 🚀 Instalação e execução

### Pré-requisitos

- 🐍 Python 3.11 ou superior
- 🐘 Banco de dados PostgreSQL (ou outro compatível com SQLAlchemy)
- 🔧 Git

### Passo a passo

**1. Clone o repositório**

```bash
git clone https://github.com/luizasilva08/evolucao-api-flask.git
cd evolucao-api-flask
```

**2. Crie e ative o ambiente virtual**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

**3. Instale as dependências**

```bash
pip install -r requirements.txt
```

**4. Configure as variáveis de ambiente**

Crie um arquivo `.env` na raiz do projeto:

```env
DATABASE_URL=postgresql+psycopg://usuario:senha@localhost:5432/nome_do_banco
```

> 🔐 **Importante:** nunca versione o arquivo `.env`. Adicione-o ao `.gitignore`.

**5. Execute a aplicação**

```bash
flask --app app run --debug
```

A API ficará disponível em `http://127.0.0.1:5000`.

---

## 🔌 Endpoints planejados

> Os endpoints abaixo correspondem ao escopo definido para a aplicação.

| Método | Rota | Descrição |
|:------:|------|-----------|
| ![GET](https://img.shields.io/badge/GET-2ea44f?style=flat-square) | `/books` | Lista todos os livros |
| ![GET](https://img.shields.io/badge/GET-2ea44f?style=flat-square) | `/books/<id>` | Consulta um livro pelo ID |
| ![POST](https://img.shields.io/badge/POST-0969da?style=flat-square) | `/books` | Cadastra um novo livro |
| ![DELETE](https://img.shields.io/badge/DELETE-cf222e?style=flat-square) | `/books/<id>` | Remove um livro |
| ![PATCH](https://img.shields.io/badge/PATCH-8250df?style=flat-square) | `/books/<id>` | Atualiza dados de um livro |

### Exemplo de requisição

```bash
curl -X POST http://127.0.0.1:5000/books \
  -H "Content-Type: application/json" \
  -d '{
        "title": "1984",
        "author": "George Orwell",
        "description": "Distopia clássica sobre vigilância e totalitarismo."
      }'
```

---

## 🗺️ Roadmap

- [x] Estrutura base da aplicação Flask
- [x] Configuração do SQLAlchemy e da conexão via `DATABASE_URL`
- [ ] Modelo `Book` com campos de leitura
- [ ] Configuração das migrações com Flask-Migrate
- [ ] CRUD completo de livros
- [ ] Endpoints de favoritos, em leitura e finalizados
- [ ] Validação de dados e tratamento de erros
- [ ] Testes automatizados
- [ ] Documentação interativa (Swagger/OpenAPI)

---

## 👩‍💻 Autora

<div align="center">

Desenvolvido por **Luíza da Silva**

[![GitHub](https://img.shields.io/badge/GitHub-luizasilva08-181717?style=for-the-badge&logo=github)](https://github.com/luizasilva08)

</div>
