# Fase 07

## Tópicos abordados na Aula

- 00:00 – O erro que te impede de entender POO
- 00:09 – Os pilares da Programação Orientada a Objetos
- 00:21 – Herança sem complicação (explicação simples)
- 00:56 – Introdução oficial + alerta importante
- 02:16 – Oportunidade que pode mudar sua vida (RJ)
- 04:02 – Os 4 pilares explicados rapidamente
- 05:03 – O que é HERANÇA de verdade
- 06:44 – Vantagens da herança (isso cai em prova!)
- 08:41 – Explicação MAIS FÁCIL que você já viu
- 12:46 – Como funciona herança no diagrama
- 15:48 – Exemplo real: sistema de escola
- 18:00 – O segredo da reutilização de código
- 20:55 – Como aplicar herança em Python (prática)
- 22:04 – Criando classes passo a passo
- 24:03 – Fazendo herança no código (ESSENCIAL)

---

## Perguntas

- Quais são os **pilares da POO**?
- O que é **herança**?
- O que é **superclasse** e **subclasse**?
- O que é **generalização** e **especialização**?
- Como programar **heranças de classe** em Python?

---

## Fase 07 - Melhorando nossa classes

### Os 4 pilares da Programação Orientada a Objetos

- Abstração
- Encapsulamento
- Herança
- Poliformismo

### Herança

Herança é um relacionamento entre itens gerais (ancestrais) e tipos específicos (descendentes) desse itens, que herdam atributos e métodos dos níveis superiores.

**Principais vantagens:**
- reutilização de código
- organização hierárquica
- facilita manuntenção
- extensibilidade
- suporte a polimorfismo

**Superclasse**
- classe base
- ancestral
- classe mãe

**Herança**
- generalização
- relação do tipo "é UM"

**Subclasse**
- classe derivada
- descendente
- classe filha

```python
class Pessoa:
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade
    
    def fazer_aniversário(self):
        self.idade += 1

```
```python
class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"{self.nome} acabou de fazer matrícula")
```
```python
class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"{self.nome} começou a dar aula")
```
```python
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"{self.nome} acabou de bater ponto")
```
