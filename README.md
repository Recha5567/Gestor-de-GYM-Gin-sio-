🏋️ Sistema de Gestão de Ginásio
Sistema de gestão em linha de comandos (CLI) desenvolvido em Python para gerir Alunos e Personal Trainers de um ginásio. Permite realizar operações CRUD completas com validação de dados e feedback inspirado nos códigos de estado HTTP.

📁 Estrutura do Projeto
├── main.py          # Ponto de entrada da aplicação
├── alunos.py        # Módulo de gestão de alunos
├── pt.py            # Módulo de gestão de personal trainers
└── utilities.py     # Funções utilitárias de validação

⚙️ Funcionalidades
👤 Alunos (alunos.py)
Cada aluno é composto pelos campos: Nome, Idade e Telefone.
AçãoDescriçãoListarMostra todos os alunos registadosAdicionarCria um novo aluno com validação de dadosEditarAtualiza os dados de um aluno existente (campos em branco mantêm o valor anterior)DeletarRemove um aluno após confirmação
🏃 Personal Trainers (pt.py)
Cada trainer é composto pelos campos: Nome, Especialidade e Telefone.
AçãoDescriçãoListarMostra todos os trainers registadosAdicionarCria um novo trainer com validação de dadosEditarAtualiza os dados de um trainer existente (campos em branco mantêm o valor anterior)DeletarRemove um trainer após confirmação
🛠️ Utilitários (utilities.py)
Funções partilhadas de validação usadas por ambos os módulos:

validar_nome — aceita apenas letras e espaços
validar_idade — aceita valores inteiros entre 5 e 120
validar_telefone — aceita números com 9 a 15 dígitos (com suporte ao prefixo +)
confirmar_acao — solicita confirmação s/n antes de ações destrutivas


▶️ Como Executar
Pré-requisitos

Python 3.x instalado

Execução
bashpython main.py
Navegação no menu
=== SISTEMA DE GESTÃO ===

Escolha a entidade para gerenciar:
1. Alunos
2. Personal Trainers
3. Sair

--- Alunos ---
a. Listar
b. Adicionar
c. Editar
d. Deletar

📡 Códigos de Resposta
O sistema utiliza uma convenção inspirada nos códigos de estado HTTP para feedback ao utilizador:
CódigoSignificado200 OKOperação realizada com sucesso201 CreatedRegisto criado com sucesso204 No ContentLista vazia, sem registos400 Bad RequestEntrada inválida ou ação cancelada404 Not FoundRegisto não encontrado

📌 Notas

Os dados são guardados apenas em memória durante a execução. Ao sair do programa, os dados são perdidos.
O sistema não utiliza base de dados nem ficheiros externos.
Para persistência de dados, seria necessário integrar armazenamento em ficheiro (ex: JSON, CSV) ou base de dados.
