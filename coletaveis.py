from random import randint
import pygame

class Moedas:
    def __init__(self, cor):
        self.cor = cor
        self.x = randint(40, 600)
        self.y = randint(40, 440)
        self.coletadas = 0
    
