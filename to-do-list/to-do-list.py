# criar tarefa

lista_tarefas = []

def criar_tarefa():
    tarefas = []
    while True:
        nova_tarefa = input('Crie sua tarefa: ').strip()
        tarefas.append(nova_tarefa)
        sair_programa = input('Criar tarefas aperta ( Enter ) ou escreve ( Sair ): ').lower().strip()
        if sair_programa == 'sair':
            lista_tarefas.extend(tarefas)
            return

# listar tarefa

def listar_tarefas():
    lista_tarefas.sort()
    print(f'''{10 * '='} Escolha um numero para editar ou deletar {10 * '='}''')
    for id in range(len(lista_tarefas)):
        print(f'''{10 * '='} [{id + 1}] - {lista_tarefas[id]}[]''')
    return

# tarefas para fazer

def tarefas_afazer():
    lista_tarefas.sort()
    print(f'''{10 * '='} Tarefas para fazer {10 * '='}''')
    for id in range(len(lista_tarefas)):
        print(f'''{10 * '='} {lista_tarefas[id]} []''')
    return

# editar tarefa

def editar_tarefas():
    opcao_editar = int(input('Qual você quer editar?: ').strip())
    opcao_editar -= 1
    tarefa_antiga = lista_tarefas[opcao_editar]
    lista_tarefas[opcao_editar] = str(input('Edite tarefas: ').strip().lower())
    return print(f'A tarefa [{tarefa_antiga}] foi editada para [{lista_tarefas[opcao_editar]}] com sucesso.')

# deletar tarefa

def deletar_tarefa():
    opcao_editar = int(input('Qual voce quer deletar?: ').strip())
    opcao_editar -= 1
    tarefa_deletada = lista_tarefas.pop(opcao_editar)
    return print(f'A tarefa [{tarefa_deletada}] foi deletada com sucesso.')

# sistema_to_do_list

def sistema_to_do_list():
    print(f'''{10 * '='} To-Do-List {10 * '='}''')
    criar_tarefa()
    tarefas_afazer()
    while True:
        print(f'''
{10 * '='} [1] - Criar tarefa     {10 * '='}
{10 * '='} [2] - Editar tarefa    {10 * '='}
{10 * '='} [3] - Deletar tarefa   {10 * '='}
{10 * '='} [4] - Sair do programa {10 * '='}
        ''')
        opcao = int(input('Digite uma opção: ').strip())
        if opcao == 1:
            tarefas_afazer()
            criar_tarefa()
        elif opcao == 2:
            listar_tarefas()
            editar_tarefas()
        elif opcao == 3:
            listar_tarefas()
            deletar_tarefa()
        else:
            return print('Você saiu do programa!')
    
sistema_to_do_list()