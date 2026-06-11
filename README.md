# SGA - Sistema de Gerenciamento Acadêmico

O **SGA** é um sistema de gerenciamento acadêmico em console (CLI) desenvolvido em Python. Ele foi projetado utilizando estruturas de dados simples (dicionários e listas) e sem o uso de Orientação a Objetos (classes), focando na modularidade e clareza do código.

O sistema permite gerenciar alunos, disciplinas (matérias) com pesos customizáveis para avaliações, lançar notas e calcular a média ponderada das notas de forma dinâmica.

---

## 🛠️ Arquitetura do Projeto

O projeto é dividido em três módulos principais para manter a separação de responsabilidades:

1. **[sga.py](file:///c:/Users/kauan.ferreira/Documents/teste%20py/sga.py)**: Ponto de entrada do sistema. Gerencia o fluxo de execução, a interface de linha de comando (CLI) e a interação com o usuário.
2. **[dados.py](file:///c:/Users/kauan.ferreira/Documents/teste%20py/dados.py)**: Gerencia o armazenamento em memória dos dados dos alunos e das matérias através de estruturas globais do módulo.
3. **[calculos.py](file:///c:/Users/kauan.ferreira/Documents/teste%20py/calculos.py)**: Módulo contendo a lógica matemática, incluindo o cálculo dinâmico da média ponderada.

---

## 🚀 Funcionalidades

- **Cadastrar Aluno**: Permite registrar alunos com número de matrícula único e nome completo.
- **Cadastrar Matéria**: Cria disciplinas com código identificador único, nome e número configurável de avaliações, cada uma contendo seu próprio peso acadêmico.
- **Lançar Nota de Aluno**: Permite associar notas (de 0.0 a 10.0) a avaliações específicas de matérias em que o aluno está cursando.
- **Exibir Boletim do Aluno**: Mostra as notas de cada avaliação e calcula automaticamente a **Média Ponderada Final** para todas as matérias. Caso alguma nota ainda não tenha sido cadastrada, o sistema exibe o status de avaliação como *Pendente* e calcula a média considerando apenas as notas já lançadas.
- **Listar Alunos e Matérias**: Permite visualizar rapidamente todos os registros cadastrados no sistema.

---

## 🎲 Dados de Teste Pré-carregados

Para facilitar a experimentação do sistema, o script já inicia com os seguintes registros simulados:

- **Matérias**:
  - `MAT` (Matemática) - 3 avaliações (Pesos: 3.0, 3.0 e 4.0)
  - `PORT` (Português) - 2 avaliações (Pesos: 4.0 e 6.0)
  - `GEO` (Geografia) - 2 avaliações (Pesos: 5.0 e 5.0)
- **Alunos**:
  - `Ana Silva` (Matrícula: `1010`)
  - `Bruno Costa` (Matrícula: `2020`)
- **Notas**: Lançamentos parciais para fins de teste.

---

## 🏃 Como Executar

Certifique-se de ter o Python 3 instalado em sua máquina.

1. Abra o terminal ou prompt de comando.
2. Navegue até a pasta do projeto.
3. Execute o comando abaixo:

```bash
python sga.py
```

---

## 📝 Exemplo de Uso do Boletim

Ao selecionar a opção **4 (Exibir Boletim)** para a aluna **Ana Silva** (matrícula `1010`), o terminal exibirá:

```text
Aluno: Ana Silva | Matrícula: 1010
--------------------------------------------------
Matéria: Matemática (MAT)
  Notas: Av1 (Peso 3.0): 8.0 | Av2 (Peso 3.0): 7.5 | Av3 (Peso 4.0): 9.0
  Média Ponderada Final: 8.25
--------------------------------------------------
Matéria: Português (PORT)
  Notas: Av1 (Peso 4.0): 7.0 | Av2 (Peso 6.0): 8.5
  Média Ponderada Final: 7.90
--------------------------------------------------
```
