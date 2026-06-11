# -*- coding: utf-8 -*-
"""
SGA - Sistema de Gerenciamento Acadêmico
Arquivo principal (CLI) integrado com dados.py e calculos.py.
Sem o uso de classes.
"""

import dados
import calculos

# --- Funções de Leitura e Interface ---

def ler_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Digite um número decimal (ex: 7.5).")

def ler_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def exibir_menu():
    print("\n" + "="*50)
    print("      SGA - SISTEMA DE GERENCIAMENTO ACADÊMICO")
    print("="*50)
    print("1. Cadastrar Aluno")
    print("2. Cadastrar Matéria")
    print("3. Lançar Nota de Aluno")
    print("4. Exibir Boletim do Aluno (com Média Ponderada)")
    print("5. Listar Todos os Alunos")
    print("6. Listar Todas as Matérias")
    print("0. Sair")
    print("="*50)

def main():
    # Cadastrar dados fictícios (Ensino Médio) para facilitar os testes iniciais
    dados.cadastrar_materia("MAT", "Matemática", [3.0, 3.0, 4.0]) # 3 avaliações, pesos 3, 3 e 4
    dados.cadastrar_materia("PORT", "Português", [4.0, 6.0])      # 2 avaliações, pesos 4 e 6
    dados.cadastrar_materia("GEO", "Geografia", [5.0, 5.0])       # 2 avaliações, pesos 5 e 5
    
    dados.cadastrar_aluno("1010", "Ana Silva")
    dados.cadastrar_aluno("2020", "Bruno Costa")
    
    # Notas da Ana
    dados.lancar_nota("1010", "MAT", 1, 8.0)
    dados.lancar_nota("1010", "MAT", 2, 7.5)
    dados.lancar_nota("1010", "MAT", 3, 9.0)
    dados.lancar_nota("1010", "PORT", 1, 7.0)
    dados.lancar_nota("1010", "PORT", 2, 8.5)
    
    # Notas do Bruno
    dados.lancar_nota("2020", "MAT", 1, 6.0)
    dados.lancar_nota("2020", "MAT", 2, 5.5)
    dados.lancar_nota("2020", "MAT", 3, 7.0)
    dados.lancar_nota("2020", "GEO", 1, 8.0)
    dados.lancar_nota("2020", "GEO", 2, 6.5)

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("\n--- Cadastro de Aluno ---")
            matricula = input("Digite a matrícula do aluno: ").strip()
            nome = input("Digite o nome completo do aluno: ").strip()
            sucesso, msg = dados.cadastrar_aluno(matricula, nome)
            print(f"\n>>> {msg}")

        elif opcao == "2":
            print("\n--- Cadastro de Matéria ---")
            codigo = input("Digite o código da matéria (ex: MAT101): ").strip()
            nome = input("Digite o nome da matéria: ").strip()
            
            num_avaliacoes = ler_int("Quantas avaliações esta matéria possui? ")
            while num_avaliacoes <= 0:
                print("A matéria deve ter no mínimo 1 avaliação.")
                num_avaliacoes = ler_int("Quantas avaliações esta matéria possui? ")
            
            pesos = []
            print("Digite o peso de cada avaliação:")
            for i in range(1, num_avaliacoes + 1):
                peso = ler_float(f"  Peso da Avaliação {i}: ")
                while peso <= 0:
                    print("O peso deve ser maior que zero.")
                    peso = ler_float(f"  Peso da Avaliação {i}: ")
                pesos.append(peso)
                
            sucesso, msg = dados.cadastrar_materia(codigo, nome, pesos)
            print(f"\n>>> {msg}")

        elif opcao == "3":
            print("\n--- Lançamento de Notas ---")
            lista_alunos = dados.listar_alunos()
            lista_materias = dados.listar_materias()
            
            if not lista_alunos:
                print("Nenhum aluno cadastrado no sistema.")
                continue
            if not lista_materias:
                print("Nenhuma matéria cadastrada no sistema.")
                continue

            matricula = input("Digite a matrícula do aluno: ").strip()
            aluno = dados.obter_aluno(matricula)
            if not aluno:
                print(">>> Aluno não encontrado!")
                continue

            codigo_materia = input("Digite o código da matéria: ").upper().strip()
            materia = dados.obter_materia(codigo_materia)
            if not materia:
                print(">>> Matéria não encontrada!")
                continue

            print(f"\nMatéria selecionada: {materia['nome']}")
            print(f"Essa matéria possui {len(materia['pesos'])} avaliações com pesos: {materia['pesos']}")
            
            avaliacao_num = ler_int(f"Digite o número da avaliação para lançar nota (1 a {len(materia['pesos'])}): ")
            nota = ler_float("Digite a nota (0.0 a 10.0): ")
            
            sucesso, msg = dados.lancar_nota(matricula, codigo_materia, avaliacao_num, nota)
            print(f"\n>>> {msg}")

        elif opcao == "4":
            print("\n--- Boletim Escolar ---")
            matricula = input("Digite a matrícula do aluno: ").strip()
            aluno = dados.obter_aluno(matricula)
            if not aluno:
                print(">>> Aluno não cadastrado!")
                continue
            
            print(f"\nAluno: {aluno['nome']} | Matrícula: {aluno['matricula']}")
            print("-" * 50)
            
            if not aluno["notas"]:
                print("Nenhuma nota lançada para este aluno ainda.")
            else:
                for cod_materia, lista_notas in aluno["notas"].items():
                    materia = dados.obter_materia(cod_materia)
                    # Calcula a média usando a função importada do calculos.py
                    media = calculos.calcular_media_ponderada(lista_notas, materia["pesos"])
                    
                    print(f"Matéria: {materia['nome']} ({cod_materia})")
                    notas_str = []
                    for idx, nota in enumerate(lista_notas):
                        peso = materia["pesos"][idx]
                        if nota is None:
                            notas_str.append(f"Av{idx+1} (Peso {peso}): Pendente")
                        else:
                            notas_str.append(f"Av{idx+1} (Peso {peso}): {nota:.1f}")
                    
                    print("  Notas: " + " | ".join(notas_str))
                    print(f"  Média Ponderada Final: {media:.2f}")
                    print("-" * 50)

        elif opcao == "5":
            print("\n--- Lista de Alunos ---")
            lista_alunos = dados.listar_alunos()
            if not lista_alunos:
                print("Nenhum aluno cadastrado.")
            else:
                for aluno in lista_alunos:
                    print(f"Matrícula: {aluno['matricula']} | Nome: {aluno['nome']}")

        elif opcao == "6":
            print("\n--- Lista de Matérias ---")
            lista_materias = dados.listar_materias()
            if not lista_materias:
                print("Nenhuma matéria cadastrada.")
            else:
                for materia in lista_materias:
                    pesos_str = ", ".join(str(p) for p in materia["pesos"])
                    print(f"Código: {materia['codigo']} | Nome: {materia['nome']} | Pesos: [{pesos_str}]")

        elif opcao == "0":
            print("\nEncerrando o SGA. Obrigado por usar!")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
