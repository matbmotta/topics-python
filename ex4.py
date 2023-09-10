"""Explicação da estratégia: 
    leitura de inputs do usuário com as opções/ subopções de de menu:
        1 - Cadastrar usuário - utiliza a tupla dos campos obrigatórios para solicitar o preenchimento dos dados
        2 - Imprimir usuários
            1 - Imprimir todos - não envia para a função de listar usuários e retorna todos
            2 - Filtrar por nomes - recebe os nomes separados por virgula e realiza a filtragem dos mesmos
            3 - Filtrar por campos - solicita os nomes dos campos e seus respectivos valores, e posteriormente os retorna 
            4 - Filtrar por nomes e campos - solicita os nomes, e posteriormente os campos, na sequência pede que seja atribuído um valor para cada campo.
        3 - Sair

Detalhamento das estruturas usadas:
    Tupla: utilizado no começo do processo quando o usuário determina os campos obrigatórios separados por vírgula
    Lista: utilizado para retornar resultados de listagens que atendem aos critérios de pesquisa
    Dicionário: Banco de dados dos usuários principais

"""

# dicionário global de usuários
banco_usuarios = {}

def cadastrar_usuario(campos_obrigatorios):
    usuario = {}
    
    for campo in campos_obrigatorios:
        valor = input(f'Digite o valor para o campo "{campo}": ')
        usuario[campo] = valor

    while True:
        campo_adicional = input('Digite o nome de um campo adicional ou "sair" para encerrar: ')
        if campo_adicional.lower() == 'sair':
            break
        valor_adicional = input(f'Digite o valor para o campo adicional "{campo_adicional}": ')
        usuario[campo_adicional] = valor_adicional

    # Adicionar o usuário ao banco de dados
    banco_usuarios[len(banco_usuarios)] = usuario

    return usuario

def imprimir_usuarios(*args, **kwargs):
    if not args and not kwargs:
        # Caso não receba argumentos, imprime todos os usuários com todas as informações
        for key in banco_usuarios:
            print(banco_usuarios[key])
    else:
        # Caso receba argumentos, filtre os usuários de acordo com os critérios
        resultados = []
        for key in banco_usuarios:
            usuario = banco_usuarios[key]
            atende_crit = True
            if args:
                # Verificar se os nomes estão na lista de argumentos
                if usuario.get('nome') not in args:
                    atende_crit = False
            if kwargs:
                # Verificar se os campos e valores correspondem aos critérios
                for campo, valor in kwargs.items():
                    if usuario.get(campo) != valor:
                        atende_crit = False
            if atende_crit:
                resultados.append(usuario)
        
        # Imprimir os resultados
        for resultado in resultados:
            print(resultado)

def main():
    campos_obrigatorios = tuple(input('Digite os nomes dos campos obrigatórios separados por vírgula: ').split(','))

    while True:
        print('\nMenu:')
        print('1 - Cadastrar usuário')
        print('2 - Imprimir usuários')
        print('3 - Sair')

        opcao = input('Digite a opção desejada: ')

        if opcao == '1':
            novo_usuario = cadastrar_usuario(campos_obrigatorios)
            print(f'Usuário cadastrado: {novo_usuario}')
        elif opcao == '2':
            print('Opções de impressão:')
            print('1 - Imprimir todos')
            print('2 - Filtrar por nomes')
            print('3 - Filtrar por campos')
            print('4 - Filtrar por nomes e campos')
            sub_opcao = input('Digite a sub-opção desejada: ')
            if sub_opcao == '1':
                imprimir_usuarios()
            elif sub_opcao == '2':
                nomes = input('Digite os nomes separados por vírgula: ').split(',')
                imprimir_usuarios(*nomes)
            elif sub_opcao == '3':
                campos = input('Digite os campos separados por vírgula: ').split(',')
                imprimir_usuarios(**dict(zip(campos, [input(f'Digite o valor para o campo "{campo}": ') for campo in campos])))
            elif sub_opcao == '4':
                nomes = input('Digite os nomes separados por vírgula: ').split(',')
                campos = input('Digite os campos separados por vírgula: ').split(',')
                imprimir_usuarios(*nomes, **dict(zip(campos, [input(f'Digite o valor para o campo "{campo}": ') for campo in campos])))
            else:
                print('Opção inválida!')
        elif opcao == '3':
            print('Saindo do programa...')
            break
        else:
            print('Opção inválida!')

if __name__ == "__main__":
    main()