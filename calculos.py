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
