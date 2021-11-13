vetpessoas = []


# vetor de pessoas
def removerpaciente():
    # função para remover os pacientes
    for i in range(len(vetpessoas)):
        print('Há pessoa da posição {}{}{} é {}{}{}'.format('\033[35m', i, '\033[m', '\033[31m', vetpessoas[i],
                                                            '\033[m'))
    try:
        posicao = (int(input('Informe a posição que deseja remover: ')))
        if posicao < len(vetpessoas):
            vetpessoas.pop(posicao)

        else:
            print('       {}Opção invalida{}        '.format('\033[31m', '\033[m'))

    except ValueError:
        limpar()
        print('         {}Somente numeros{}         '.format('\033[31m', '\033[m'))


def atendimento(vetpessoas):
    # função para o atendimento dos pacientes
    print('O paciente: {}{}{} está sendo chamado(a)'.format('\033[34m', vetpessoas[0], '\033[m'))
    vetpessoas.pop(0)


def cadastro():
    # função para cadastrar os pacientes
    vetpessoas.append(str(input('Informe o nome do paciente: ')))


def limpar():
    # função para 'limpar a tela' (15 linhas em branco)
    print("\n" * 20)


while True:
    # menu de escolhas
    print('-=-' * 13)
    print('|         {}1-{} Atendimento               |'.format('\033[36m', '\033[m'))
    print('|         {}2-{} Cadastro                  |'.format('\033[36m', '\033[m'))
    print('|         {}3-{} Remover Usuario           |'.format('\033[36m', '\033[m'))
    print('|         {}4-{} Listagem                  |'.format('\033[36m', '\033[m'))
    print('|         {}5-{} Sair                      |'.format('\033[36m', '\033[m'))
    print('-=-' * 13)
    opcao = str(input('')).strip()
    # variavel para receber a escolha do menu

    if opcao == '1':
        limpar()
        if len(vetpessoas) == 0:
            print('       {}A lista está vazia{}       '.format('\033[31m', '\033[m'))
        else:
            atendimento(vetpessoas)
    # usado para chamar a função de atendimento

    elif opcao == '2':
        limpar()
        cadastro()
        limpar()
    # usado para chamar a função de cadastro

    elif opcao == '3':
        limpar()
        if len(vetpessoas) == 0:
            print('       {}A lista está vazia{}       '.format('\033[31m', '\033[m'))
        else:
            removerpaciente()
    # usado para chamar a função de remover paciente

    elif opcao == '4':
        limpar()
        if len(vetpessoas) == 0:
            print('       {}A lista está vazia{}        '.format('\033[31m', '\033[m'))
        else:
            for i in range(len(vetpessoas)):
                print('{}{}°{} pessoa é {}{}{}'.format('\033[34m', (i + 1), '\033[m', vetpessoas[i],
                                                       '\033[31m', '\033[m'))
    # usado para mostrar a lista

    elif opcao == '5':
        print('{}   Fim do programa!!   {}'.format('\033[92:40m', '\033[m'))
        break
    # usado para fechar o programa

    else:
        limpar()
        print('           {}Opção invalida{}          '.format('\033[31m', '\033[m'))
        # caso a opção informada não seja correspondente, retorna opção invalida
        