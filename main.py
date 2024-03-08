import pygame

pygame.init()

tela = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Dark Quest')
running = True

while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    clock = pygame.time.Clock()
    clock.tick(60)
    tela.fill("black")

    pygame.display.update()

pygame.quit()
