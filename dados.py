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


def cadastrar_aluno(matricula, nome):
    """
    Cadastra um novo aluno no sistema.
    Retorna (sucesso: bool, mensagem: str)
    """
    matricula = matricula.strip()
    nome = nome.strip()
    
    if not matricula or not nome:
        return False, "Matrícula e nome do aluno não podem ser vazios."
        
    if matricula in alunos:
        return False, f"O aluno com matrícula '{matricula}' já está cadastrado."
        
    # Salva o aluno como um dicionário simples
    alunos[matricula] = {
        "matricula": matricula,
        "nome": nome,
        "notas": {}  # Chave: codigo_materia -> Valor: lista de notas (floats/None)
    }
    return True, f"Aluno '{nome}' cadastrado com sucesso!"


def cadastrar_materia(codigo, nome, pesos):
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
        
    # Salva a matéria como um dicionário simples
    materias[codigo] = {
        "codigo": codigo,
        "nome": nome,
        "pesos": pesos
    }
    return True, f"Matéria '{nome}' cadastrada com sucesso!"


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
        
    # Inicializa a lista de notas com None se o aluno ainda não possuir notas nessa matéria
    if codigo_materia not in aluno["notas"]:
        aluno["notas"][codigo_materia] = [None] * num_avaliacoes
        
    # Lança a nota no índice correto (0 a N-1)
    aluno["notas"][codigo_materia][avaliacao_num - 1] = nota
    return True, f"Nota {nota} lançada para a Avaliação {avaliacao_num} da matéria {materia['nome']}."


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
