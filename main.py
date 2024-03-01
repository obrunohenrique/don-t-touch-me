import pygame

pygame.init()

tela = pygame.display.set_mode((300, 300))
running = True

while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    clock = pygame.time.Clock()
    clock.tick(60)
    tela.fill("blue")

    pygame.display.update()

pygame.quit()