# -*- coding: utf-8 -*-
"""
Módulo de Cálculos Matemáticos do SGA
Contém funções auxiliares de cálculos acadêmicos (Ex: Média Ponderada).
"""

def calcular_media_ponderada(notas, pesos):
    """
    Calcula a média ponderada das notas fornecidas com base em seus pesos correspondentes.
    Ignora as posições onde a nota é None (não lançada ainda).
    
    Exemplo:
        notas = [8.0, 9.0]
        pesos = [2.0, 3.0]
        Retorna: ((8 * 2) + (9 * 3)) / 5 = (16 + 27) / 5 = 43 / 5 = 8.6
    """
    soma_ponderada = 0.0
    soma_pesos = 0.0
    
    for i in range(len(pesos)):
        # Garante que não vamos acessar um índice de notas inexistente
        if i >= len(notas):
            break
            
        nota = notas[i]
        if nota is not None:
            soma_ponderada += nota * pesos[i]
            soma_pesos += pesos[i]
            
    if soma_pesos == 0.0:
        return 0.0
        
    return soma_ponderada / soma_pesos


def calcular_frequencia(faltas, total_aulas):
    """
    Calcula o percentual de frequência com base nas faltas e no total de aulas.
    Retorna um valor float entre 0.0 e 100.0.
    """
    if total_aulas <= 0:
        return 100.0
    frequencia = ((total_aulas - faltas) / total_aulas) * 100.0
    return max(0.0, min(100.0, frequencia))


def determinar_situacao(media, frequencia, nota_minima=6.0):
    """
    Determina a situação final do estudante com base na média final, frequência e a nota mínima exigida.
    
    Situações possíveis:
    - 'Aprovado': média >= nota_minima e frequência >= 75%
    - 'Reprovado por nota': média < nota_minima e frequência >= 75%
    - 'Reprovado por falta': frequência < 75% (independente da nota)
    """
    if frequencia < 75.0:
        return "Reprovado por falta"
    elif media < nota_minima:
        return "Reprovado por nota"
    else:
        return "Aprovado"

