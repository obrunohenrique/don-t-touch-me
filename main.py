import pygame
from random import randint

pygame.init()

musica_de_fundo = pygame.mixer.music.load('Overcome.mp3')
pygame.mixer.music.play(-1)

som_moeda = pygame.mixer.Sound('smw_1-up.wav')

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))

# Insere o nome do jogo na jenela
pygame.display.set_caption('Dark Quest')

# Insere textos na tela
fonte = pygame.font.SysFont('arial', 20, True, False)

running = True

# Coordenadas dos objetos na tela
x = y = 0
x2 = largura/2
y2 = altura/2
x3 = randint(40, 600)
y3 = randint(40, 440)

# Variável da pontuação
pontuacao = int()

# Início do loop
while running:
    mensagem_moeda = f'Pontuação: {pontuacao}'
    texto_formatado = fonte.render(mensagem_moeda, True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Modo de inserir funções para as teclas do teclado
        '''
        if event.type == pygame.KEYDOWN:
          
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                x2 -= 32
                if x2 < 0:
                    x2 = 0

            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                x2 += 32
                if x2 > largura - 50:
                    x2 = largura - 50

            if event.key == pygame.K_w or event.key == pygame.K_UP:
                y2 -= 32
                if y2 < 0:
                    y2 = 0

            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                y2 += 32
                if y2 > altura - 50:
                    y2 = altura - 50
        '''

    # Modo de inserir funções para as teclas do teclado caso o usuário pressione a tecla ao invés de apertar uma única vez
    if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]:
        x2 -= 0.5
        # Isso aqui serve pra inserir colisão com as bordas da tela
        if x2 < 0:
            x2 = 0

    if pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:
        x2 += 0.5
        if x2 > largura - 50:
            x2 = largura - 50

    if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
        y2 -= 0.5
        if y2 < 0:
            y2 = 0

    if pygame.key.get_pressed()[pygame.K_s] or pygame.key.get_pressed()[pygame.K_DOWN]:
        y2 += 0.5
        if y2 > altura - 50:
            y2 = altura - 50

    # Define o FPS do game
    clock = pygame.time.Clock()
    clock.tick(500)
    tela.fill("black")

    x = 295

    # Objetos
    ret_red = pygame.draw.rect(tela, (255, 0 , 0), (x, y, 50, 50))
    ret_green = pygame.draw.rect(tela, (0, 255 , 0), (x2, y2, 50, 50))
    circle_yellow = pygame.draw.circle(tela, (255, 255 , 0), (x3, y3), (5))

    # Configura a colisão com a moeda
    if ret_green.colliderect(circle_yellow):
        x3 = randint(40, 600)
        y3 = randint(40, 440)
        pontuacao += 1
        som_moeda.play()

        # Exibe uma mensagem de pontuação
        print('=+' * 50)
        print('{:^100}'.format('Parabéns por alcançar mais uma moeda!'))
        print('{:^100}'.format(f'Sua nova pontuação é: {pontuacao}'))
        print('=+' * 50)

    tela.blit(texto_formatado, (480, 40))
    
    # Configura a colisão com o inimigo
    if ret_green.colliderect(ret_red):
        tela.blit(texto_formatado, (520, 40))
        running = False

        # Exibe uma mensagem de game over
        print('!' * 100)
        print('{:^100}'.format('GAME OVER !!!'))
        print('!' * 100)

    # Cria a movimentação do inimigo
    y += 1
    if y > altura:
        y = 0

# Fim do Código Principal
    
    pygame.display.update()

pygame.quit()