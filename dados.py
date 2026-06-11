# -*- coding: utf-8 -*-
"""
Módulo de Dados do SGA
Gerencia o armazenamento na memória dos alunos e matérias usando dicionários simples e funções.
"""

# Banco de dados na memória (Dicionários globais do módulo)
# Estrutura do aluno: { "1010": {"matricula": "1010", "nome": "Ana", "notas": {"MAT101": [8.0, 9.0]}} }
alunos = {}

# Estrutura da matéria: { "MAT101": {"codigo": "MAT101", "nome": "Matemática", "pesos": [2.0, 3.0]} }
materias = {}


def cadastrar_aluno(matricula, nome, nivel="Ensino Médio"):
    """
    Cadastra um novo aluno no sistema.
    Retorna (sucesso: bool, mensagem: str)
    """
    matricula = matricula.strip()
    nome = nome.strip()
    nivel = nivel.strip()
    
    if not matricula or not nome:
        return False, "Matrícula e nome do aluno não podem ser vazios."
        
    if matricula in alunos:
        return False, f"O aluno com matrícula '{matricula}' já está cadastrado."
        
    # Salva o aluno como um dicionário simples com suporte a nível, faltas e carga horária
    alunos[matricula] = {
        "matricula": matricula,
        "nome": nome,
        "nivel": nivel,
        "notas": {},    # Chave: codigo_materia -> Valor: lista de notas (floats/None)
        "faltas": {},   # Chave: codigo_materia -> Valor: int (quantidade de faltas, padrão 0)
        "aulas": {}     # Chave: codigo_materia -> Valor: int (total de aulas da disciplina)
    }
    return True, f"Aluno '{nome}' cadastrado com sucesso no {nivel}!"


def cadastrar_materia(codigo, nome, pesos, total_aulas=40):
    """
    Cadastra uma nova matéria no sistema.
    Retorna (sucesso: bool, mensagem: str)
    """
    codigo = codigo.upper().strip()
    nome = nome.strip()
    
    if not codigo or not nome:
        return False, "Código e nome da matéria não podem ser vazios."
        
    if codigo in materias:
        return False, f"A matéria com código '{codigo}' já está cadastrada."
        
    if not pesos:
        return False, "A matéria precisa ter pelo menos uma avaliação/peso definido."
        
    if total_aulas <= 0:
        return False, "O número total de aulas deve ser maior que zero."
        
    # Salva a matéria com a carga horária de aulas
    materias[codigo] = {
        "codigo": codigo,
        "nome": nome,
        "pesos": pesos,
        "total_aulas": total_aulas
    }
    return True, f"Matéria '{nome}' cadastrada com sucesso!"


def inicializar_aluno_materia(matricula, codigo_materia):
    """
    Inicializa as estruturas de notas, faltas e aulas para um aluno em uma matéria específica.
    """
    aluno = alunos[matricula]
    materia = materias[codigo_materia]
    num_avaliacoes = len(materia["pesos"])
    
    if codigo_materia not in aluno["notas"]:
        aluno["notas"][codigo_materia] = [None] * num_avaliacoes
    if codigo_materia not in aluno["faltas"]:
        aluno["faltas"][codigo_materia] = 0
    if codigo_materia not in aluno["aulas"]:
        aluno["aulas"][codigo_materia] = materia["total_aulas"]


def lancar_nota(matricula, codigo_materia, avaliacao_num, nota):
    """
    Lança uma nota para um aluno em uma determinada avaliação de uma matéria.
    Retorna (sucesso: bool, mensagem: str)
    """
    matricula = matricula.strip()
    codigo_materia = codigo_materia.upper().strip()
    
    if matricula not in alunos:
        return False, "Aluno não encontrado no sistema."
        
    if codigo_materia not in materias:
        return False, "Matéria não encontrada no sistema."
        
    aluno = alunos[matricula]
    materia = materias[codigo_materia]
    num_avaliacoes = len(materia["pesos"])
    
    # Validação do número da avaliação (1 a N)
    if avaliacao_num < 1 or avaliacao_num > num_avaliacoes:
        return False, f"Esta matéria tem apenas {num_avaliacoes} avaliações definidas (1 a {num_avaliacoes})."
        
    if nota < 0.0 or nota > 10.0:
        return False, "A nota deve estar entre 0.0 e 10.0."
        
    # Inicializa as estruturas se necessário
    inicializar_aluno_materia(matricula, codigo_materia)
        
    # Lança a nota no índice correto (0 a N-1)
    aluno["notas"][codigo_materia][avaliacao_num - 1] = nota
    return True, f"Nota {nota} lançada para a Avaliação {avaliacao_num} da matéria {materia['nome']}."


def lancar_faltas(matricula, codigo_materia, quantidade_faltas):
    """
    Registra a quantidade de faltas de um aluno em uma determinada matéria.
    Retorna (sucesso: bool, mensagem: str)
    """
    matricula = matricula.strip()
    codigo_materia = codigo_materia.upper().strip()
    
    if matricula not in alunos:
        return False, "Aluno não encontrado no sistema."
        
    if codigo_materia not in materias:
        return False, "Matéria não encontrada no sistema."
        
    aluno = alunos[matricula]
    materia = materias[codigo_materia]
    
    # Inicializa as estruturas se necessário
    inicializar_aluno_materia(matricula, codigo_materia)
    
    total_aulas = aluno["aulas"][codigo_materia]
    
    if quantidade_faltas < 0:
        return False, "A quantidade de faltas não pode ser negativa."
        
    if quantidade_faltas > total_aulas:
        return False, f"A quantidade de faltas ({quantidade_faltas}) não pode ser maior que o total de aulas ({total_aulas}) da matéria."
        
    aluno["faltas"][codigo_materia] = quantidade_faltas
    return True, f"Total de {quantidade_faltas} faltas registrado para a matéria {materia['nome']}."



def obter_aluno(matricula):
    """Retorna o dicionário do aluno ou None se não existir."""
    return alunos.get(matricula.strip())


def obter_materia(codigo):
    """Retorna o dicionário da matéria ou None se não existir."""
    return materias.get(codigo.upper().strip())


def listar_alunos():
    """Retorna uma lista contendo todos os dicionários de alunos."""
    return list(alunos.values())


def listar_materias():
    """Retorna uma lista contendo todos os dicionários de matérias."""
    return list(materias.values())
