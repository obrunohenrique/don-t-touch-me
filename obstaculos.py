from random import randint


class Obst:
    def __init__(self, direcao):
        self.x = randint(40, 600)
        self.y = randint(40, 440)
        self.direcao = direcao
    def movimentar(self, largura, altura):

        if self.direcao == "horizontal":

            self.x += 1
            if self.x > largura:
                self.x = 0
        
        if self.direcao == "vertical":

            self.y += 1
            if self.y > altura:
                self.y = 0
            
