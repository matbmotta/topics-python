"""
Explicação da estratégia: 
    sorteada a palavra com base no arquivo lista_palavras.txt
    recebido o input do jogador
    Validação do tamanho da palavra
    Comparação letra a letra das palavras, caso exista, é validado se a posição está correta, ao imprimir são colocadas as cores:
        azul: Letra correta, mas na posição inválida
        vermelho: Letra inválida
        verde: na posição correta

Detalhamento das estruturas usadas: 
    utilizado a estrutura Lista para controlar as letras invalidas, na posição correta e incorreta
    utilizado uma tupla onde cada elemento é uma letra da palavra sorteada
    utilizado um set para armazenar as letras que já foram utilizadas
"""

import io
import random

class terminal_colors:
    """classe para ser utilizada nos prints de cores no terminal

    Returns:
        string: cor a ser imprimida no terminal
    """
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    ENDC = '\033[0m'

palavra = ""

def sortear_palavra_arquivo():
    """Realiza a leitura do arquivo lista_palavras.txt e sortea uma palavra para ser utilizada no jogo

    Returns:
        str: palavra sortada
    """
    with io.open("lista_palavras.txt", "r", encoding="utf-8") as f:
        palavras = []
        for linha in f:
            palavras.append(linha.strip())
    return random.choice(palavras)

def iniciar_jogo():

    global palavra
    palavra = sortear_palavra_arquivo()
    letras_utilizadas = set()
    letras_invalidas = []
    letras_posicao_correta = []
    letras_posicao_incorreta = []
    tupla_palavra_sorteada = tuple(palavra)
    tamanho_palavra = len(tupla_palavra_sorteada)
    tentativas = 6

    print("_ " * tamanho_palavra)

    while True:

        print(f"Tentativas restantes: {tentativas}")
        palavra_informada = str(input('Informe uma palavra: '))

        if palavra_informada == palavra:
            print(f"{terminal_colors.GREEN}{palavra}{terminal_colors.ENDC}")
            print("você venceu!")
            break

        if len(palavra_informada) != tamanho_palavra:
            print(f'Tamanho da palavra inválida. Informe uma palavra com {tamanho_palavra} letras')
            continue


        for letra_informada in list(palavra_informada):

            if letra_informada in letras_utilizadas:
                continue

            letras_utilizadas.add(letra_informada)

            try:
                posicao_palavra_sorteada = tupla_palavra_sorteada.index(letra_informada)
                if posicao_palavra_sorteada == palavra_informada.find(letra_informada):
                    letras_posicao_correta.append(letra_informada)
                else: 
                    letras_posicao_incorreta.append(letra_informada)
            except ValueError:
                letras_invalidas.append(letra_informada)

        tentativas = tentativas - 1

        if tentativas == 0:
            print(f"Você perdeu! A palavra era: {palavra}")
            break

        imprimir = ''
        for letra_imprimir in list(palavra_informada):
            try:
                posicao_correta_index = letras_posicao_correta.index(letra_imprimir)
                imprimir = f"{imprimir}{terminal_colors.GREEN}{letra_imprimir}{terminal_colors.ENDC}"
            except ValueError as posicao_incorreta:
                try:
                    posicao_incorreta_index = letras_posicao_incorreta.index(letra_imprimir)
                    imprimir = f"{imprimir}{terminal_colors.BLUE}{letra_imprimir}{terminal_colors.ENDC}"
                except ValueError as letra_outra_posicao:
                    imprimir = f"{imprimir}{terminal_colors.RED}{letra_imprimir}{terminal_colors.ENDC}"

        print(imprimir)

        print(f"Letras inválidas: {letras_invalidas}")

if __name__ == '__main__':
    iniciar_jogo()