# Evolução API Flask

API REST em **Flask** para o gerenciamento de uma biblioteca pessoal de livros. O projeto permite consultar, editar, atualizar e remover livros, além de organizá-los por status de leitura e marcá-los como favoritos.

> **Status do projeto:** em desenvolvimento inicial. A configuração base da aplicação (Flask, SQLAlchemy e variáveis de ambiente) está estruturada; os endpoints listados abaixo correspondem ao escopo planejado.

---

## Sumário

- [Funcionalidades](#funcionalidades)
- [Tecnologias](#tecnologias)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Pré-requisitos](#pré-requisitos)
- [Instalação e execução](#instalação-e-execução)
- [Configuração](#configuração)
- [Migrações de banco de dados](#migrações-de-banco-de-dados)
- [Endpoints previstos](#endpoints-previstos)
- [Próximos passos](#próximos-passos)
- [Autoria](#autoria)

---

## Funcionalidades

- Consultar livros cadastrados
- Editar e atualizar informações de um livro
- Deletar livros
- Favoritar livros
- Listar livros em leitura
- Listar livros finalizados

## Tecnologias

| Camada | Tecnologia |
| --- | --- |
| Linguagem | Python 3 |
| Framework web | Flask |
| ORM | Flask-SQLAlchemy / SQLAlchemy |
| Migrações | Flask-Migrate / Alembic |
| Banco de dados | PostgreSQL (driver `psycopg`) |
| Configuração | python-dotenv |

## Estrutura do projeto

```
evolucao-api-flask/
├── models/            # Modelos (entidades) mapeados pelo SQLAlchemy
├── app.py             # Aplicação Flask e definição dos endpoints
├── db.py              # Instância compartilhada do SQLAlchemy (ORM)
├── migrations.py      # Controle das alterações estruturais do banco
├── requirements.txt   # Dependências do projeto
└── README.md
```

| Arquivo | Responsabilidade |
| --- | --- |
| `app.py` | Cria a aplicação Flask, carrega o `.env` e define a URI do banco de dados. É o ponto de entrada dos endpoints. |
| `db.py` | Expõe a instância `db` do SQLAlchemy, reutilizada em diferentes partes da aplicação. |
| `migrations.py` | Reservado ao controle das alterações estruturais realizadas no banco. |
| `models/` | Reúne as classes que representam as tabelas do banco. |

## Pré-requisitos

- Python 3.10 ou superior
- PostgreSQL em execução (local ou remoto)
- `pip` e, preferencialmente, `venv`

## Instalação e execução

1. **Clonar o repositório**

   ```bash
   git clone https://github.com/luizasilva08/evolucao-api-flask.git
   cd evolucao-api-flask
   ```

2. **Criar e ativar o ambiente virtual**

   ```bash
   python -m venv venv

   # Linux / macOS
   source venv/bin/activate

   # Windows
   venv\Scripts\activate
   ```

3. **Instalar as dependências**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar as variáveis de ambiente** (veja a seção [Configuração](#configuração)).

5. **Executar a aplicação**

   ```bash
   flask --app app run --debug
   ```

   A API ficará disponível em `http://127.0.0.1:5000`.

## Configuração

A aplicação lê suas configurações de um arquivo `.env` na raiz do projeto. Crie o arquivo com o seguinte conteúdo:

```env
DATABASE_URL=postgresql+psycopg://usuario:senha@localhost:5432/nome_do_banco
```

| Variável | Descrição |
| --- | --- |
| `DATABASE_URL` | URI de conexão com o banco de dados, utilizada em `SQLALCHEMY_DATABASE_URI`. |

> **Importante:** não versione o arquivo `.env`. Adicione-o ao `.gitignore` para evitar a exposição de credenciais.

## Migrações de banco de dados

O projeto inclui o **Flask-Migrate** (Alembic) para o versionamento do esquema do banco. Após inicializar a extensão na aplicação, o fluxo usual é:

```bash
flask --app app db init       # executado uma única vez
flask --app app db migrate -m "descrição da alteração"
flask --app app db upgrade
```

## Endpoints previstos

A tabela abaixo descreve o escopo planejado da API. Os caminhos são sugestões e podem ser ajustados durante a implementação.

| Método | Rota | Descrição |
| --- | --- | --- |
| `GET` | `/livros` | Lista todos os livros |
| `GET` | `/livros/<id>` | Consulta um livro específico |
| `PUT` | `/livros/<id>` | Atualiza os dados de um livro |
| `DELETE` | `/livros/<id>` | Remove um livro |
| `PATCH` | `/livros/<id>/favorito` | Marca ou desmarca um livro como favorito |
| `GET` | `/livros/em-leitura` | Lista os livros em leitura |
| `GET` | `/livros/finalizados` | Lista os livros finalizados |

## Próximos passos

- [ ] Definir os modelos em `models/` (por exemplo, `Livro`)
- [ ] Inicializar o Flask-Migrate e gerar a migração inicial
- [ ] Implementar os endpoints descritos acima
- [ ] Adicionar validação de dados e tratamento de erros
- [ ] Incluir testes automatizados
- [ ] Revisar o `requirements.txt`, mantendo apenas as dependências necessárias ao projeto

## Autoria

Desenvolvido por [Luíza da Silva](https://github.com/luizasilva08).
