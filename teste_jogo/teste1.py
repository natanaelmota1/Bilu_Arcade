import pygame
import random
import os
import sys
import math

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
pygame.display.set_caption("Bilu's Arcade")
FPS = pygame.time.Clock()

# definindo cores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Teste
mouse_c = ('sprites/target.jpg')
mousec = pygame.image.load(mouse_c).convert_alpha()

# parâmetros do player
player_x = 300
player_y = 400
player_spryte = pygame.image.load(
    "sprites/spr_bilu1.png").convert_alpha()
angles = [0, 45, 90, 135, 180, 225, 270, 315, 360]
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
    if key[pygame.K_w] or key[pygame.K_UP]:
        player_y -= 10
    if key[pygame.K_s] or key[pygame.K_DOWN]:
        player_y += 10
    if key[pygame.K_a] or key[pygame.K_LEFT]:
        player_x -= 10
    if key[pygame.K_d] or key[pygame.K_RIGHT]:
        player_x += 10
    # Teste
    pos = pygame.mouse.get_pos()
    screen.blit(mousec, (pos))
    angle = 360-math.atan2(pos[1]-300,pos[0]-400)*180/math.pi
    rotimage = pygame.transform.rotate(player_spryte,angle)
    rect = rotimage.get_rect(center=(player_x, player_y))
    player = screen.blit(rotimage,rect)
    pygame.display.update()
    screen.fill(white)
    FPS.tick(25)
