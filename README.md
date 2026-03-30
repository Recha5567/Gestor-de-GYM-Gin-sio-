# 🏋️ Sistema de Gestão de Ginásio

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/CLI-App-green?style=for-the-badge&logo=windowsterminal&logoColor=white" />
  <img src="https://img.shields.io/badge/CRUD-Operations-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-purple?style=for-the-badge" />
</p>

<p align="center">
  Sistema de gestão em linha de comandos (CLI) desenvolvido em Python para gerir <strong>Alunos</strong> e <strong>Personal Trainers</strong> de um ginásio, com validação de dados e feedback inspirado nos códigos de estado HTTP.
</p>

---

## 📋 Índice

- [Funcionalidades](#️-funcionalidades)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Como Executar](#️-como-executar)
- [Demo](#-demo)
- [Códigos de Resposta](#-códigos-de-resposta)
- [Melhorias Futuras](#-melhorias-futuras)
- [Contribuir](#-contribuir)
- [Licença](#-licença)

---

## ⚙️ Funcionalidades

### 👤 Alunos
Cada aluno é composto pelos campos: **Nome**, **Idade** e **Telefone**.

| Ação | Descrição |
|------|-----------|
| 📋 Listar | Mostra todos os alunos registados |
| ➕ Adicionar | Cria um novo aluno com validação de dados |
| ✏️ Editar | Atualiza os dados de um aluno (campos em branco mantêm o valor anterior) |
| 🗑️ Deletar | Remove um aluno após confirmação |

### 🏃 Personal Trainers
Cada trainer é composto pelos campos: **Nome**, **Especialidade** e **Telefone**.

| Ação | Descrição |
|------|-----------|
| 📋 Listar | Mostra todos os trainers registados |
| ➕ Adicionar | Cria um novo trainer com validação de dados |
| ✏️ Editar | Atualiza os dados de um trainer (campos em branco mantêm o valor anterior) |
| 🗑️ Deletar | Remove um trainer após confirmação |

### 🛠️ Validações
Todas as entradas são validadas antes de serem aceites:

| Campo | Regra |
|-------|-------|
| `Nome` | Apenas letras e espaços |
| `Idade` | Número inteiro entre 5 e 120 |
| `Telefone` | 9 a 15 dígitos (suporta prefixo `+`) |
| `Confirmação` | Resposta obrigatória `s` ou `n` |

---

## 📁 Estrutura do Projeto

```
gym-manager/
├── main.py          # Ponto de entrada — menu principal
├── alunos.py        # Módulo CRUD de alunos
├── pt.py            # Módulo CRUD de personal trainers
└── utilities.py     # Funções utilitárias de validação partilhadas
```

---

## ▶️ Como Executar

### Pré-requisitos

- [Python 3.x](https://www.python.org/downloads/) instalado

### Instalação

```bash
# 1. Clona o repositório
git clone https://github.com/teu-utilizador/gym-manager.git

# 2. Entra na pasta do projeto
cd gym-manager

# 3. Executa a aplicação
python main.py
```

> Não são necessárias dependências externas. O projeto usa apenas a biblioteca padrão do Python.

---

## 🎬 Demo

```
=== SISTEMA DE GESTÃO ===

Escolha a entidade para gerenciar:
1. Alunos
2. Personal Trainers
3. Sair
Opção: 1

--- Alunos ---
a. Listar
b. Adicionar
c. Editar
d. Deletar
Escolha a ação: b

➕ Adicionar Aluno
Nome: João Silva
Idade: 25
Telefone: +351912345678
201 Created - Aluno 'João Silva' adicionado!

200 OK - Lista de Alunos:
1. Nome: João Silva, Idade: 25, Telefone: +351912345678
```

---

## 📡 Códigos de Resposta

O sistema usa uma convenção inspirada nos códigos de estado HTTP:

| Código | Significado |
|--------|-------------|
| `200 OK` | Operação realizada com sucesso |
| `201 Created` | Registo criado com sucesso |
| `204 No Content` | Lista vazia, sem registos |
| `400 Bad Request` | Entrada inválida ou ação cancelada |
| `404 Not Found` | Registo não encontrado |

---

## 🚀 Melhorias Futuras

- [ ] Persistência de dados em ficheiro JSON ou CSV
- [ ] Associação de alunos a personal trainers
- [ ] Pesquisa e filtragem de registos
- [ ] Interface gráfica (GUI) ou web
- [ ] Testes unitários

---

## 🤝 Contribuir

Contribuições são bem-vindas! Para contribuir:

1. Faz um **fork** do projeto
2. Cria uma branch para a tua feature (`git checkout -b feature/nova-funcionalidade`)
3. Faz commit das alterações (`git commit -m 'Adiciona nova funcionalidade'`)
4. Faz push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abre um **Pull Request**

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Consulta o ficheiro [LICENSE](LICENSE) para mais detalhes.

---

<p align="center">Feito com ❤️ em Python</p>
