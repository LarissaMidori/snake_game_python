import pygame
import random

pygame.init()

azul = (50, 100, 213) # cor do fundo da tela do jogo
laranja = (205, 102, 0)
verde = (0, 255, 0)
amarelo = (255, 255, 102)

dimensoes = (600,600) # dimensões da tela do jogo

fonte =pygame.font.SysFont("Arial", 35)

### Valores Iniciais ###
x = 300
y = 300

d = 20

lista_cobra = [[x, y]]

dx = 0
dy = 0

x_comida = round(random.randrange(0, 600 - d) / 20) * 20 # a comida aparece aleatoriamente na tela
y_comida = round(random.randrange(0, 600 - d) / 20) * 20 # a comida aparece aleatoriamente na tela

tela = pygame.display.set_mode((dimensoes))
pygame.display.set_caption('Snake Game')

tela.fill(azul) # preenche a tela

clock = pygame.time.Clock()

def desenhar_cobra(lista_cobra):
    tela.fill(azul)
    for unidade in lista_cobra:
        pygame.draw.rect(tela, laranja, [unidade[0], unidade[1], d, d])

def mover_cobra(dx, dy, lista_cobra):

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -d
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = d
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -d
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = d

    x_novo = lista_cobra[-1][0] + dx
    y_novo = lista_cobra[-1][1] + dy

    lista_cobra.append([x_novo, y_novo])

    del lista_cobra[0]

    return dx, dy, lista_cobra

def verifica_comida(dx, dy, x_comida, y_comida, lista_cobra):

    head = lista_cobra[-1]

    x_novo = head[0] + dx
    y_novo = head[1] + dy

    if head[0] == x_comida and head[1] == y_comida:
        lista_cobra.append([x_novo, y_novo])
        x_comida = round(random.randrange(0, 600 - d) / 20) * 20 # faz com que a comida aparece em lugares aleatórios
        y_comida = round(random.randrange(0, 600 - d) / 20) * 20

    pygame.draw.rect(tela, verde, [x_comida, y_comida, d , d])

    return x_comida, y_comida, lista_cobra

def verifica_parede(lista_cobra):
    head = lista_cobra[-1]
    x = head[0]
    y = head[1]

    if x not in range(600) or y not in range(600):
        raise Exception # o raise interrompe a execução

def verifica_mordeu_cobra(lista_cobra):
    head = lista_cobra[-1]
    corpo = lista_cobra.copy()

    del corpo[-1]
    for x, y in corpo:
        if x == head[0] and y == head[1]:
            raise Exception

def atualizar_pontos(lista_cobra): # pontuação do jogo
    pontos = str(len(lista_cobra))
    score = fonte.render("Pontuação: " + pontos, True, amarelo)
    tela.blit(score, [0, 0])

while True:
    pygame.display.update()
    desenhar_cobra(lista_cobra)
    dx, dy, lista_cobra = mover_cobra(dx, dy, lista_cobra)
    x_comida, y_comida, lista_cobra = verifica_comida(dx, dy, x_comida, y_comida, lista_cobra)

    print(lista_cobra)
    verifica_parede(lista_cobra)
    verifica_mordeu_cobra(lista_cobra)
    atualizar_pontos(lista_cobra)
    
    clock.tick(10) # isso que vai dar ideia de movimento no jogo