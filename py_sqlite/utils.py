import sqlite3
import os


def conectar():
    """
    Função para conectar ao servidor
    """
    conn = sqlite3.connect('mydb.db')
    conn.execute("""
          CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            estoque  INTEGER NOT NULL
          );      
    """)
    return conn


def desconectar(conn):
    """ 
    Função para desconectar do servidor.
    """
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
            print(f'nome: {produto[1]}')
            print(f'peço: {produto[2]}')
            print(f'estoque: {produto[3]}')
            print('....................')
    else:
        print('Não existem produtos cadastrados!')


def inserir():
    """
    Função para inserir um produto
    """
    conn = conectar()
    cursor = conn.cursor()

    nome = input('Informe o nome do produto: ')
    preco = float(input('Informe o preço do produto: '))
    estoque = int(input('Informe o valor em estoque: '))

    cursor.execute(
        f"INSERT INTO produtos (nome, preco, estoque) VALUES ('{nome}', {preco}, {estoque});")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'Produto {nome} inseriodo com sucesso!')
    else:
        print('Falha ao inserir o produto!')
    desconectar(conn)


def atualizar():
    """
    Função para atualizar um produto
    """
    conn = conectar()
    cursor = conn.cursor()

    codigo = int(input('Informe o codigo do produto: '))
    nome = input('Informe o nome do produto: ')
    preco = float(input('Informe o preço do produto: '))
    estoque = int(input('Informe o valor em estoque: '))

    cursor.execute(
        f"UPDATE produto SET nome='{nome}', preco={preco}, estoque={estoque} WHERE id={codigo}")
    conn.commit()

    if cursor.rowcount == 1:
        print('Produto atualizado com sucesso!')
    else:
        print('Erro ao atualiza o produto!')
    desconectar(conn)


def deletar():
    """
    Função para deletar um produto
    """
    conn = conectar()
    cursor = conn.cursor()
    codigo = int(input('Informe o codido do produto: '))
    cursor.execute(f"DELETE FROM produtos WHERE id={codigo}")
    conn.commit()

    if cursor.rowcount == 1:
        print('Produto removido com sucesso!')
    else:
        print('Erro ao remover o produto!')

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
