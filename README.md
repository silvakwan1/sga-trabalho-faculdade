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

- **Cadastrar Aluno**: Permite registrar alunos do **Ensino Médio** com número de matrícula único e nome completo. Ao cadastrar, é sugerida a pré-vinculação automática das disciplinas básicas do Ensino Médio.
- **Cadastrar Matéria**: Cria disciplinas com código identificador único, nome, número configurável de avaliações com seus respectivos pesos acadêmicos e a carga horária total de aulas.
- **Lançar Nota de Aluno**: Associa notas (de 0.0 a 10.0) a avaliações específicas de matérias em que o aluno está cursando.
- **Lançar Falta de Aluno**: Registra o total de faltas obtidas pelo estudante em uma disciplina específica (limitado à carga horária da matéria).
- **Gerar Relatório Final do Aluno (LDB)**: Exibe o boletim acadêmico final contendo o nível de ensino, disciplinas cursadas, médias finais calculadas, total de faltas, percentual de frequência e situação final.
- **Listar Alunos e Matérias**: Permite visualizar rapidamente todos os registros e configurações acadêmicas.

---

## ⚖️ Critérios de Avaliação LDB (Ensino Médio)

Em conformidade com a Lei de Diretrizes e Bases da Educação Nacional (LDB nº 9.394/1996), o sistema classifica o estudante em um dos três estados possíveis:

*   **Aprovado**: Média Final $\ge$ 6.0 e Frequência $\ge$ 75% em todas as disciplinas.
*   **Reprovado por nota**: Média Final $<$ 6.0 e Frequência $\ge$ 75%.
*   **Reprovado por falta**: Frequência $<$ 75%, independente da nota final.

---

## 🎲 Dados de Teste Pré-carregados

O sistema já inicia pré-carregado com 3 alunos simulando cada uma das situações possíveis para facilitar os testes:

1.  **Ana Silva** (Matrícula: `1010`) $\rightarrow$ **Aprovado**
    *   Matemática: Média 8.25 | Frequência 95% (4 faltas em 80 aulas)
    *   Português: Média 7.90 | Frequência 92.5% (6 faltas em 80 aulas)
    *   Geografia: Média 8.50 | Frequência 95% (2 faltas em 40 aulas)
2.  **Bruno Costa** (Matrícula: `2020`) $\rightarrow$ **Reprovado por nota**
    *   Matemática: Média 5.55 | Frequência 90% (8 faltas em 80 aulas)
    *   Português: Média 7.70 | Frequência 87.5% (10 faltas em 80 aulas)
    *   Geografia: Média 7.50 | Frequência 90% (4 faltas em 40 aulas)
3.  **Carla Dias** (Matrícula: `3030`) $\rightarrow$ **Reprovado por falta**
    *   Matemática: Média 8.50 | Frequência 68.75% (25 faltas em 80 aulas)
    *   Português: Média 8.00 | Frequência 93.75% (5 faltas em 80 aulas)

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

## 📝 Exemplo de Relatório Acadêmico Final

Ao selecionar a opção **5 (Gerar Relatório Final)** para a aluna **Ana Silva** (matrícula `1010`), o terminal exibirá:

```text
=================================================================
                 RELATÓRIO ACADÊMICO FINAL
                 (DIRETRIZES LDB - 75% FREQ)
=================================================================
Aluno: ANA SILVA
Matrícula: 1010
Nível de Ensino: Ensino Médio
-----------------------------------------------------------------
Critérios: Nota Mínima: 6.0 | Frequência Mínima: 75%
-----------------------------------------------------------------
DISCIPLINA      | MÉDIA  | FALTAS   | FREQ %   | SITUAÇÃO            
-----------------------------------------------------------------
Matemática      | 8.25   | 4 /80    | 95.0 %   | Aprovado            
Português       | 7.90   | 6 /80    | 92.5 %   | Aprovado            
Geografia       | 8.50   | 2 /40    | 95.0 %   | Aprovado            
-----------------------------------------------------------------
RESUMO GERAL DO DESEMPENHO:
  Média Geral das Disciplinas: 8.22
  Total de Faltas Acumuladas: 12 faltas em 200 aulas
  Frequência Geral do Aluno:  94.00%

****************************************
  SITUAÇÃO GERAL: APROVADO
****************************************
=================================================================
```

