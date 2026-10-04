import os
import platform
from veterinaria import Veterinaria

vet = Veterinaria('BOB Veterinária')


def limpar_tela():
    os.system('cls' if platform.system() == 'Windows' else 'clear')


def exibir_nome_do_programa():
    print("""
██████╗░░█████╗░██████╗░
██╔══██╗██╔══██╗██╔══██╗
██████╦╝██║░░██║██████╦╝
██╔══██╗██║░░██║██╔══██╗
██████╦╝╚█████╔╝██████╦╝
╚═════╝░░╚════╝░╚═════╝░

██╗░░██╗███████╗████████╗███████╗██████╗░██╗███╗░░██╗░█████╗░██████╗░██╗░█████╗░
██║░░██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗██║████╗░██║██╔══██╗██╔══██╗██║██╔══██╗
╚██╗██╔╝█████╗░░░░░██║░░░█████╗░░██████╔╝██║██╔██╗██║███████║██████╔╝██║███████║
░╚███╔╝░██╔══╝░░░░░██║░░░██╔══╝░░██╔══██╗██║██║╚████║██╔══██║██╔══██╗██║██╔══██║
░░╚█╔╝░░███████╗░░░██║░░░███████╗██║░░██║██║██║░╚███║██║░░██║██║░░██║██║██║░░██║
░░░╚═╝░░╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚═╝
""")


def exibir_opcoes():
    print('1. Cadastrar paciente')
    print('2. Listar pacientes')
    print('3. Cadastrar responsável')
    print('4. Listar responsáveis')
    print('5. Cadastrar consulta')
    print('6. Listar consultas')
    print('7. Sair\n')


def exibir_subtitulo(texto):
    limpar_tela()
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()


def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()


def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()


def cadastrar_novo_responsavel():
    exibir_subtitulo('Cadastro de novo Responsável')
    nome = input('Digite o nome do responsável: ')
    telefone = input(f'Digite o telefone de {nome}: ')
    email = input('Qual o e-mail?: ')
    endereco = input(f'Qual o endereço de {nome}?: ')
    vet.cadastrar_responsavel(nome, telefone, email, endereco)
    print(f'\nO responsável {nome} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()


def listar_responsaveis():
    exibir_subtitulo('Listando Responsáveis')
    vet.listar_responsaveis()
    voltar_ao_menu_principal()


def cadastrar_novo_paciente():
    exibir_subtitulo('Cadastro de novo Paciente')

    if not vet._responsaveis:
        print('Não há responsáveis cadastrados ainda. Cadastre um responsável primeiro (opção 3).')
        voltar_ao_menu_principal()
        return

    print('Tipo de animal:')
    print('1. Cachorro')
    print('2. Gato')
    tipo_opcao = input('Escolha (1-2): ')
    tipo = 'cachorro' if tipo_opcao == '1' else 'gato'

    nome = input('Digite o nome do paciente: ')
    idade = input(f'Digite a idade de {nome}: ')
    sintomas = input('Quais os sintomas?: ')
    doente = input(f'{nome} está doente? (sim/nao): ')
    alergia = input('O paciente tem alguma alergia? Se sim, qual?: ')
    raca = input('Digite a raça do paciente: ')

    print('\nResponsáveis cadastrados:')
    vet.listar_responsaveis()
    nome_responsavel = input('\nDigite o nome do responsável deste paciente: ')

    if tipo == 'cachorro':
        extra = input('Qual o porte do cachorro (pequeno/médio/grande)?: ')
    else:
        extra = input('O gato é indoor ou outdoor?: ')

    animal = vet.cadastrar_animal(tipo, nome, idade, sintomas, doente, alergia, raca,
                                   nome_responsavel, extra)
    if animal:
        print(f'\nO paciente {nome} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()


def listar_pacientes():
    exibir_subtitulo('Listando Pacientes')
    vet.listar_animais()

    if vet._animais:
        ver_detalhes = input('\nDeseja ver detalhes de algum paciente? (sim/nao): ')
        if ver_detalhes.lower() == 'sim':
            try:
                indice = int(input('Digite o número do paciente: ')) - 1
                vet.exibir_animal(indice)
            except ValueError:
                print('Entrada inválida.')
    voltar_ao_menu_principal()


def cadastrar_nova_consulta():
    exibir_subtitulo('Cadastro de nova Consulta')
    nome = input('Digite o nome/procedimento da consulta: ')
    responsavel_tecnico = input('Digite o nome do veterinário responsável: ')
    valor = input('Digite o valor da consulta: ')
    tempo = input('Digite o tempo estimado: ')
    plano = input('Digite o plano associado (ou "Particular"): ')

    try:
        vet.cadastrar_consulta(nome, responsavel_tecnico, valor, tempo, plano)
        print(f'\nA consulta {nome} foi cadastrada com sucesso!')
    except ValueError:
        print('Valor inválido para a consulta.')
    voltar_ao_menu_principal()


def listar_consultas():
    exibir_subtitulo('Listando Consultas')
    vet.listar_consultas()

    if vet._consultas:
        ver_detalhes = input('\nDeseja verificar o plano de alguma consulta? (sim/nao): ')
        if ver_detalhes.lower() == 'sim':
            try:
                indice = int(input('Digite o número da consulta: ')) - 1
                if 0 <= indice < len(vet._consultas):
                    vet._consultas[indice].exibir_info()
                    opcao = int(input("O cliente possui plano? Digite '1' para sim ou '2' para não: "))
                    vet._consultas[indice].verificar_plano(opcao)
                else:
                    print('Consulta não encontrada.')
            except ValueError:
                print('Entrada inválida.')
    voltar_ao_menu_principal()


def main():
    limpar_tela()
    exibir_nome_do_programa()
    exibir_opcoes()
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        cadastrar_novo_paciente()
    elif opcao == '2':
        listar_pacientes()
    elif opcao == '3':
        cadastrar_novo_responsavel()
    elif opcao == '4':
        listar_responsaveis()
    elif opcao == '5':
        cadastrar_nova_consulta()
    elif opcao == '6':
        listar_consultas()
    elif opcao == '7':
        print('\nAté logo! 🐾')
    else:
        opcao_invalida()


if __name__ == '__main__':
    vet.carregar_dados_exemplo()  # carrega alguns dados de exemplo para já ter o que mostrar
    main()
