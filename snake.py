import pygame

azul = (50, 100, 213)
dimensoes = (600,600)

tela = pygame.display.set_mode((dimensoes))
pygame.display.set_caption('Snake Game')

tela.fill(azul)

clock = pygame.time.Clock()

while True:
    pygame.display.update()
    print('oi')
    clock.tick(1)