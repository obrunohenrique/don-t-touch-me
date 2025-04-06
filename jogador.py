import pygame

class Player:
    def __init__(self, largura, altura):
        self.x = largura/2 + 160
        self.y = altura/2 + 160
        self.pontuacao_amarela = 0
        self.tamanho = 0
        self.tamanho_exibido = 0

    def movimentar(self, largura, altura):
        
        if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]:
            # Essa parte, além de configurar a ação, também adiciona velocidade conforme o usuário coleta moedas
            self.x -= 0.5 + (0.05 * self.pontuacao_amarela)
            # Isso aqui serve pra inserir colisão com as bordas da tela
            if self.x < 0:
                self.x = 0

        if pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.x += 0.5 + (0.05 * self.pontuacao_amarela)
            if self.x > largura - (50 - self.tamanho * 1):
                self.x = largura - (50 - self.tamanho * 1)

        if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
            self.y -= 0.5 + (0.05 * self.pontuacao_amarela)
            if self.y < 0:
                self.y = 0

        if pygame.key.get_pressed()[pygame.K_s] or pygame.key.get_pressed()[pygame.K_DOWN]:
            self.y += 0.5 + (0.05 * self.pontuacao_amarela)
            if self.y > altura - (50 - self.tamanho * 1):
                self.y = altura - (50 - self.tamanho * 1)