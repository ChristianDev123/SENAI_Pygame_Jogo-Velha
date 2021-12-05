import time
import sys
import pygame as game
game.init()
# Matriz Paralela para verificação de resultado:
matrizParalela = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
]
# Dicionário de cores em RGB (Red, Green, Blue):
coresEmRGB = {
    "branco":(255,255,255),
    "preto":(0,0,0),
    "vermelho":(255,0,0),
    "azul":(0,0,255),
    "verde":(0,255,0),
    "vermeloEscuro":(139,0,0),
    "cinza":(128, 128, 128),
    "prata":(192, 192, 192),
    "azulEscuro":(0,0,128),
    "amarelo":(255,255,0),
    "aqua":(0,255,255),
    "magenta":(255,0,255),
    "marrom":(128,0,0),
}
# Configurações da tela do jogo: 
dimensao = (720,720)
tela = game.display.set_mode(dimensao)
tela.fill(coresEmRGB["branco"])
alturaTela = tela.get_height()
larguraTela = tela.get_width()
# Cosições das linhas do jogo:
linhasTela = {
    "horizontalC": {
        "posInicial":(0,alturaTela/3),
        "posFinal":(larguraTela,alturaTela/3),
    },
    "horizontalB":{
        "posInicial":(0,(alturaTela/3)*2),
        "posFinal":(larguraTela,(alturaTela/3)*2),
    },
    "verticalE":{
        "posInicial":(larguraTela/3,0),
        "posFinal":(larguraTela/3,alturaTela),
    },
    "verticalD":{
        "posInicial":((larguraTela/3)*2,0),
        "posFinal":((larguraTela/3)*2,alturaTela),
    }
}
# configurações das imagens a serem colocadas no jogo:
imagemX = game.image.load("imagemX.gif")
imagemXMenor = game.transform.scale(imagemX,(150,150))
imagemO = game.image.load("imagemO.jpg")
imagemOMenor = game.transform.scale(imagemO,(150,150))
# posições para serem colocadas as imagens na tela:
posicaoJogo = {
    "1":(0,0),
    "2":((larguraTela/3),0),
    "3":((larguraTela/3)*2,0),
    "4":(0,(alturaTela/3)),
    "5":((larguraTela/3),(alturaTela/3)),
    "6":((larguraTela/3)*2,(alturaTela/3)),
    "7":(0,(alturaTela/3)*2),
    "8":((larguraTela/3),(alturaTela/3)*2),
    "9":((larguraTela/3)*2,(alturaTela/3)*2),
}
# Variavel de controle de jogadas
jogadas = 0
# Função que cria linhas do jogo na tela:
def linhaTela():
    game.draw.line(tela,coresEmRGB["vermelho"],linhasTela["horizontalC"]["posInicial"],linhasTela["horizontalC"]["posFinal"],7)
    game.draw.line(tela,coresEmRGB["vermelho"],linhasTela["horizontalB"]["posInicial"],linhasTela["horizontalB"]["posFinal"],7)
    game.draw.line(tela,coresEmRGB["azul"],linhasTela["verticalE"]["posInicial"],linhasTela["verticalE"]["posFinal"],7)
    game.draw.line(tela,coresEmRGB["azul"],linhasTela["verticalD"]["posInicial"],linhasTela["verticalD"]["posFinal"],7)    
# Função para inserir as jogadas e registra-las na matriz paralela: 
def jogo(jogador, posicao):
    x = int(posicao[0]/200)
    y = int(posicao[1]/200)
    if(matrizParalela[x][y] != "x" and matrizParalela[x][y] != "o"):
        if(jogador == "x"):
            colocaImagem(imagemXMenor,posicao[0],posicao[1])
            matrizParalela[x][y] = jogador
            return "jogou"
        else:
            colocaImagem(imagemOMenor,posicao[0],posicao[1])
            matrizParalela[x][y] = jogador
            return "jogou"
    else:
        print("posição já escolhida! faça outra jogada")
# Função para inserir imagens no jogo:
def colocaImagem(varImagem,posX,posY):
    tela.blit(varImagem,(posX+50,posY+50))
# Função para definir a vez de cada jogada baseado na variável de controle:
def jogadorVez():
    if(jogadas%2 == 0 ):
        return "x"
    else:
        return "o"
