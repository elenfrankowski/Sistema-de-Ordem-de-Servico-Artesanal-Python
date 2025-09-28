materiais = []
ordens_servico = []

"""
Primeira Parte: Cadastro de Materiais
"""

def cadastrar_material():
    print("\n---Cadastro de Material---")
    nome = input("Nome do material: ")
    unidade = input("Unidade de medida (ex: g, m, un, ml): ")
    qtd_total = float(input(f"Quantidade total comprada ({unidade}): "))
    valor_total = float(input("Valor total pago por essa quantidade (R$): "))

    valor_unitario = valor_total / qtd_total

    material = {
        "nome": nome,
        "unidade": unidade,
        "qtd_total": qtd_total,
        "valor_total": valor_total,
        "valor_unitario": valor_unitario
    }

    materiais.append(material)
    print(f"Material '{nome}' cadastrado com sucesso!")
    print(f"Valor unitário calculado: R${valor_unitario:.4f} por {unidade}.")

#Listagem dos Materiais
def listar_materiais():
    print("\n---Lista de Materiais Cadastrados---")
    if not materiais:
        print("Nenhum material cadastrado ainda.")
    else:
        for i, mat in enumerate(materiais, start=1): #associa a cada item um índice numérico
            print(f"{i}. {mat['nome']} - R${mat['valor_unitario']:.4f} por {mat['unidade']}")
            print("-------------------------------------------------")

"""
Terceira Parte 1: Remover Material
"""
#Remover Materiais
def remover_material():
    print("\n---Remover Material---")
    if not materiais:
        print("Não há material para remover.")
        return
    
    while True:
        for i, mat in enumerate(materiais, start=1): 
            print(f"{i}. {mat['nome']} - R${mat['valor_unitario']:.4f} por {mat['unidade']}")
            print("-------------------------------------------------")

        escolha = input("\nDigite o número do material que deseja remover ou pressione ENTER para encerrar: ")
        if escolha == "":
            break

        if not escolha.isdigit():
            print("Entrada inválida.")
            return
        
        indice = int(escolha) - 1 #ajustar a contagem dos índices da lista
        if 0 <= indice < len(materiais):
            material_removido = materiais.pop(indice)
            print(f"Material '{material_removido['nome']}' foi removido com sucesso!")
            break
        else:
            print("Índice inválido")

"""
Segunda Parte: Ordem de Serviço
"""

def criar_ordem_servico():
    print("\n---Nova Ordem de Serviço---")
    cliente = input("Nome do cliente: ")
    peca = input("Nome da peça: ")

    materiais_usados = []
    if not materiais:
        print("Nenhum material cadastrado ainda.")
        return
    
    while True:
        print("\nEscolha os materiais usados: ")
        for i, mat in enumerate(materiais):
            print(f"{i+1}. {mat['nome']} - R${mat['valor_unitario']:.4f} por {mat['unidade']}")

        escolha = input("\nNúmero do material (ou ENTER para encerrar): ")
        if escolha == "":
            break
        indice = int(escolha) - 1
        if 0 <= indice < len(materiais):
            material = materiais[indice]
            unidade = material['unidade']
            qtd_usada = float(input(f"Quantidade usada de '{material['nome']}' ({unidade}): "))
            custo = qtd_usada * material['valor_unitario']
            materiais_usados.append({
                "nome": material['nome'],
                "quantidade_usada": qtd_usada,
                "unidade": unidade,
                "custo": custo
            })
            #Mostrar a lista parcial dos materiais usados até agora
            print("\nMateriais adicionados até agora: ")
            for item in materiais_usados:
                print(f".{item['nome']}: {item['quantidade_usada']} {item['unidade']} - R${item['custo']:.2f}")
                print("-------------------------------------------------")
        else:
            print("Número Inválido")
    
    tempo = float(input("\nTempo de produção (em horas): "))
    valor_hora = float(input("Valor da sua hora de trabalho (R$): "))
    lucro_percentual = float(input("Margem de lucro desejada (%): "))

    custo_materiais = sum(item['custo'] for item in materiais_usados)
    custo_tempo = tempo * valor_hora
    custo_total = custo_materiais + custo_tempo
    valor_venda = custo_total * (1 + lucro_percentual / 100)

    ordem = {
        "cliente": cliente,
        "peca": peca,
        "materiais_usados": materiais_usados,
        "tempo_producao": tempo,
        "valor_hora": valor_hora,
        "lucro_percentual": lucro_percentual,
        "valor_total": valor_venda,
        "status": "Em andamento"
    }

    ordens_servico.append(ordem)
    print(f"\nOrdem criada com sucesso! Valor sugerido de venda: R${valor_venda:.2f}")

