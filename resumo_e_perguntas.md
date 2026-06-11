# Guia de Estudo e Resumo Técnico: SGA (Ensino Médio)

Este documento apresenta um resumo das implementações técnicas, das estruturas e tipos de dados utilizados no **SGA (Sistema de Gerenciamento Acadêmico)**, além de compilar **10 perguntas técnicas** que a professora pode fazer durante a apresentação do projeto.

---

## 1. Resumo Técnico do que foi Feito
O sistema SGA foi evoluído para simular a gestão acadêmica completa de estudantes do **Ensino Médio** em conformidade com as diretrizes da **LDB (Lei de Diretrizes e Bases da Educação - nº 9.394/1996)**. As principais implementações foram:
- **Gestão de Faltas e Carga Horária**: Criação de estruturas para rastrear o número de aulas por matéria e registrar as faltas de cada estudante.
- **Validação de Situação Final (LDB)**: Criação de algoritmo que classifica o estudante em: **Aprovado** (Média $\ge$ 6.0 e Frequência $\ge$ 75%), **Reprovado por Nota** (Média < 6.0 e Frequência $\ge$ 75%) ou **Reprovado por Falta** (Frequência < 75%).
- **Relatório Acadêmico Final**: Desenvolvimento de um gerador de boletim final detalhado por console.
- **Modularização Sem Classes**: O projeto manteve-se estritamente fiel ao desenvolvimento procedural, utilizando apenas funções de manipulação de estruturas em arquivos separados para garantir organização e legibilidade.

---

## 2. Dados, Tipos e Estrutura de Dados Usadas

O sistema armazena as informações na memória RAM durante a execução por meio de dois dicionários globais localizados em `dados.py`:

### A. Dicionário `alunos`
*   **Tipo Geral**: `dict`
*   **Chave**: Matrícula do aluno (`str`)
*   **Valor**: Um dicionário (`dict`) contendo as chaves:
    *   `"matricula"`: `str`
    *   `"nome"`: `str`
    *   `"nivel"`: `str` (padrão `"Ensino Médio"`)
    *   `"notas"`: `dict`
        *   *Chave*: Código da matéria (`str`) (ex: `"MAT"`)
        *   *Valor*: Lista (`list`) de notas contendo `float` ou `None` (caso a avaliação ainda esteja pendente). Exemplo: `[8.0, 7.5, None]`
    *   `"faltas"`: `dict`
        *   *Chave*: Código da matéria (`str`)
        *   *Valor*: Inteiro (`int`) representando as faltas acumuladas do aluno. Exemplo: `4`
    *   `"aulas"`: `dict`
        *   *Chave*: Código da matéria (`str`)
        *   *Valor*: Inteiro (`int`) representando o total de aulas previstas para aquela matéria. Exemplo: `80`

**Exemplo visual da estrutura de um aluno:**
```python
alunos = {
    "1010": {
        "matricula": "1010",
        "nome": "Ana Silva",
        "nivel": "Ensino Médio",
        "notas": {
            "MAT": [8.0, 7.5, 9.0],
            "PORT": [7.0, 8.5]
        },
        "faltas": {
            "MAT": 4,
            "PORT": 6
        },
        "aulas": {
            "MAT": 80,
            "PORT": 80
        }
    }
}
```

### B. Dicionário `materias`
*   **Tipo Geral**: `dict`
*   **Chave**: Código único da matéria (`str`) (ex: `"MAT"`)
*   **Valor**: Um dicionário (`dict`) contendo as chaves:
    *   `"codigo"`: `str` (ex: `"MAT"`)
    *   `"nome"`: `str` (ex: `"Matemática"`)
    *   `"pesos"`: Lista (`list`) de números decimais (`float`) representando o peso de cada prova. Exemplo: `[3.0, 3.0, 4.0]`
    *   `"total_aulas"`: Inteiro (`int`) representando a carga horária em número de aulas. Exemplo: `80`

**Exemplo visual da estrutura de uma matéria:**
```python
materias = {
    "MAT": {
        "codigo": "MAT",
        "nome": "Matemática",
        "pesos": [3.0, 3.0, 4.0],
        "total_aulas": 80
    }
}
```

---

## 3. Top 10 Perguntas Técnicas da Professora e Como Responder

### Pergunta 1: Como e onde os dados dos alunos e das matérias são salvos no sistema?
*   **Resposta**: Os dados são salvos em memória RAM enquanto o programa está rodando, usando dois dicionários globais (`alunos` e `materias`) dentro do arquivo `dados.py`. Como o armazenamento é local na memória temporária do Python, os dados cadastrados são resetados quando fechamos o programa.

### Pergunta 2: Por que vocês optaram por usar dicionários encadeados e listas em vez de usar Classes (Orientação a Objetos)?
*   **Resposta**: Optamos por uma modelagem de programação estruturada/procedural utilizando tipos fundamentais do Python (`dict`, `list`). Isso atende aos objetivos de manter o cômputo do código enxuto, de fácil legibilidade e focando estritamente na prática dos conceitos de estruturas de dados e modularização que foram estudados até este período letivo.

