""" 
Explicação da estratégia: 

    OBS: A implementação do jogo é exatamente a mesma utilizada no exercício 1, 
    com a diferença de que nos valores de ranges fixos do código (tamanho fixo do tabuleiro em linhas e colunas)
    é aceito um valor informado pelo usuário, que é utilizado para determinar o número de linhas e colunas

    Inicia com o Jogador "O"
    Valores possíveis por casa: "X", "O", " "
    Utilizado uma lista e valida se a linha e a coluna informada existe no tabuleiro. 
        - caso a linha / coluna exista: É preenchida a posição no tabuleiro, realizada a verificação de vitória ou empate.
        - Caso a linha ou a coluna não exista, a entrada é inválida e é solicitada uma nova entrada válida de uma casa que exista no tabuleiro;
        - Caso tenha ocorrido vitória ou empate, o sistema imprime o resultado e encerra a execução
        - Caso não tenha ocorrido vitória ou empate, o jogador da vez é alterado ("X" ou "O") e é solicitada uma nova entrada de linha e coluna do jogador.

Detalhamento das estruturas usadas: utilizado a estrutura Lista
"""

linhas_colunas = 0

def imprimir_tabuleiro(tabuleiro):
    """imprime o tabuleiro com a divisão " | "

    Args:
        tabuleiro (list): Lista de linhas que contém os valores das colunas
    """
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("--" * 21)

def ganhou_jogo(tabuleiro, jogador):
    """Retorna se o jogador venceu o jogo
    Args:
        tabuleiro (list): Lista multidimensional representando o tabuleiro
        jogador (str): string representando o jogador (valores possíveis: "X" ou "O")

    Returns:
        bool: Valor booleano representando vitória ou derrota
    """
    for linha in tabuleiro:
        # Valida se o jogador venceu em todas as casas em uma linha horizontal
        if all(casa == jogador for casa in linha):
            return True

    for coluna in range(linhas_colunas):
        # Valida se o jogador venceu em todas as casas em uma linha vertical
        if all(tabuleiro[linha][coluna] == jogador for linha in range(linhas_colunas)):
            return True

    if all(tabuleiro[i][i] == jogador for i in range(linhas_colunas)) or all(tabuleiro[i][(linhas_colunas - 1) - i] == jogador for i in range(linhas_colunas)):
        # valida se o jogador venceu na diagonal
        return True

    return False

def empatou(tabuleiro):
    """Verifica se o jogo empatou

    Args:
        tabuleiro (list): o tabuleiro

    Returns:
        bool
    """
    return all(casa != " " for linha in tabuleiro for casa in linha)

def iniciar_jogo():

    while True:
        global linhas_colunas
        linhas_colunas = int(input(f"Informe o número de linhas / colunas do jogo: "))
        if linhas_colunas >= 3:
            break
        else:
            print("Informe um número maior ou igual a 3 para iniciar o jogo")

    tabuleiro = [[" " for _ in range(linhas_colunas)] for _ in range(linhas_colunas)]
    jogador = "O"

    while True:
        imprimir_tabuleiro(tabuleiro)
        linha = int(input(f"Jogador {jogador}, informe a linha (1-{linhas_colunas}): "))
        coluna = int(input(f"Jogador {jogador}, informe a coluna (1-{linhas_colunas}): "))

        linha = linha - 1
        coluna = coluna - 1

        if 0 <= linha <= linhas_colunas and 0 <= coluna <= linhas_colunas and tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador

            if ganhou_jogo(tabuleiro, jogador):
                imprimir_tabuleiro(tabuleiro)
                print(f"Jogador {jogador} venceu!")
                break
            elif empatou(tabuleiro):
                imprimir_tabuleiro(tabuleiro)
                print("O jogo empatou!")
                break
            else:
                if jogador == "X":
                    jogador = "O"
                else:
                    jogador = "X"
        else:
            print("Esta casa não existe, informe uma válida")

if __name__ == "__main__":
    iniciar_jogo()