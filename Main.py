import pygame
from jogador import Player
from obstaculos import Obst
from random import randint

pygame.init()

# Adiciona uma música de fundo
pygame.mixer.music.set_volume(0.2)
musica_de_fundo = pygame.mixer.music.load('assets/audio/Main Theme.mp3')
pygame.mixer.music.play(-1)

# Adiciona som ao coletar uma moeda
som_moeda = pygame.mixer.Sound('assets/audio/Coin Sound.wav')

#Proporções da tela
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))

# Insere o nome do jogo na jenela
pygame.display.set_caption('Dark Quest')

# Insere textos na tela
fonte = pygame.font.SysFont('arial', 20, True, False)

# Game ON
running = True

# Coordenadas dos objetos na tela
obstaculo1 = Obst("vertical")
obstaculo2 = Obst("horizontal")
jogador = Player(largura, altura)
x4 = randint(40, 600)
y4 = randint(40, 440)
x4_1 = randint(40, 600)
y4_1 = randint(40, 440)


# Início do loop
while running:

    mensagem_moeda_amarela = f'Pontuação: {jogador.pontuacao_amarela}'
    texto_formatado = fonte.render(mensagem_moeda_amarela, True, (255, 255, 255))

    mensagem_moeda_azul = f'Tamanho: {jogador.pontuacao_azul}'
    texto_formatado2 = fonte.render(mensagem_moeda_azul, True, (255, 255, 255))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Modo de inserir funções para as teclas do teclado caso o usuário pressione a tecla ao invés de apertar uma única vez
    jogador.movimentar(largura, altura)

    # Define o FPS do game
    clock = pygame.time.Clock()
    clock.tick(540)
    tela.fill("black")

    # Inimigos ON
    x2 = largura/2 - 20
    y = altura/2 - 20

    # Objetos
    obstaculo_1 = pygame.draw.rect(tela, (255, 0 , 0), (obstaculo1.x, obstaculo1.y, 50, 50))
    obstaculo_2 = pygame.draw.rect(tela, (255, 0 , 0), (obstaculo2.x, obstaculo2.y, 50, 50))
    player = pygame.draw.rect(tela, (0, 255 , 0), (jogador.x, jogador.y, (50 - jogador.pontuacao_azul * 1), (50 - jogador.pontuacao_azul * 1)))
    moeda_amarela = pygame.draw.circle(tela, (255, 255 , 0), (x4, y4), (8))
    moeda_azul = pygame.draw.circle(tela, (0, 255, 255), (x4_1, y4_1), (6))

    # Configura a colisão com as moedas
    if player.colliderect(moeda_amarela):
        x4 = randint(40, 600)
        y4 = randint(40, 440)
        jogador.pontuacao_amarela += 1
        som_moeda.play()

    if player.colliderect(moeda_azul):
        x4_1 = randint(40, 600)
        y4_1 = randint(40, 440)
        jogador.pontuacao_azul += 1
        som_moeda.play()

        # Exibe uma mensagem de pontuação
        print('=+' * 50) if jogador.pontuacao_amarela == 1 else None
        print('{:^100}'.format('Parabéns por coletar mais uma moeda, sua velocidade aumentou!'))
        print('{:^100}'.format(f'Sua nova pontuação é: {jogador.pontuacao_amarela}'))
        print('=+' * 50)

    # Decide onde o texto será exibido
    tela.blit(texto_formatado, (480, 40))
    tela.blit(texto_formatado2, (480, 60))
    
    # Configura a colisão entre os inimigos
    if player.colliderect(obstaculo_1) or player.colliderect(obstaculo_2):
        tela.blit(texto_formatado, (520, 40))
        running = False

        # Exibe uma mensagem de game over e printa a pontuação final
        print('#' * 100)
        print('{:^100}'.format('!!! GAME OVER !!!'))
        print('#' * 100)
        print('{:^100}'.format(f'Sua pontuação final foi: {jogador.pontuacao_amarela}'))
        print('#' * 100)

    # Cria a movimentação dos inimigos
    obstaculo1.movimentar(largura, altura)
    obstaculo2.movimentar(largura, altura)


# Fim do loop

    # Atualiza a tela
    pygame.display.update()

# Encerra o jogoa
pygame.quit()