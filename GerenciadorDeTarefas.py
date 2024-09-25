import datetime

def exibir_menu():
    print("\nGerenciador de tarefas")
    print("1. Adicionar tarefa")
    print("2. Remover tarefa")
    print("3. Vizualizar tarefas")
    print("4. sair")

def adicionar_tarefa(tarefas):
    tarefa = input("Qual a tarefa para ser adicionada? ")
    tarefa = tarefa.lower()
    tarefas.append(tarefa)
    print(f"Tarefa {tarefa} adicionada, no dia {datetime.datetime.today()} ")

def remover_tarefa (tarefas):
    tarefa = input("\nQual tarefa deseja remover? ")
    tarefa = tarefa.lower()
    if tarefa in tarefas:
        tarefas.remove(tarefa)
        print(f"Tarefa {tarefa} foi removida com sucesso no dia {datetime.datetime.today()}!")
    else:
        print("Tarefa não encontrada")

def vizualizar_tarefa(tarefas):
    if tarefas:
        print("\nTarefas:")

        for tarefa in tarefas:
            print(tarefa)
    else:
        print("Nenhuma tarefa encontrada")

lista_tarefas = []
while True:
    exibir_menu()
    try:
        escolha = int(input("Qual deseja selecionar? "))
    except ValueError:
        print("Opção invalida, tente novamente ")
        continue

    if escolha == 1:
        while True:
            add = adicionar_tarefa(lista_tarefas)
            print("\nDeseja adicionar mais alguma tarefa? ")
            try:
                eco = int(input("1. Sim\n2. Não\n"))
            except ValueError:
                print("Opção invalida, tente novmente")
                continue

            if eco == 1:
                print("Certo, pode adicionar")
            elif eco == 2:
                break
            else:
                print("Opção invalida, tente novamente")

    elif escolha == 2:
        while True:
            print("\nTarefas:")
            for tarefas in lista_tarefas:
                print(tarefas)
                
            remove = remover_tarefa(lista_tarefas)
            print("\nDeseja remover mais alguma tarefa? ")
            try:
                re = int(input("1. Sim\n2. Não\n"))
            except ValueError:
                print("Opção invalida, tente novmente")
                continue

            if re == 1:
                print("Certo, pode adicionar")
            elif re == 2:
                break
            else:
                print("Opção invalida, tente novamente")

    elif escolha == 3:
        vizu = vizualizar_tarefa(lista_tarefas)
    elif escolha == 4:
        print("Saindo do programa")
        break
    else:
        print("Opção invalida, tente novamente")


#projeto feito por kauan victor santos de lima, 25/09/2024