### Pergunta 3: Como a média ponderada é calculada se algumas notas das avaliações ainda não foram lançadas (são `None`)?
*   **Resposta**: Na função `calcular_media_ponderada` (`calculos.py`), nós filtramos a lista de notas. Se o valor em uma posição da lista de notas for `None`, a nota e o peso correspondente daquele índice são ignorados. O cálculo da média ponderada é feito de forma dinâmica multiplicando a nota pelo peso e dividindo apenas pela soma dos pesos das avaliações que já possuem notas efetivamente registradas.

### Pergunta 4: Se o aluno ainda não possui notas ou faltas cadastradas em uma matéria e tentamos realizar um lançamento, como o sistema evita um erro de chave inexistente (`KeyError`)?
*   **Resposta**: Criamos a função `inicializar_aluno_materia(matricula, codigo_materia)` em `dados.py`. Antes de qualquer operação de lançamento de nota ou falta, essa função é chamada. Ela verifica se o código da matéria existe nas notas/faltas/aulas do aluno. Se não existir, ela cria as chaves no dicionário interno com valores iniciais padrão (lista cheia de `None` para notas, `0` para faltas e o valor padrão de `total_aulas` da matéria para as aulas).

### Pergunta 5: Como o sistema garante que o usuário não cause uma quebra de execução (Crash/Bug) ao digitar um texto em campos que esperam números como Nota ou Quantidade de Faltas?
*   **Resposta**: Desenvolvemos funções de entrada de dados seguras no arquivo `sga.py` denominadas `ler_float(mensagem)` e `ler_int(mensagem)`. Elas utilizam um loop `while True` com o bloco de tratamento de exceções `try-except ValueError`. Se o usuário digita algo que não pode ser convertido para `float` ou `int`, o programa captura a exceção, exibe uma mensagem de erro na tela e solicita a redigitação de forma amigável sem interromper o fluxo do sistema.

### Pergunta 6: Na função de lançar faltas, existe alguma validação pedagógica ou de limite para impedir que sejam digitados valores incoerentes?
*   **Resposta**: Sim. Na função `lancar_faltas` em `dados.py`, nós realizamos duas validações cruciais: garantimos que a quantidade de faltas não seja negativa (`< 0`) e verificamos se o número de faltas não excede o limite total de aulas cadastradas para aquela disciplina no boletim do aluno. Se o usuário digitar um valor fora desse intervalo, a função retorna `False` acompanhado de uma mensagem de erro instrutiva.

### Pergunta 7: Como vocês implementaram a regra da LDB sobre a frequência de 75% no cálculo da situação geral do aluno?
*   **Resposta**: A situação é avaliada por disciplina na função `determinar_situacao` em `calculos.py`. Além disso, no relatório final em `sga.py`, acumulamos o total de aulas e o total de faltas de todas as disciplinas do aluno para calcular sua **Frequência Geral**. A regra geral diz: se a frequência geral acumulada for menor que 75% ou se o aluno for reprovado por falta em alguma disciplina individual, a situação final dele será classificada como **Reprovado por falta** (que tem prioridade legal sobre a nota).

### Pergunta 8: Qual é a diferença prática entre as funções localizadas em `calculos.py` e em `dados.py`?
*   **Resposta**: Aplicamos o princípio da responsabilidade única e modularidade. O arquivo `dados.py` funciona como uma camada de dados (Data Layer), possuindo funções que acessam e alteram o estado dos dicionários (como cadastros e gravações). O arquivo `calculos.py` é uma biblioteca de funções utilitárias puras (como cálculo de média e de percentual); elas apenas recebem parâmetros numéricos/listas e retornam resultados calculados, sem alterar diretamente nenhuma variável global.

### Pergunta 9: Como funciona o retorno das funções de cadastro e manipulação de estado?
*   **Resposta**: Elas utilizam o recurso de retorno múltiplo do Python. Cada função retorna uma tupla `(sucesso: bool, mensagem: str)`. O chamador (no menu em `sga.py`) captura o resultado usando desempacotamento de variáveis: `sucesso, msg = dados.lancar_nota(...)`. Se `sucesso` for verdadeiro, exibe a mensagem de sucesso; se for falso, exibe a justificativa do erro ocorrido.

### Pergunta 10: Como o sistema calcula a frequência de forma exata? O que acontece se a carga horária for zero?
*   **Resposta**: A frequência é calculada pela função `calcular_frequencia(faltas, total_aulas)` com a fórmula: `((total_aulas - faltas) / total_aulas) * 100`. Para blindar contra o erro de divisão por zero (`ZeroDivisionError`), o código verifica se `total_aulas <= 0`, retornando `100.0` (frequência total padrão) caso ocorra essa situação incoerente. Além disso, limitamos o retorno entre `0.0` e `100.0` usando as funções `max()` e `min()`.
