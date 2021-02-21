from random import sample

grid = [['*', '*', '*', '*'], ['*', '*', '*', '*'], ['*', '*', '*', '*'], ['*', '*', '*', '*']]
resposta = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
x = y = acertos = jogadas = 0
escolha1 = escolha2 = [0, 0]
fim = True

def main():
    """
    Programa principal que contém todas as outras funções para gerenciar todo o andamento do Jogo da Memória.
    """
    geraResposta()
    mostraMatriz(grid)
    while fim:
        interacao("primeira")
        validacao("primeira")
        atualizaEscolha(grid)
        mostraMatriz(grid)
        interacao("segunda")
        validacao("segunda")
        atualizaEscolha(grid)
        fimDeTurno()

def geraResposta():
    """
    Gera uma matriz e cria posições aleatórias.
    :return: list -> list
    """
    opcoes = [1, 2, 3, 4, 5, 6, 7, 8]
    ocorrencias = [0, 0, 0, 0, 0, 0, 0, 0]
    for lin in range(len(resposta)):
        for col in range(len(resposta[lin])):
            while True:
                elemento = sample(opcoes, 1)[0]
                if ocorrencias[elemento - 1] < 2:
                    resposta[lin][col] = elemento
                    ocorrencias[elemento - 1] += 1
                    break

    return resposta



def mostraMatriz(matriz):
    """
    Representa a matriz em formato de linhas e colunas.
    :param matriz: list(list) -> list(list)
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end='')
    print('\n')

def interacao(turno):
    """
    Interpretador das respostas do usuário para verificar as posições das rodadas do jogo.
    :param turno: str -> str
    """
    global x, y
    posicao = input(f'Escolha a {turno} posição no formato [x,y]: ')
    x = int(posicao[1])
    y = int(posicao[3])

def validacao(turno):
    """
    Verifica a posição de um número inserido pelo usuário.
    :param turno: str -> str
    :return:
    """
    global x, y, escolha1, escolha2
    while x < 0 or x > 3 or y < 0 or y > 3 or grid[x][y] != '*':
        posicao = input(f'Posição inválida ou já escolhida. Escolha a {turno} posição no formato [x,y]: ')
        x = int(posicao[1])
        y = int(posicao[3])

    if turno == 'primeira':
        escolha1 = [x, y]

    elif turno == 'segunda':
        escolha2 = [x, y]

def atualizaEscolha(matriz):
    """
    Atualiza os valores da matriz para os números inseridos.
    :param matriz: list(list) -> list(list)
    """
    matriz[x][y] = resposta[x][y]

def fimDeTurno():
    """
    Verifica se o usuário acertou ou errou e se chegou ao final do turno.
    :return:
    """
    global jogadas, acertos
    jogadas += 1
    if grid[escolha1[0]][escolha1[1]] == grid[escolha2[0]][escolha2[1]]:
        acertos += 1
        mostraMatriz(grid)
        print('Parabéns! Você acertou')
        checarVitoria()

    else:
        mostraMatriz(grid)
        grid[escolha1[0]][escolha1[1]] = '*'
        grid[escolha2[0]][escolha2[1]] = '*'
        print('Você errou... tente de novo.')
        mostraMatriz(grid)

def checarVitoria():
    """
    Função helper que verifica se o usuário acertou todos os asteriscos da matriz.
    """
    global fim
    if acertos == 8:
        print(f'Parabéns! Você conseguiu descobrir todas as casas em {jogadas} jogadas!')
        fim = False


main()
