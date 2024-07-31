autores = [{'nome': 'Machado de Assis', 'codigo': '1'}]
#{'nome': nome, 'codigo': codigo}
livros = [{'titulo': 'Dom casmurro', 'ano': '1985', 'codigo_autor': '1'}]
#{'titulo': titulo, 'ano': ano, 'codigo_autor': codigo_autor}

import os
import time

def clear():
    os.system('cls')


def cadastrar_autor():
    clear()
    print('===== Cadastro de Autor(a) =====')
    nome = input('\nDigite o nome do(a) autor(a): ')
    codigo = input('Digite o código do autor: ')
    
    for autor in autores:
        if autor['codigo'] == codigo:
            opcao = input(f'Já existe um autor registrado com esse código. Próximo código disponível: [{len(autores) + 1}] \n[1] Para tentar novamente ou [2] para voltar para o Menu: ')
            if opcao == '1':
                cadastrar_autor()
                return
            elif opcao == '2':
                clear()
                print('Voltando para o menu...')
                time.sleep(2)
                clear()
                return
            else: 
                print('Opção inválida.')
                time.sleep(2)
                clear()
                return
    
    autores.append({'nome': nome, 'codigo': codigo})
    clear()
    print(f'Autor(a) {nome} cadastrado com sucesso.')
    time.sleep(2)
    clear()


def cadastrar_livro():
    clear()
    print('===== Cadastro de Livros =====')
    titulo = input('\nDigite o título do livro: ')
    ano = int(input('Digite o ano de publicação do livro: '))
    codigo_autor = input('Digite o código do autor do livro: ')
    autor_existe = False

    for autor in autores:
        if autor['codigo'] == codigo_autor:
            autor_existe = True
            break
    if not autor_existe:
        print('Autor ainda não cadastrado.')
        time.sleep(2)
        clear()
        return

    for livro in livros:
        if livro['titulo'].lower() == titulo.lower() and livro['codigo_autor'] == codigo_autor:
            opcao = input('Este livro já foi cadastrado anteriormente. \n[1] Para tentar novamente ou [2] para voltar para o Menu: ')
            if opcao == '1':
                cadastrar_livro()
                return
            elif opcao == '2':
                clear()
                print('Voltando para o menu...')
                time.sleep(2)
                clear()
                return
            else:
                print('Opção inválida.')
                time.sleep(2)
                clear()
                return
    
    livros.append({'titulo': titulo, 'ano': ano, 'codigo_autor': codigo_autor})
    clear()
    print('Cadastrando livro...')
    time.sleep(1)
    clear()
    print(f'Livro {titulo} adicionado com sucesso.')
    time.sleep(2)
    clear()

def listar_autores():
    clear()
    print('===== Listar Autores =====')
    if autores:
        for autor in autores:
            print(f'Código: {autor["codigo"]}, Nome: {autor["nome"]}')
        
        if len(autores) != 0:
            print('\nPróximo código disponível: ', len(autores) + 1)
        time.sleep(2)
            
    else:
        print('Nenhum autor cadastrado. Código para cadastro do primeiro autor: [1]')
        


def listar_livros():
    clear()
    print('===== Listar Livros =====')
    opcao = int(input('Digite: \n[1] para listar todos os livros cadastrados ou \n[2] para listar livros de um autor específico:   '))

    if opcao == 1:
        if len(livros) == 0:
            clear()
            print('Nenhum livro cadastrado.')
            time.sleep(2)
            clear()
        else:
            clear()
            print('Lista de livros:')
            for livro in livros:
                titulo = livro['titulo'].upper()
                ano = livro['ano']
                codigo_autor = livro['codigo_autor']
                print('Código: ', codigo_autor, '- ', titulo, '(',ano,')')
                time.sleep(3)
    elif opcao == 2:
        clear()
        codigo_autor = input('Digite o código do autor: ')
        for livro in livros:
            if livro['codigo_autor'] == codigo_autor:
                titulo = livro['titulo'].capitalize()
                ano = livro['ano']
                print('Título:', titulo, ' - Ano:', ano)
        time.sleep(2)
    else:
        print('Opção inválida.')
        time.sleep(2)
        clear()


