from random import sample

# Variáveis globais para todas as funções
grid = [['*', '*', '*', '*'], ['*', '*', '*', '*'], ['*', '*', '*', '*'], ['*', '*', '*', '*']] # Grid Inicial
resposta = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] # Respostas Iniciais
x = y = acertos = jogadas = 0 # Variáveis que condiciona a vitória ou a derrota de um jogador
escolha1 = escolha2 = [0, 0] # Escolha no grid da rodada 01 e da rodada 02 de cada jogada
fim = True

def main():
    """
    Programa principal que contém todas as outras funções para gerenciar todo o andamento do Jogo da Memória.
    """
    gera_resposta()
    mostra_grid(grid)
    while fim:
        interacao("primeira") # Pede para jogar a primeira rodada
        validacao("primeira") # Verifica a jogada na primeira rodada
        atualiza_escolha(grid) # Atualiza o GRID para o número na posição escolhida
        mostra_grid(grid) # Mostra o GRID atualizado
        interacao("segunda") # Pede para jogar a segunda rodada
        validacao("segunda") # Verifica a jogada na segunda rodada
        atualiza_escolha(grid) # Atualiza o GRID para o número na posição escolhida
        fim_turno() # Finaliza o turno

def gera_resposta():
    """
    Gera uma matriz e cria posições aleatórias.
    :return: list -> list
    """
    opcoes = [1, 2, 3, 4, 5, 6, 7, 8] # Números da matriz como opção de 1 a 8
    ocorrencias = [0, 0, 0, 0, 0, 0, 0, 0] # Ocorrência para cada número da matriz
    for lin in range(len(resposta)):
        for col in range(len(resposta[lin])):
            while True:
                # Garante que cada número dentro desta matriz vai ser repetido, isto é, aparecer duas vezes.
                elemento = sample(opcoes, 1)[0]
                if ocorrencias[elemento - 1] < 2:
                    resposta[lin][col] = elemento
                    ocorrencias[elemento - 1] += 1
                    break

    return resposta



def mostra_grid(grid):
    """
    Representa a matriz em formato de linhas e colunas.
    :param matriz: list(list) -> list(list)
    """
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end='')
        print('\n')

def interacao(turno):
    """
    Interpretador das respostas do usuário para verificar as posições das rodadas do jogo.
    :param turno: str -> str
    """
    global x, y
    posicao = input(f'Escolha a {turno} posição no formato [x,y]: ') # [x,y] => Uma lista com o length de 0 a 4
    x = int(posicao[1]) # Pega o número x dentro da string [x,y] e transforma em inteiro
    y = int(posicao[3]) # Pega o número y dentro da string [x,y] e transforma em inteiro

def validacao(turno):
    """
    Verifica a posição de um número inserido pelo usuário.
    :param turno: str -> str
    :return:
    """
    global x, y, escolha1, escolha2
    # Garante que o usuário não insere uma posição errada, isto é, valor negativo ou acima de 3 (pois o GRID é
    # uma matriz 4x4) indo de 0 a 3.

    while x < 0 or x > 3 or y < 0 or y > 3 or grid[x][y] != '*':
        posicao = input(f'Posição inválida ou já escolhida. Escolha a {turno} posição no formato [x,y]: ')
        x = int(posicao[1]) # Pega o número x dentro da string [x,y] e transforma em inteiro
        y = int(posicao[3]) # Pega o número y dentro da string [x,y] e transforma em inteiro

    if turno == 'primeira':
        # Garante que se o número for inserido no primeiro turno, adiciona este valor para a escolha 1
        escolha1 = [x, y]

    elif turno == 'segunda':
        # Garante que se o número for inserido no segundo turno, adiciona este valor para a escolha 2
        escolha2 = [x, y]

def atualiza_escolha(grid):
    """
    Atualiza os valores do grid para os números inseridos.
    :param matriz: list(list) -> list(list)
    """
    grid[x][y] = resposta[x][y]

def fim_turno():
    """
    Verifica se o usuário acertou ou errou e se chegou ao final do turno.
    :return:
    """
    global jogadas, acertos
    jogadas += 1 # Contador de rodadas no jogo
    # Verifica se a posição escolhida no grid na rodada 01 é o mesmo na rodada 02 e se for acerta a jogada e
    # atualiza o GRID para a próxima rodada.
    if grid[escolha1[0]][escolha1[1]] == grid[escolha2[0]][escolha2[1]]:
        acertos += 1
        mostra_grid(grid)
        print('Parabéns! Você acertou')
        checa_vitoria()

    else:
        # Se o número inserido na posição 01 não for o mesmo na rodada 02, o número não é inserido e o GRID
        # retorna ao inicio.
        mostra_grid(grid)
        grid[escolha1[0]][escolha1[1]] = '*'
        grid[escolha2[0]][escolha2[1]] = '*'
        print('Você errou... tente de novo.')
        mostra_grid(grid)

def checa_vitoria():
    """
    Função helper que verifica se o usuário acertou todos os asteriscos da matriz.
    """
    global fim
    # Se os acertos forem igual a 8, isto é, o GRID terá 8 números para serem acertados então ao chegar em 8 acertos
    # é possível declarar que o jogador acertou todos os números no GRID.
    if acertos == 8:
        print(f'Parabéns! Você conseguiu descobrir todas as casas em {jogadas} jogadas!')
        fim = False


main()

