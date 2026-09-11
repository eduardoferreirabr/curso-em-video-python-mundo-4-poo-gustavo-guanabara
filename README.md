# 🐍 Python Mundo 4 – Programação Orientada a Objetos (POO)

> Repositório de estudos do **Curso de Python POO** do professor **Gustavo Guanabara** – [Curso em Vídeo](https://www.cursoemvideo.com).

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![uv](https://img.shields.io/badge/Gerenciador-uv-5C4EE5?style=flat)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/badge/Linter-Ruff-FF5A5F?style=flat)](https://github.com/astral-sh/ruff)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🎓 Sobre o Curso

O **Python Mundo 4** é o módulo de **Programação Orientada a Objetos (POO)** do curso gratuito de Python do Gustavo Guanabara no [Curso em Vídeo](https://www.cursoemvideo.com). O curso aborda os fundamentos e os quatro pilares da POO aplicados à linguagem Python, com aulas teóricas, exercícios práticos e desafios.

🔗 **Playlist oficial no YouTube:**
**[▶ Curso Python POO – Gustavo Guanabara](https://youtube.com/playlist?list=PLHz_AreHm4dn_RXXoa3Ameh77f95Hgwv3)**

> **Pré-requisito:** Recomenda-se ter concluído os Mundos 1, 2 e 3 do curso de Python do Curso em Vídeo antes de iniciar.

---

## 📚 Conteúdo das Aulas

| Aula | Título |
|------|--------|
| 00 | Python Orientado a Objetos: O Guia Definitivo para Iniciantes – Onde está o Mundo 4? |
| 01 | Crise do Software: O motivo do surgimento da POO |
| 02 | As 6 Vantagens da POO: Programação Orientada a Objetos |
| 03 | POO para Iniciantes: Guia Definitivo – Classes, Objetos, Atributos, etc. |
| 04 | Python Orientado a Objetos: Criando Classes e Objetos na Prática |
| 05 | Melhorando Classes e Criando uma Conta Bancária na Prática |
| 05 (Extra) | Aprenda POO com Desafios em Python |
| 07 | Herança em Python explicada como nunca fizeram |
| 08 | Abstração: um dos Pilares Centrais da POO |
| 09 | Desafios de Herança, Abstração e Classes |
| 10 | Encapsulamento: público, protegido e privado (Parte 1) |
| 11 | Encapsulamento: Getters, Setters e @Property (Parte 2) |
| 12 | Domine Encapsulamento em Python com Getters, Setters e 6 Projetos Reais |
| 13 | Polimorfismo em Python: Override, Overload e Duck Typing |
| 14 | Operator Overloading em Python: Personalizando Operadores na Prática |
| 15 | 7 Desafios de Polimorfismo em Python – POO na Prática |

---

## 🏛️ Pilares da POO abordados

| Pilar | Descrição |
|-------|-----------|
| **Encapsulamento** | Visibilidade (público, protegido, privado), getters, setters e `@property` |
| **Herança** | Reutilização de código com classes pai e filho |
| **Polimorfismo** | Override, Overload e Duck Typing; Operator Overloading |
| **Abstração** | Classes e métodos abstratos com `ABC` |

---

## 🗂️ Estrutura do Projeto

```
src/
└── curso_em_video_python_mundo_4_poo_gustavo_guanabara/
    ├── aulas/          # Anotações em Markdown de cada aula (aula_00 a aula_15)
    ├── exercicios/     # Exercícios resolvidos em Python (ex_001 a ex_017)
    ├── desafios/       # Desafios em Markdown e resoluções em Python (desafio_001 a desafio_022)
    └── rich/           # Exemplos de uso da biblioteca Rich para terminal
```

### 📝 Aulas (`aulas/`)
Anotações em formato Markdown organizadas por aula (`aula_00` a `aula_15`), contendo os conceitos teóricos apresentados nos vídeos.

### 💻 Exercícios (`exercicios/`)
17 exercícios práticos resolvidos em Python (`ex_001` a `ex_017`), cobrindo desde criação de classes simples até hierarquias com herança múltipla, encapsulamento e polimorfismo.

### 🏆 Desafios (`desafios/`)
22 desafios propostos pelo professor (`desafio_001` a `desafio_022`):
- **001 a 015** – Enunciados em Markdown (a resolver)
- **016 a 022** – Resoluções implementadas em Python

### 🎨 Rich (`rich/`)
5 scripts de exemplo explorando a biblioteca [`rich`](https://github.com/Textualize/rich) para saída formatada no terminal (tabelas, painéis, cores, etc.).

---

## ⚙️ Configuração do Ambiente

Este projeto utiliza [`uv`](https://github.com/astral-sh/uv) como gerenciador de pacotes e ambiente virtual.

### Pré-requisitos
- Python 3.12+
- [`uv`](https://docs.astral.sh/uv/getting-started/installation/)

### Instalação

```bash
# Clone o repositório
git clone https://github.com/eduardoferreirabr/curso-em-video-python-mundo-4-poo-gustavo-guanabara.git
cd curso-em-video-python-mundo-4-poo-gustavo-guanabara

# Crie o ambiente virtual e instale as dependências
uv sync
```

### Dependências

| Pacote | Versão | Finalidade |
|--------|--------|------------|
| [`rich`](https://github.com/Textualize/rich) | ≥ 15.0.0 | Saída formatada e colorida no terminal |

### Executando scripts individuais

```bash
# Exemplo: executar um exercício
uv run python -m src.curso_em_video_python_mundo_4_poo_gustavo_guanabara.exercicios.ex_006

# Exemplo: executar um script da pasta rich
uv run python src/curso_em_video_python_mundo_4_poo_gustavo_guanabara/rich/rich_004.py
```

---

## 🔧 Ferramentas de Desenvolvimento

| Ferramenta | Finalidade |
|------------|------------|
| [uv](https://github.com/astral-sh/uv) | Gerenciamento de pacotes e ambiente virtual |
| [Ruff](https://github.com/astral-sh/ruff) | Linter e formatador de código |

### Formatando o código

```bash
uv run ruff format .
uv run ruff check .
```

---

## 👨‍🏫 Professor

**Gustavo Guanabara** – Professor e criador do [Curso em Vídeo](https://www.cursoemvideo.com), um dos maiores portais de cursos gratuitos em português do Brasil.

- 🌐 Site: [cursoemvideo.com](https://www.cursoemvideo.com)
- ▶️ YouTube: [youtube.com/@CursoemVideo](https://www.youtube.com/@CursoemVideo)

---

## 👤 Autor do Repositório

**Eduardo Ferreira**
- GitHub: [@eduardoferreirabr](https://github.com/eduardoferreirabr)
- E-mail: eduardociviluff@gmail.com

---

## 📄 Licença

Este projeto está licenciado sob a licença **MIT** – veja o arquivo [LICENSE](LICENSE) para mais detalhes.

> ⚠️ Este repositório é exclusivamente para fins de **estudo pessoal**. Todo o conteúdo didático pertence ao professor Gustavo Guanabara e ao Curso em Vídeo.
