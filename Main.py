import pygame
from jogador import Player
from obstaculos import Obst
from random import randint

# Encapsula o código principal para o caso do jogo ser reiniciado
def main():
    
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
    pygame.display.set_caption("Don't touch me")

    # Insere textos na tela
    fonte = pygame.font.SysFont('arial', 20, True, False)
    fonte_menor = pygame.font.SysFont('arial', 15, True, False)

    # Game ON
    running = True

    # Coordenadas dos objetos na tela
    obstaculo1 = Obst("vertical")
    obstaculo2 = Obst("horizontal")
    jogador = Player(largura, altura)
    x_moeda_amarela = randint(40, 600)
    y_moeda_amarela = randint(40, 440)
    x_moeda_azul = randint(40, 600)
    y_moeda_azul = randint(40, 440)
    x_moeda_roxa = randint(40, 600)
    y_moeda_roxa = randint(40, 440)


    tempo_inicial = pygame.time.get_ticks()


    # Cria a condição de fim de jogo
    fim_de_jogo = False


    # Início do loop
    while running:


        # Caso o usuário perca o jogo
        while fim_de_jogo:

            # Exibe uma mensagem de game over
            tela.fill("black")
            mensagem_gameover = 'GAME OVER!'
            texto_formatado_gameover = fonte.render(mensagem_gameover, True, (255, 0, 0))
            tela.blit(texto_formatado_gameover, (largura/2-75, altura/2-75))

            # Exibe uma mensagem da pontuação final juntamente com o questionamento de que se o usuário quer tentar novamente ou não
            mensagem_tentar_novamente = f"PONTUAÇÃO FINAL: {jogador.pontuacao_amarela}. PRESSIONE R PARA REINICIAR OU ESC PARA SAIR!"
            texto_formatado_tentar_novamente = fonte_menor.render(mensagem_tentar_novamente, True, (255, 255, 255))
            tela.blit(texto_formatado_tentar_novamente, (largura/2-280, altura/2))
            keys = pygame.key.get_pressed()

            # Interrompe a música
            pygame.mixer.music.stop()

            # Encerra o loop do jogo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Configura as teclas
            if keys[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                pygame.quit()
            if keys[pygame.K_r]:
                main()

            # Atualiza a tela
            pygame.display.update()


        # Configura as mensagens exibidas na tela
        mensagem_moeda_amarela = f'Velocidade: {jogador.pontuacao_amarela}'
        texto_formatado = fonte.render(mensagem_moeda_amarela, True, (255, 255, 255))

        mensagem_tamanho = f'Tamanho: {jogador.tamanho_exibido}'
        texto_formatado2 = fonte.render(mensagem_tamanho, True, (255, 255, 255))


        # Encerra o loop do jogo
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
        player = pygame.draw.rect(tela, (0, 255 , 0), (jogador.x, jogador.y, (50 - jogador.tamanho * 1), (50 - jogador.tamanho * 1)))
        moeda_amarela = pygame.draw.circle(tela, (255, 255 , 0), (x_moeda_amarela, y_moeda_amarela), (8))
        moeda_azul = pygame.draw.circle(tela, (0, 255, 255), (x_moeda_azul, y_moeda_azul), (6))


        # Configura a colisão com as moedas
        if player.colliderect(moeda_amarela):
            x_moeda_amarela = randint(40, 600)
            y_moeda_amarela = randint(40, 440)
            jogador.pontuacao_amarela += 1
            som_moeda.play()

        if player.colliderect(moeda_azul):
            x_moeda_azul = randint(40, 600)
            y_moeda_azul = randint(40, 440)
            jogador.tamanho += 1
            jogador.tamanho_exibido -= 1
            som_moeda.play()

        if jogador.tamanho >= 5:
            moeda_roxa = pygame.draw.circle(tela, (107, 63, 160), (x_moeda_roxa, y_moeda_roxa), (6))
            if player.colliderect(moeda_roxa):
                x_moeda_roxa = randint(40, 600)
                y_moeda_roxa = randint(40, 440)
                jogador.tamanho -= 1
                jogador.tamanho_exibido += 1
                som_moeda.play()

            
        # Decide onde o texto será exibido
        tela.blit(texto_formatado, (480, 40))
        tela.blit(texto_formatado2, (480, 60))
        
        tempo_atual = pygame.time.get_ticks()
        tempo_decorrido = tempo_atual - tempo_inicial

        # Configura a colisão entre os inimigos
        if tempo_decorrido >= 2000:
            if player.colliderect(obstaculo_1) or player.colliderect(obstaculo_2):
                fim_de_jogo = True
                
        # Cria a movimentação dos inimigos
        obstaculo1.movimentar(largura, altura) 
        obstaculo2.movimentar(largura, altura)

    # Fim do loop
        
        # Atualiza a tela
        pygame.display.update()

    # Encerra o jogo
    pygame.quit()

# Roda o código do jogo
main()
