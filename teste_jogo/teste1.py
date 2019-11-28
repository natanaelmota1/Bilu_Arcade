import pygame
import random
import os
import sys
import math

# Teste de execução do jogo
try:
    pygame.init()
except:
    print('O módulo pygame não foi inicializado com sucesso')

# Parâmetros da tela
width = 800
height = 650

# Interface
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bilu's Arcade")
FPS = pygame.time.Clock()
background = pygame.image.load("sprites/bac_area51.png").convert()
exit = True

# Definindo cores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Parâmetros do player
player_x = 400
player_y = 300
player_sprite = pygame.image.load("sprites/spr_bilu1.png").convert_alpha()
mousec = pygame.image.load('sprites/target2.png').convert_alpha()
pygame.mouse.set_visible(False)

wall_rect = pygame.Rect(200,150,40,40)

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

    # Mira do player
    pos = pygame.mouse.get_pos()
    screen.blit(mousec, (pos))
    angle = 360-math.atan2(pos[1]-player_y, pos[0]-player_x)*180/math.pi
    rotimage = pygame.transform.rotate(player_sprite, angle)
    rect = rotimage.get_rect(center=(player_x, player_y))

    wall = pygame.draw.rect(screen, white, [160, 120, 40, 40])
    player = screen.blit(rotimage, rect)
    player_rect = pygame.Rect(player_x, player_y, 50, 50)

    if wall_rect.colliderect(player_rect) > 0:
        player_x -=20
        player_y -=20
    
    pygame.display.update()
    screen.blit(background, (0, 0))
    FPS.tick(25)