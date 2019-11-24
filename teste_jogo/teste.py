import pygame
import random
import os

# teste de execução do jogo
try:
    pygame.init()
except:
    print('O módulo pygame não foi inicializado com sucesso')

# parâmetros da tela
width = 800
height = 650

# interface
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bilu's Escape")
FPS = pygame.time.Clock()

# definindo cores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# parâmetros do player
player_x = 300
player_y = 400
player_spryte = pygame.image.load("sprites/yellowbird-midflap.png").convert_alpha()
angles = [0,30,90,135,180,225,270,315,360]
angle = 0
exit = True

while(exit):

    # Condição de saída
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit = False
        if (event.type == pygame.QUIT):
            exit = False
    
    # Movimentação do player
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        player_y -= 10
        angle = 90
    if key[pygame.K_s]:
        player_y += 10
        angle = 270
    if key[pygame.K_a]:
        player_x -= 10
        angle = 180
    if key[pygame.K_d]:
        player_x += 10
        angle = 0
    
    player_spryte1 = pygame.transform.rotate(player_spryte, angle)
    player = screen.blit(player_spryte1, (player_x, player_y))
    pygame.display.update()
    screen.fill(white)
    FPS.tick(25)
