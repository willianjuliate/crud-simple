import MySQLdb
import os


def conectar():
    """
    Função para conectar ao servidor
    """
    try:
        conn = MySQLdb.connect(
            db='pmysql',
            host='localhost',
            user='geek',
            passwd='741963',
        )
        return conn
    except MySQLdb.Error as e:
        print(f'Erro na conexão ao Mysql Server: {e}')


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
    curs = conn.cursor()
    curs.execute('SELECT * FROM produtos')
    produtos = curs.fetchall()

    if len(produtos) > 0:
        print('Listando produtos...')
        print('....................')
        for produto in produtos:
            print(
                f'ID: {produto[0]}\nProduto: {produto[1]}\nPreço: {produto[2]}\nEstoque: {produto[3]}')
            print('....................')
    else:
        print('Não existe produtos cadastrados.')
    desconectar(conn)


def inserir():
    """
    Função para inserir um produto
    """
    conn = conectar()
    curs = conn.cursor()

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))
    estoque: int = int(input('Informe a quantidade em estoque: '))

    curs.execute(
        f"INSERT INTO produtos(nome, preco, estoque) VALUES ('{nome}', {preco}, {estoque})")
    conn.commit()
    if curs.rowcount == 1:
        print(f'O produto {nome} foi inserido com sucesso.')
    else:
        print('Não foi possível inserir o produto.')
    desconectar(conn)


def atualizar():
    """
    Função para atualizar um produto
    """
    conn = conectar()
    curs = conn.cursor()

    listar()

    codigo: int = int(input("Informe o código do produto: "))
    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o novo preço do produto: '))
    estoque: int = int(input('Informe a nova quantidade em estoque: '))

    curs.execute(
        f"UPDATE produtos SET nome='{nome}', preco={preco}, estoque={estoque} WHERE id={codigo}")
    conn.commit()

    if curs.rowcount == 1:
        print(f'O produto {nome} foi atualizado com sucesso.')
    else:
        print('Não foi possível atualizar o produto.')
    desconectar(conn)


def deletar():
    """
    Função para deletar um produto
    """
    conn = conectar()
    curs = conn.cursor()

    listar()
    codigo = int(input('Informe o código do produto para deletar: '))
    curs.execute(f'DELETE FROM produtos WHERE id={codigo}')
    conn.commit()

    if curs.rowcount == 1:
        print(f'O produto foi deletado com sucesso.')
    else:
        print('Não foi possível deletar o produto.')
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
