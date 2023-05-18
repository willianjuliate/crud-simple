import psycopg2
import os


def conectar():
    """
    Função para conectar ao servidor
    """
    try:
        conn = psycopg2.connect(
            database='pypsql',
            host='localhost',
            user='geek',
            password='zaq1'
        )
        return conn
    except psycopg2.Error as err:
        print(f'Erro na conexao ao PostgreSQL Server: {err}')


def desconectar(conn):
    """ 
    Função para desconectar do servidor.
    """
    if conn:
        conn.close()


def listar():
    """
    Função para listar os produtos
    """
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()

    if len(produtos) > 0:
        print('Listando Produtos...')
        print('....................')
        for produto in produtos:
            print(f'id: {produto[0]}')
            print(f'produto: {produto[1]}')
            print(f'preço: {produto[2]}')
            print(f'estoque: {produto[3]}')
        print('....................')
    else:
        print('Nao existem produtos cadastrado')
    desconectar(conn)


def inserir():
    """
    Função para inserir um produto
    """
    conn = conectar()
    cursor = conn.cursor()

    nome = input('Informe o nome do produto: ')
    preco = float(input('Informe o preco do produto: '))
    estoque = int(input('Informe a quantidade em estoque: '))

    cursor.execute(
        f"INSERT INTO produtos (descricao, preco, estoque) VALUES ('{nome}', {preco}, {estoque})")
    conn.commit()
    if cursor.rowcount == 1:
        print(f'O produto {nome} foi inserido com sucesso.')
    else:
        print('Nao foi possivel inserir o produto')
    desconectar(conn)


def atualizar():
    """
    Função para atualizar um produto
    """
    conn = conectar()
    cursor = conn.cursor()

    codigo: int = int(input("Informe o código do produto: "))
    nome = input('Informe o novo nome do produto: ')
    preco = float(input('Informe o novo preco do produto: '))
    estoque = int(input('Informe o novo estoque: '))

    cursor.execute(
        f"UPDATE produtos SET descricao={nome}, preco={preco}, estoque={estoque} WHERE id={codigo} ")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'O produto {nome} foi alterado com sucesso.')
    else:
        print('Nao foi possivel alterar o produto')
    desconectar(conn)


def deletar():
    """
    Função para deletar um produto
    """
    conn = conectar()
    cursor = conn.cursor()
    codigo = int(input('Informe o código do produto para deletar: '))
    cursor.execute(f"DELETE FROM produtos WHERE id={codigo}")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'O produto foi deletado com sucesso.')
    else:
        print('Nao foi possivel deletar o produto')
    desconectar(conn)


def menu():
    """
    Função para gerar o menu inicial
    """
    print('=========Gerenciamento de Produtos==============')
    print('Selecione uma opção: ')
    print('1 - Listar produtos.')
    print('2 - Inserir produtos.')
    print('3 - Atualizar produto.')
    print('4 - Deletar produto.')
    print('0 - Sair.')
    opcao = int(input('> '))
    os.system('cls')
    if opcao in [1, 2, 3, 4, 0]:
        if opcao == 1:
            listar()
        elif opcao == 2:
            inserir()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            deletar()
        elif opcao == 0:
            return
        menu()
    else:
        print('Opção inválida')
