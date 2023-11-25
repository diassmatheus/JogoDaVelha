import random
import os
import time

class JogoDaVelha:
    def __init__(self):
        self.reseta_tabuleiro()

    def imprime_tabuleiro(self):
        print("")
        print(" " + self.tabuleiro[0][0] + " | " + self.tabuleiro[0][1] + " | " + self.tabuleiro[0][2])
        print("-----------")
        print(" " + self.tabuleiro[1][0] + " | " + self.tabuleiro[1][1] + " | " + self.tabuleiro[1][2])
        print("-----------")
        print(" " + self.tabuleiro[2][0] + " | " + self.tabuleiro[2][1] + " | " + self.tabuleiro[2][2])

    def reseta_tabuleiro(self):
        self.tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.encerra = ""

    def checa_vitoria_ou_empate(self):
        dicionario_vitoria = {}

        for i in ["X", "O"]:
            # Horizontais
            dicionario_vitoria[i] = (self.tabuleiro[0][0] == self.tabuleiro[0][1] == self.tabuleiro[0][2] == i)
            dicionario_vitoria[i] = (self.tabuleiro[1][0] == self.tabuleiro[1][1] == self.tabuleiro[1][2] == i) or dicionario_vitoria[i]
            dicionario_vitoria[i] = (self.tabuleiro[2][0] == self.tabuleiro[2][1] == self.tabuleiro[2][2] == i) or dicionario_vitoria[i]
            # Verticais
            dicionario_vitoria[i] = (self.tabuleiro[0][0] == self.tabuleiro[1][0] == self.tabuleiro[2][0] == i) or dicionario_vitoria[i]
            dicionario_vitoria[i] = (self.tabuleiro[0][1] == self.tabuleiro[1][1] == self.tabuleiro[2][1] == i) or dicionario_vitoria[i]
            dicionario_vitoria[i] = (self.tabuleiro[0][2] == self.tabuleiro[1][2] == self.tabuleiro[2][2] == i) or dicionario_vitoria[i]
            # Diagonais                  
            dicionario_vitoria[i] = (self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] == i) or dicionario_vitoria[i]
            dicionario_vitoria[i] = (self.tabuleiro[2][0] == self.tabuleiro[1][1] == self.tabuleiro[0][2] == i) or dicionario_vitoria[i]

        if dicionario_vitoria["X"]:
            self.encerra = "x"
            print("X venceu!")
            time.sleep(1)
            return
        elif dicionario_vitoria["O"]:
            self.encerra = "o"
            print("O venceu!")
            time.sleep(1)
            return
            
        teste_encerramento = 0
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == " ":
                    teste_encerramento += 1
                    break

        if teste_encerramento == 0:
            self.encerra = "e"
            print("Empate!")
            time.sleep(1)
            return



    def jogada_player(self):
        mov_invalido = True

        while mov_invalido:
            try:
                print("Digite a linha do seu próximo lance: ")
                x = int(input())

                print("Digite a coluna do seu próximo lance: ")
                y = int(input())

                if x > 2 or x < 0 or y > 2 or y < 0:
                    print("Coordenadas inválidas")
                    time.sleep(1)
                    continue

                if self.tabuleiro[x][y] != " ":
                    print("Posição já preenchida")
                    time.sleep(1)
                    continue

            except Exception as e:
                print(e)
                continue

            mov_invalido = False
        self.tabuleiro[x][y] = "X"


    def jogada_computador(self):
        jogadas_possiveis = list()

        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == " ":
                    jogadas_possiveis.append((i, j))
                
        if len(jogadas_possiveis) > 0:
            x, y = random.choice(jogadas_possiveis)
            self.tabuleiro[x][y] = "O"


jogo_da_velha = JogoDaVelha()
jogo_da_velha.imprime_tabuleiro()

novamente = 0

while novamente == 0:
    os.system("cls" if os.name == "nt" else "clear")
    jogo_da_velha.imprime_tabuleiro()
    while jogo_da_velha.encerra == "":
        jogo_da_velha.jogada_player()
        jogo_da_velha.jogada_computador()
        os.system("cls" if os.name == "nt" else "clear")
        jogo_da_velha.imprime_tabuleiro()
        jogo_da_velha.checa_vitoria_ou_empate()

    print("Digite 1 para sair ou qualquer número para jogar novamente")
    novamente = int(input())
    if novamente == 1:
        break
    else:
        jogo_da_velha.reseta_tabuleiro()
        novamente = 0