import pygame

from gerenciadores import Gerenciadora

def jogo():
    gerenc = Gerenciadora()
    gerenc.roda_loop()

if __name__ == "__main__":
    jogo()