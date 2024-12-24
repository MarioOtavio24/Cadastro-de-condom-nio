import os
os.system('cls')
import colorama
from colorama import Fore, Back, Style
colorama.init()

print(Fore.GREEN + 'Bem vindo à sessão de cadastro! ')
registro_dos_clientes = {}  # Mantenho o dicionário fora do loop para acumular registros

def calcular_imposto(valor):
    """Função para calcular o imposto de renda com base nos valores"""
    if valor < 2000:
        imposto = valor * 0.025  # 2.5%
    elif 2000 <= valor <= 4000:
        imposto = valor * 0.045  # 4.5% para faixa intermediária
    else:
        imposto = valor * 0.055  # 5.5%
    return imposto

while True:
    menu = input(Fore.LIGHTGREEN_EX + '''
        (1) Adicionar alguém ao lote
        (2) Imposto de renda
        (3) Mostrar Perfil
        (4) Sair
        
        ===> ''')

    if menu == '1':
        try:
            Nome = input(Fore.LIGHTGREEN_EX + 'Digite o seu nome: ')
            Idade = int(input(Fore.LIGHTGREEN_EX + 'Digite a sua idade: '))
            if Idade < 18:
                print(Fore.RED + 'Infelizmente menores de 18 anos não podem logar.')
                input(Fore.LIGHTWHITE_EX + 'Pressione enter para voltar ao menu.')
                continue

            Lote = int(input(Fore.LIGHTGREEN_EX + 'Digite o seu lote: '))
            numerodacasa = int(input(Fore.LIGHTGREEN_EX + 'Digite o número da sua casa: '))
            
            # Armazenar dados no dicionário
            registro_dos_clientes[Nome] = {
                'Idade': Idade,
                'Lote': Lote,
                'número da casa': numerodacasa
            }
            print(Fore.LIGHTCYAN_EX + 'Você foi registrado com sucesso!')

        except ValueError:
            print(Fore.LIGHTRED_EX + 'Erro: Nesse campo só pode haver números!')
            input(Fore.LIGHTWHITE_EX + 'Pressione enter para voltar ao menu.')
            continue

    elif menu == '2':
        try:
            renda = float(input(Fore.LIGHTGREEN_EX + 'Digite a sua renda mensal: '))
            if renda < 0:
                print(Fore.LIGHTRED_EX + 'A renda não pode ser negativa.')
                continue

            resultado = calcular_imposto(renda)
            print(Fore.LIGHTCYAN_EX + f'Esse é o imposto que você tem que pagar: R$ {resultado:.2f}')
        
        except ValueError:
            print(Fore.LIGHTRED_EX + 'Erro: Digite um valor numérico válido para a renda!')
            input(Fore.LIGHTWHITE_EX + 'Pressione enter para voltar ao menu.')

    elif menu =='3':
        print('Esses são os morados do condominio!',registro_dos_clientes)
        input(Fore.LIGHTWHITE_EX + 'Pressione enter para voltar ao menu.')
    
    elif menu == '4':
        print(Fore.LIGHTGREEN_EX + 'Saindo do sistema. Até mais!')
        break

    else:
        print(Fore.LIGHTRED_EX + 'Opção inválida! Tente novamente.')