# Função para verificação de resultado:
def verificaResultado(symbolPlayer):
    pontoDiagonal = 0
    pontoDiagonalSecundaria = 0
    pontoLinhas0 = 0
    pontoLinhas1 = 0
    pontoLinhas2 = 0
    pontosColuna0 = 0
    pontosColuna1 = 0
    pontosColuna2 = 0
    for x in range(0,3):
        for y in range(0,3):
            # diagonais
            if(x==y and matrizParalela[x][y] == symbolPlayer):
                pontoDiagonal += 1
            if((x == 0 and y == 2) or (x == 1 and y == 1) or (x == 2 and y == 0)):
                if(matrizParalela[x][y] == symbolPlayer):
                    pontoDiagonalSecundaria += 1
            # linhas
            if(x == 0):
                if(matrizParalela[x][y] == symbolPlayer):
                    pontoLinhas0 += 1
                    if(y == 2 and pontoLinhas0 != 3):
                        pontoLinhas0 = 0
            if(x == 1):
                if(matrizParalela[x][y] == symbolPlayer):
                    pontoLinhas1 += 1
                    if(y == 2 and pontoLinhas1 != 3):
                        pontoLinhas1 = 0
            if(x == 2):
                if(matrizParalela[x][y] == symbolPlayer):
                    pontoLinhas2 += 1
                    if(y == 2 and pontoLinhas2 != 3):
                        pontoLinhas2 = 0
            #colunas
            if(y == 0):
                if(matrizParalela[x][y] == symbolPlayer):
                    pontosColuna0 += 1
                    if(x == 2 and pontosColuna0 != 3):
                        pontosColuna0 = 0
            if(y == 1):
                if(matrizParalela[x][y] == symbolPlayer):
                    pontosColuna1 += 1
                    if(x == 2 and pontosColuna1 != 3):
                        pontosColuna1 = 0
            if(y == 2):
                if(matrizParalela[x][y] == symbolPlayer):
                    pontosColuna2 += 1
                    if(x == 2 and pontosColuna2 != 3):
                        pontosColuna2 = 0
            if(pontoDiagonal == 3):
                return 3
            if(pontoDiagonalSecundaria == 3):
                return 3
            if(pontoLinhas0 == 3):
                return 3
            if(pontoLinhas1 == 3):
                return 3
            if(pontoLinhas2 == 3):
                return 3
            if(pontosColuna0 == 3):
                return 3
            if(pontosColuna1 == 3):
                return 3
            if(pontosColuna2 == 3):
                return 3

linhaTela()
#WhatDog:
while True:
    for evento in game.event.get():
        # Para a leitura do código inteiro ao detectar o fechamento da tela do jogo:
        if(evento.type == game.QUIT):
            for q in range(len(matrizParalela)):
                print(matrizParalela[q])
            sys.exit()
        # Detecta o click do mouse na tela do jogo:
        if(evento.type == game.MOUSEBUTTONDOWN):
            posicaoMouse = game.mouse.get_pos()
            #linha 01
            if((posicaoMouse[0] < larguraTela/3) and (posicaoMouse[1] <= alturaTela/3)):
                posicao = posicaoJogo["1"] 
            elif((posicaoMouse[0] < (larguraTela/3)*2) and (posicaoMouse[1] <= alturaTela/3)):
                posicao = posicaoJogo["2"]
            elif((posicaoMouse[0] > (larguraTela/3)*2) and (posicaoMouse[1] <= alturaTela/3)):
                posicao = posicaoJogo["3"]
            # Linha 02
            elif((posicaoMouse[0] < (larguraTela/3)) and (posicaoMouse[1] <= (alturaTela/3)*2)):
                posicao = posicaoJogo["4"]
            elif((posicaoMouse[0] < (larguraTela/3)*2) and (posicaoMouse[1] <= (alturaTela/3)*2)):
                posicao = posicaoJogo["5"]
            elif((posicaoMouse[0] > (larguraTela/3)*2) and (posicaoMouse[1] <= (alturaTela/3)*2)):
                posicao = posicaoJogo["6"]
            # Linha 03
            elif((posicaoMouse[0] < (larguraTela/3)) and (posicaoMouse[1] >= (alturaTela/3)*2)):
                posicao = posicaoJogo["7"]
            elif((posicaoMouse[0] < (larguraTela/3)*2) and (posicaoMouse[1] >= (alturaTela/3)*2)):
                posicao = posicaoJogo["8"]
            elif((posicaoMouse[0] > (larguraTela/3)*2) and (posicaoMouse[1] >= (alturaTela/3)*2)):
                posicao = posicaoJogo["9"]
            
            if(jogo(jogadorVez(),posicao) == "jogou"):
                if(verificaResultado(jogadorVez()) == 3):
                    print(f"Jogador [{jogadorVez()}] ganhou!")
                    while True:
                        sys.exit()
                jogadas += 1
            if(jogadas == 9):
                print("O jogo acabou! Empate")
                while True:
                    sys.exit()
                

    game.display.flip()