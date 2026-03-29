import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CAMINHO_ARQUIVO = os.path.join(BASE_DIR, 'tarefas.json')

CAMINHO_ARQUIVO_CONCLUIDO = os.path.join(BASE_DIR,'tarefa_concluida.json')

# abrir arquivo se não existir ele vai criar a lista_tarefas

def carregar_tarefas():
    global lista_tarefas
    global tarefas_concluidas
    try:
        with open(CAMINHO_ARQUIVO, 'r') as openfil:
            lista_tarefas = json.load(openfil)
    except:
        lista_tarefas = []

    try:
        with open(CAMINHO_ARQUIVO_CONCLUIDO, 'r') as openfil:
            tarefas_concluidas = json.load(openfil)
    except:
        tarefas_concluidas = []

# criar tarefa

def criar_tarefa():
    while True:
        nova_tarefa = input('Crie sua tarefa: ').strip()
        lista_tarefas.append(nova_tarefa)
        sair_programa = input('Criar tarefas aperta ( Enter ) ou escreve ( Sair ): ').lower().strip()
        if sair_programa == 'sair':
            return
        
# mostrar tarefas criadas

def tarefas_afazer():
    lista_tarefas.sort()
    print(f'''{10 * '='} Tarefas para fazer {10 * '='}''')
    for id in range(len(lista_tarefas)):
        print(f'''{10 * '='} {lista_tarefas[id]} []''')
    return

def tarefas_feitas():
    tarefas_concluidas.sort()
    print(f'''{10 * '='} Tarefas Feitas {10 * '='}''')
    for id in range(len(tarefas_concluidas)):
        print(f'''{10 * '='} {tarefas_concluidas[id]} [x]''')
    return

def listar_tarefas():
    lista_tarefas.sort()
    print(f'''{10 * '='} Escolha um numero {10 * '='}''')
    for id in range(len(lista_tarefas)):
        print(f'''{10 * '='} [{id + 1}] - {lista_tarefas[id]}[]''')
    return

# editar tarefas

def editar_tarefas():
    opcao_editar = int(input('Qual você quer editar?: ').strip())
    opcao_editar -= 1
    tarefa_antiga = lista_tarefas[opcao_editar]
    lista_tarefas[opcao_editar] = str(input('Edite tarefas: ').strip().lower())
    return print(f'A tarefa [{tarefa_antiga}] foi editada para [{lista_tarefas[opcao_editar]}] com sucesso.')

# deletar tarefas

def deletar_tarefa():
    opcao_editar = int(input('Qual você quer deletar?: ').strip())
    opcao_editar -= 1
    tarefa_deletada = lista_tarefas.pop(opcao_editar)
    return print(f'A tarefa [{tarefa_deletada}] foi deletada com sucesso.')

def marcar_concluido():
    opcao_check = int(input('Escolha para marcar com concluido: ').strip())
    opcao_check -= 1
    tarefas_concluidas.append(lista_tarefas[opcao_check])
    lista_tarefas.pop(opcao_check)
    return print(f'Tarefa [{tarefas_concluidas[opcao_check]}] foi feita com sucesso.')

# guardar as tarefas
def salvar_tarefas():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        json.dump(lista_tarefas,arquivo, indent=4) 

    with open(CAMINHO_ARQUIVO_CONCLUIDO, 'w') as arquivo2:
        json.dump(tarefas_concluidas,arquivo2, indent=4)

    return print('Suas tarefas foram salvas com sucesso.')

# sistema funcionando
def to_do_list():
    print(f'''{10 * '='} To-Do-List {10 * '='}''')
    carregar_tarefas()
    if len(lista_tarefas) >= 1:
        tarefas_afazer()
    if len(tarefas_concluidas) >= 1:
        tarefas_feitas()
    if len(lista_tarefas) == 0:
        criar_tarefa()
        salvar_tarefas()
    while True:
        print(f'''
{10 * '='} [1] - Criar tarefa          {10 * '='}
{10 * '='} [2] - Editar tarefa         {10 * '='}
{10 * '='} [3] - Deletar tarefa        {10 * '='}
{10 * '='} [4] - Ver tarefas           {10 * '='}
{10 * '='} [5] - Marcar como concluido {10 * '='}
{10 * '='} [6] - Sair do programa      {10 * '='}
        ''')
        opcao = int(input('Escolha uma opção: ').strip())
        if opcao == 1:
            criar_tarefa()
            salvar_tarefas()
        elif opcao == 2:
            listar_tarefas()
            editar_tarefas()
            salvar_tarefas()
        elif opcao == 3:
            listar_tarefas()
            deletar_tarefa()
            salvar_tarefas()      
        elif opcao == 4:
            tarefas_afazer()
            tarefas_feitas()
            salvar_tarefas()
        elif opcao == 5:
            listar_tarefas()
            tarefas_feitas()
            marcar_concluido()
            salvar_tarefas()
        else:
            return print('Você saiu do programa!')

to_do_list()