def listar_ordens():
    print("\n---Ordens de Serviço---")
    if not ordens_servico:
        print("Nenhuma ordem cadastrada ainda.")
    else:
        for i, ordem in enumerate(ordens_servico, start=1):
            print(f"{i}. Cliente: {ordem['cliente']} | Peça: {ordem['peca']} | Valor: R${ordem['valor_total']:.2f} | Status: {ordem['status']}")
            print("--------------------------------------------------------------------------------------------------")

"""
Terceira Parte 2: Remover Ordem de Serviço
"""
#Remover Ordem de Serviço
def remover_ordem():
    print("\n---Remover Ordem de Serviço---")
    if not ordens_servico:
        print("Não há uma ordem de serviço para remover.")
        return
    
    while True:
        for i, ordem in enumerate(ordens_servico, start=1):
            print(f"{i}. Cliente: {ordem['cliente']} | Peça: {ordem['peca']} | Valor: R${ordem['valor_total']:.2f} | Status: {ordem['status']}")
            print("--------------------------------------------------------------------------------------------------")

        escolha = input("\nDigite o número da ordem que deseja remover ou pressione ENTER para encerrar: ")
        if escolha == "":
            break

        if not escolha.isdigit():
            print("Entrada inválida.")
            return
        
        indice = int(escolha) - 1
        if 0 <= indice < len(ordens_servico):
            ordem_removida = ordens_servico.pop(indice)
            print(f"Ordem '{ordem_removida['cliente']}' foi removida com sucesso!")
            break
        else:
            print("Índice inválido")

"""
Quarta Parte: Atualização do Status
"""

def atualizar_status_ordem():
    print("\n---Atualizar Status da Ordem de Serviço---")
    if not ordens_servico:
        print("Nenhuma ordem de serviço cadastrada ainda.")
        return

    for i, ordem in enumerate(ordens_servico, start=1):
        print(f"{i}. Cliente: {ordem['cliente']} | Peça: {ordem['peca']} | Status atual: {ordem['status']}")

    escolha = input("Digite o número da ordem que deseja atualizar: ")
    if not escolha.isdigit():
        print("Entrada inválida.")
        return
    
    indice = int(escolha) - 1 
    if 0 <= indice < len(ordens_servico):
        nova = input("Novo status (Em andamento / Concluído / Cancelado): ").strip().capitalize() #strip remove os espaços, capitalize deixa o primeiro caracter em maiúsculo e o restante minúsculo
        if nova not in ["Em andamento", "Concluído", "Cancelado"]:
            print("Status inválido. Não foi atualizado.")
        else:
            ordens_servico[indice]['status'] = nova
            print(f"Status atualizado para '{nova}' com sucesso!")
    else:
        print("Número de ordem inválido.")

#Menu Principal
while True:
    print("\n---MENU---")
    print("1. Cadastrar Material")
    print("2. Listar Materiais")
    print("3. Remover Material")
    print("4. Criar Nova Ordem de Serviço")
    print("5. Listar Ordens de Serviço")
    print("6. Remover Ordem de Serviço")
    print("7. Atualizar Status da Ordem de Serviço")
    print("8. Sair")

    opcao = input("Selecione uma opção: ")

    if opcao == '1':
        cadastrar_material()
    elif opcao == '2':
        listar_materiais()
    elif opcao == '3':
        remover_material()
    elif opcao == '4':
        criar_ordem_servico()
    elif opcao == '5':
        listar_ordens()
    elif opcao == '6':
        remover_ordem()
    elif opcao == '7':
        atualizar_status_ordem()
    elif opcao == '8':
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Tente Novamente")