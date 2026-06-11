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
    print("                 (ENSINO MÉDIO)")
    print("="*50)
    print("1. Cadastrar Aluno")
    print("2. Cadastrar Matéria")
    print("3. Lançar Nota de Aluno")
    print("4. Lançar Falta de Aluno")
    print("5. Gerar Relatório Final do Aluno (LDB)")
    print("6. Listar Todos os Alunos")
    print("7. Listar Todas as Matérias")
    print("0. Sair")
    print("="*50)

def main():
    # Cadastrar matérias com carga horária de aulas (Ensino Médio)
    dados.cadastrar_materia("MAT", "Matemática", [3.0, 3.0, 4.0], 80) # 80 aulas
    dados.cadastrar_materia("PORT", "Português", [4.0, 6.0], 80)      # 80 aulas
    dados.cadastrar_materia("GEO", "Geografia", [5.0, 5.0], 40)       # 40 aulas
    dados.cadastrar_materia("FIS", "Física", [3.0, 3.0, 4.0], 80)      # 80 aulas
    dados.cadastrar_materia("QUI", "Química", [5.0, 5.0], 40)         # 40 aulas
    dados.cadastrar_materia("BIO", "Biologia", [5.0, 5.0], 40)        # 40 aulas
    dados.cadastrar_materia("HIST", "História", [5.0, 5.0], 40)       # 40 aulas
    
    # Cadastrar alunos no Ensino Médio
    dados.cadastrar_aluno("1010", "Ana Silva", "Ensino Médio")
    dados.cadastrar_aluno("2020", "Bruno Costa", "Ensino Médio")
    dados.cadastrar_aluno("3030", "Carla Dias", "Ensino Médio") # Exemplo para reprovar por falta
    
    # Inicializar matérias para os alunos pré-carregados
    for cod in ["MAT", "PORT", "GEO"]:
        dados.inicializar_aluno_materia("1010", cod)
        dados.inicializar_aluno_materia("2020", cod)
        dados.inicializar_aluno_materia("3030", cod)

    # Notas e Faltas da Ana (Situação: Aprovada)
    dados.lancar_nota("1010", "MAT", 1, 8.0)
    dados.lancar_nota("1010", "MAT", 2, 7.5)
    dados.lancar_nota("1010", "MAT", 3, 9.0)
    dados.lancar_faltas("1010", "MAT", 4) # Freq: 95%
    
    dados.lancar_nota("1010", "PORT", 1, 7.0)
    dados.lancar_nota("1010", "PORT", 2, 8.5)
    dados.lancar_faltas("1010", "PORT", 6) # Freq: 92.5%
    
    dados.lancar_nota("1010", "GEO", 1, 9.0)
    dados.lancar_nota("1010", "GEO", 2, 8.0)
    dados.lancar_faltas("1010", "GEO", 2) # Freq: 95%
    
    # Notas e Faltas do Bruno (Situação: Reprovado por Nota)
    dados.lancar_nota("2020", "MAT", 1, 5.0)
    dados.lancar_nota("2020", "MAT", 2, 5.5)
    dados.lancar_nota("2020", "MAT", 3, 6.0) # Média: 5.55
    dados.lancar_faltas("2020", "MAT", 8) # Freq: 90%
    
    dados.lancar_nota("2020", "PORT", 1, 8.0)
    dados.lancar_nota("2020", "PORT", 2, 7.5)
    dados.lancar_faltas("2020", "PORT", 10) # Freq: 87.5%
    
    dados.lancar_nota("2020", "GEO", 1, 8.0)
    dados.lancar_nota("2020", "GEO", 2, 7.0)
    dados.lancar_faltas("2020", "GEO", 4) # Freq: 90%

    # Notas e Faltas da Carla (Situação: Reprovada por Falta)
    dados.lancar_nota("3030", "MAT", 1, 8.0)
    dados.lancar_nota("3030", "MAT", 2, 9.0)
    dados.lancar_nota("3030", "MAT", 3, 8.5)
    dados.lancar_faltas("3030", "MAT", 25) # Freq: 68.75% (< 75%)
    
    dados.lancar_nota("3030", "PORT", 1, 8.0)
    dados.lancar_nota("3030", "PORT", 2, 8.0)
    dados.lancar_faltas("3030", "PORT", 5) # Freq: 93.75%

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("\n--- Cadastro de Aluno ---")
            matricula = input("Digite a matrícula do aluno: ").strip()
            nome = input("Digite o nome completo do aluno: ").strip()
            # Cadastrado por padrão no Ensino Médio
            sucesso, msg = dados.cadastrar_aluno(matricula, nome, "Ensino Médio")
            print(f"\n>>> {msg}")
            
            # Pré-vincula disciplinas básicas para agilizar o uso
            if sucesso:
                pre_vincular = input("Deseja pré-vincular as matérias recomendadas do Ensino Médio? (S/N) [S]: ").strip().upper()
                if pre_vincular != "N":
                    for cod in ["MAT", "PORT", "GEO", "FIS", "QUI", "BIO", "HIST"]:
                        if dados.obter_materia(cod):
                            dados.inicializar_aluno_materia(matricula, cod)
                    print(">>> Matérias recomendadas vinculadas com sucesso!")

        elif opcao == "2":
            print("\n--- Cadastro de Matéria ---")
            codigo = input("Digite o código da matéria (ex: MAT): ").upper().strip()
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
                
            total_aulas = ler_int("Qual o total de aulas previstas para esta matéria? (Padrão: 80): ")
            if total_aulas <= 0:
                total_aulas = 80
                
            sucesso, msg = dados.cadastrar_materia(codigo, nome, pesos, total_aulas)
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

            dados.inicializar_aluno_materia(matricula, codigo_materia)
            print(f"\nMatéria selecionada: {materia['nome']}")
            print(f"Essa matéria possui {len(materia['pesos'])} avaliações com pesos: {materia['pesos']}")
            
            avaliacao_num = ler_int(f"Digite o número da avaliação para lançar nota (1 a {len(materia['pesos'])}): ")
            nota = ler_float("Digite a nota (0.0 a 10.0): ")
            
            sucesso, msg = dados.lancar_nota(matricula, codigo_materia, avaliacao_num, nota)
            print(f"\n>>> {msg}")

        elif opcao == "4":
            print("\n--- Lançamento de Faltas ---")
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

            dados.inicializar_aluno_materia(matricula, codigo_materia)
            total_aulas = aluno["aulas"][codigo_materia]
            faltas_atuais = aluno["faltas"].get(codigo_materia, 0)
            
            print(f"\nMatéria: {materia['nome']}")
            print(f"Carga Horária (Aulas): {total_aulas} | Faltas atuais: {faltas_atuais}")
            
            faltas = ler_int(f"Digite o novo total de faltas (0 a {total_aulas}): ")
            sucesso, msg = dados.lancar_faltas(matricula, codigo_materia, faltas)
            print(f"\n>>> {msg}")

        elif opcao == "5":
            print("\n--- Relatório Final de Desempenho (LDB) ---")
            matricula = input("Digite a matrícula do aluno: ").strip()
            aluno = dados.obter_aluno(matricula)
            if not aluno:
                print(">>> Aluno não cadastrado!")
                continue
            
            print("\n" + "="*65)
            print("                 RELATÓRIO ACADÊMICO FINAL")
            print("                 (DIRETRIZES LDB - 75% FREQ)")
            print("="*65)
            print(f"Aluno: {aluno['nome'].upper()}")
            print(f"Matrícula: {aluno['matricula']}")
            print(f"Nível de Ensino: {aluno.get('nivel', 'Ensino Médio')}")
            print("-" * 65)
            
            nota_minima = 6.0  # Nota mínima de aprovação padrão
            print(f"Critérios: Nota Mínima: {nota_minima:.1f} | Frequência Mínima: 75%")
            print("-" * 65)
            
            if not aluno["notas"]:
                print("Nenhuma nota ou frequência registrada para este aluno ainda.")
            else:
                total_aulas_geral = 0
                total_faltas_geral = 0
                soma_medias = 0.0
                num_materias = 0
                algum_reprovado_por_nota = False
                algum_reprovado_por_falta = False
                
                # Cabeçalho formatado
                print(f"{'DISCIPLINA':<15} | {'MÉDIA':<6} | {'FALTAS':<8} | {'FREQ %':<8} | {'SITUAÇÃO':<20}")
                print("-" * 65)
                
                for cod_materia, lista_notas in aluno["notas"].items():
                    materia = dados.obter_materia(cod_materia)
                    if not materia:
                        continue
                    
                    media = calculos.calcular_media_ponderada(lista_notas, materia["pesos"])
                    faltas = aluno["faltas"].get(cod_materia, 0)
                    aulas = aluno["aulas"].get(cod_materia, materia["total_aulas"])
                    
                    freq = calculos.calcular_frequencia(faltas, aulas)
                    situacao_disc = calculos.determinar_situacao(media, freq, nota_minima)
                    
                    if situacao_disc == "Reprovado por falta":
                        algum_reprovado_por_falta = True
                    elif situacao_disc == "Reprovado por nota":
                        algum_reprovado_por_nota = True
                        
                    total_aulas_geral += aulas
                    total_faltas_geral += faltas
                    soma_medias += media
                    num_materias += 1
                    
                    print(f"{materia['nome']:<15} | {media:<6.2f} | {faltas:<2}/{aulas:<5} | {freq:<7.1f}% | {situacao_disc:<20}")
                
                print("-" * 65)
                
                # Resumo Geral do Aluno
                freq_geral = calculos.calcular_frequencia(total_faltas_geral, total_aulas_geral)
                media_geral = soma_medias / num_materias if num_materias > 0 else 0.0
                
                # Regras gerais de aprovação
                if freq_geral < 75.0 or algum_reprovado_por_falta:
                    situacao_geral = "Reprovado por falta"
                elif algum_reprovado_por_nota:
                    situacao_geral = "Reprovado por nota"
                else:
                    situacao_geral = "Aprovado"
                    
                print("RESUMO GERAL DO DESEMPENHO:")
                print(f"  Média Geral das Disciplinas: {media_geral:.2f}")
                print(f"  Total de Faltas Acumuladas: {total_faltas_geral} faltas em {total_aulas_geral} aulas")
                print(f"  Frequência Geral do Aluno:  {freq_geral:.2f}%")
                print("\n" + "*"*40)
                print(f"  SITUAÇÃO GERAL: {situacao_geral.upper()}")
                print("*"*40)
            print("="*65)

        elif opcao == "6":
            print("\n--- Lista de Alunos ---")
            lista_alunos = dados.listar_alunos()
            if not lista_alunos:
                print("Nenhum aluno cadastrado.")
            else:
                for aluno in lista_alunos:
                    print(f"Matrícula: {aluno['matricula']} | Nome: {aluno['nome']} | Nível: {aluno.get('nivel', 'Ensino Médio')}")

        elif opcao == "7":
            print("\n--- Lista de Matérias ---")
            lista_materias = dados.listar_materias()
            if not lista_materias:
                print("Nenhuma matéria cadastrada.")
            else:
                for materia in lista_materias:
                    pesos_str = ", ".join(str(p) for p in materia["pesos"])
                    print(f"Código: {materia['codigo']} | Nome: {materia['nome']} | Pesos: [{pesos_str}] | Aulas: {materia.get('total_aulas', 40)}")

        elif opcao == "0":
            print("\nEncerrando o SGA. Obrigado por usar!")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
