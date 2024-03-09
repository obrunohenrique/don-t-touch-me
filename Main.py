import pygame
from random import randint

pygame.init()

# Adiciona uma música de fundo
musica_de_fundo = pygame.mixer.music.load('Main Theme.mp3')
pygame.mixer.music.play(-1)

# Adiciona som ao coletar uma moeda
som_moeda = pygame.mixer.Sound('Coin Sound.wav')

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
x = y = x2 = y2 = 0
x3 = largura/2 + 160
y3 = altura/2 - 160
x4 = randint(40, 600)
y4 = randint(40, 440)

# Variável de pontuação
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
        # Essa parte, além de configurar a ação, também adiciona velocidade conforme o usuário coleta moedas
        x3 -= 0.5 + (0.05 * pontuacao)
        # Isso aqui serve pra inserir colisão com as bordas da tela
        if x3 < 0:
            x3 = 0

    if pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:
        x3 += 0.5 + (0.05 * pontuacao)
        if x3 > largura - 50:
            x3 = largura - 50

    if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
        y3 -= 0.5 + (0.05 * pontuacao)
        if y3 < 0:
            y3 = 0

    if pygame.key.get_pressed()[pygame.K_s] or pygame.key.get_pressed()[pygame.K_DOWN]:
        y3 += 0.5 + (0.05 * pontuacao)
        if y3 > altura - 50:
            y3 = altura - 50

    # Define o FPS do game
    clock = pygame.time.Clock()
    clock.tick(540)
    tela.fill("black")

    # Inimigos ON
    x2 = largura/2 - 20
    y = altura/2 - 20

    # Objetos
    ret_red_1 = pygame.draw.rect(tela, (255, 0 , 0), (x, y, 50, 50))
    ret_red_2 = pygame.draw.rect(tela, (255, 0 , 0), (x2, y2, 50, 50))
    ret_green = pygame.draw.rect(tela, (0, 255 , 0), (x3, y3, 50, 50))
    circle_yellow = pygame.draw.circle(tela, (255, 255 , 0), (x4, y4), (8))

    # Configura a colisão com a moeda
    if ret_green.colliderect(circle_yellow):
        x4 = randint(40, 600)
        y4 = randint(40, 440)
        pontuacao += 1
        som_moeda.play()

        # Exibe uma mensagem de pontuação
        print('=+' * 50) if pontuacao == 1 else None
        print('{:^100}'.format('Parabéns por coletar mais uma moeda, sua velocidade aumentou!'))
        print('{:^100}'.format(f'Sua nova pontuação é: {pontuacao}'))
        print('=+' * 50)

    # Decide onde o texto será exibido
    tela.blit(texto_formatado, (480, 40))
    
    # Configura a colisão entre os inimigos
    if ret_green.colliderect(ret_red_1) or ret_green.colliderect(ret_red_2):
        tela.blit(texto_formatado, (520, 40))
        running = False

        # Exibe uma mensagem de game over e printa a pontuação final
        print('#' * 100)
        print('{:^100}'.format('!!! GAME OVER !!!'))
        print('#' * 100)
        print('{:^100}'.format(f'Sua pontuação final foi: {pontuacao}'))
        print('#' * 100)

    # Cria a movimentação dos inimigos
    x += 1
    if x > largura:
        x = 0

    y2 += 1
    if y2 > altura:
        y2 = 0

# Fim do loop

    # Atualiza a tela
    pygame.display.update()

# Encerra o jogo
pygame.quit()