def atualizar_autor():
    clear()
    print('===== Atualizar Autor =====')
    codigo = input('\nDigite o código do(a) Autor(a) que deseja atualizar: ')
    
    autor_encontrado = False
    for autor in autores:
        if autor['codigo'] == codigo:
            novo_nome = input('Digite o novo nome do(a) Autor(a): ')
            autor['nome'] = novo_nome
            print('Atualizando nome do(a) Autor(a)...')
            time.sleep(1)
            print(f'Nome do(a) autor(a) atualizado para {novo_nome}.')
            time.sleep(2)
            autor_encontrado = True
            break

    if not autor_encontrado:
        print('Código do(a) Autor(a) não encontrado.')
        time.sleep(2)
    
    clear()

def atualizar_livro():
    clear()
    print('===== Atualizar livro =====')
    titulo = input('\nDigite o título do livro que deseja atualizar: ')
    livro_encontrado = False
    for livro in livros:
        if livro['titulo'].lower() == titulo.lower():
            novo_titulo = input('Digite o novo título do livro: ')
            novo_ano = input('Digite o ano de publicação do livro: ')
            livro['titulo'] = novo_titulo
            livro['ano'] = novo_ano
            print('Atualizando livro...')
            time.sleep(1)
            print(f'Livro {titulo} atualizado para {novo_titulo} ({novo_ano}).')
            time.sleep(1)
            livro_encontrado = True
            break
    if not livro_encontrado:
        print('Livro não encontrado.')
        time.sleep(2)


def deletar_autor():
    clear()
    print('===== Deletar Autor =====')
    codigo = input('Digite o código do autor que deseja deletar: ')
    autor_encontrado = False

    for autor in autores:
        if autor['codigo'] == codigo:
            autores.remove(autor)
            autor_encontrado = True
            break
    
    if autor_encontrado:
        livros_a_remover = []
        for livro in livros:
            if livro['codigo_autor'] == codigo:
                livros_a_remover.append(livro)
        
        for livro in livros_a_remover:
            livros.remove(livro)
        
        clear()
        print('Removendo...')
        time.sleep(1)
        print('Autor(a) e seus livros deletados com sucesso.')
        time.sleep(2)
    else:
        clear()
        print('Autor(a) não encontrado.')
        time.sleep(2)
    clear()


def deletar_livro():
    clear()
    print('===== Deletar Livro =====')
    titulo = input('\nDigite o título do livro que deseja deletar: ')
    codigo_autor = input('Digite o código do(a) autor(a): ')
    livro_encontrado = False
    
    for livro in livros:
        if livro['titulo'] == titulo and livro['codigo_autor'] == codigo_autor:
            livros.remove(livro)
            livro_encontrado = True
            break
    
    if livro_encontrado:
        print('Removendo livro...')
        time.sleep(1)
        print(f'Livro {titulo} deletado com sucesso.')
        time.sleep(2)
    else:
        clear()
        print('Livro não encontrado.')
        time.sleep(2)
    clear()

def menu():

    while True:

        print('\n==================================================')
        print('   SISTEMA DE GERENCIAMENTO DE LIVROS E AUTORES')
        print('==================================================')
        print('\n              Área de autores                ')
        print('\n[1]. Cadastrar Autor(a)')
        print('[2]. Listar Autores')
        print('[3]. Atualizar Autor(a)')
        print('[4]. Deletar Autor(a)')
        print('\n               Área de livros                 ')
        print('\n[5]. Cadastrar Livros')    
        print('[6]. Listar Livros')
        print('[7]. Atualizar Livro')    
        print('[8]. Deletar Livro')
        print('[9]. Sair do Sistema')
        opcao = input('\n>>>>> Escolha uma opção: ')
        
        if opcao == '1':
            cadastrar_autor()
        elif opcao == '2':
            listar_autores()
        elif opcao == '3':
            atualizar_autor()
        elif opcao == '4':
            deletar_autor()
        elif opcao == '5':
            cadastrar_livro()
        elif opcao == '6':
            listar_livros()
        elif opcao == '7':
            atualizar_livro()
        elif opcao == '8':
            deletar_livro()
        elif opcao == '9':
            clear()
            print('Saindo do sistema...')
            time.sleep(2)
            clear()
            print('Sistema finalizado.')
            break
        else:
            clear()
            print('Opção inválida. Tente novamente.')


menu()
