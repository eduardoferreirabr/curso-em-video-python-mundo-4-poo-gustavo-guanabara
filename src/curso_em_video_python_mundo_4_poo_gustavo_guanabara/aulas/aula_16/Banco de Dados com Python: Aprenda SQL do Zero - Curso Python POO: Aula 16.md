# Fase 16

## Tópicos abordados na Aula

- 00:00 Introdução à aula de banco de dados
- 01:14 Aula 16 — Introdução aos bancos de dados com SQLite
- 02:05 Recado especial e história de sucesso da Ftec
- 03:54 O que é um banco de dados?
- 04:30 Memória principal, memória RAM e dados temporários
- 05:01 Por que os dados são perdidos ao fechar um programa?
- 05:43 Memória secundária: HD, SSD e armazenamento permanente
- 06:14 Arquivos de texto e suas limitações
- 06:40 O que diferencia um banco de dados de um arquivo comum?
- 07:15 Tabelas, registros, campos e organização dos dados
- 08:00 Relacionamentos entre dados e tabelas
- 08:20 O que é um banco de dados relacional?
- 08:49 Exemplos de sistemas de bancos de dados relacionais
- 09:23 Por que escolher SQLite para o curso de Python?
- 10:06 Vantagens do SQLite: simplicidade e integração com Python
- 10:51 O que é SQL (Structured Query Language)?
- 11:08 Registros, campos e estrutura dos dados
- 11:18 Curso de Banco de Dados com MySQL do Curso em Vídeo
- 11:55 Comando CREATE TABLE: criando uma tabela
- 12:29 Chave primária, nome e data de nascimento
- 12:57 Comando INSERT INTO: cadastrando registros
- 13:12 Como armazenar datas em bancos de dados
- 13:51 Comando SELECT: consultando informações
- 14:03 Filtrando registros por data de nascimento
- 14:23 Onde aprender SQL e aprofundar os estudos
- 15:23 Criando o primeiro banco de dados SQLite
- 15:43 Instalando o DB Browser for SQLite
- 16:28 SQLite como arquivo e a integração com Python
- 17:13 Criando um novo banco de dados
- 17:46 Criando a tabela amigos e definindo seus campos
- 18:27 Inserindo registros e preenchendo os dados
- 18:56 Salvando as alterações no banco de dados
- 19:20 Criando um banco de dados SQLite online
- 19:56 Criando tabelas com o comando CREATE TABLE IF NOT EXISTS
- 20:22 Inserindo registros e consultando dados com SELECT
- 20:47 Salvando e baixando o banco de dados criado online
- 21:21 Canal de distribuição do Curso em Vídeo no Telegram
- 21:59 Revisão dos conceitos e encerramento da aula
- 22:14 Like, comentários e compartilhamento
- 22:34 Próxima aula: acessando o banco de dados com Python

---

## Perguntas:

- O que é **banco de dados**?
- O que é **SQL**?
- Por que usar **sqlite**?
- Como criar um banco **sqlite**?

---

## Fase 16 - Banco de Dados SQLite - Parte 1

Um banco de dados é composto por uma ou mais tabelas.

Banco de Dados Relacional

- PostgreSQL
- MySQL
- MariaDB
- Oracle
- SQL Server
- SQLite

---

### SQL

* Structured
* Query
* Language

```sql
CREATE TABLE amigos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    nascimento DATE NOT NULL
)
```

```sql
INSERT INTO amigos (
    (nomem, nascimento)
VALUES
    ('Lucas Santos', '1995-04-12')
    ('Beatriz Lima', '2001-11-23')
    ('Rafael Costa', '1988-07-05')
)
```

```sql
SELECT nome, nascimento
FROM amigos
WHERE nascimento >= '2000-01-01'
```
