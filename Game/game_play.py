import pygame
import random
import os
import sys
import math
from sprites import enemy_generate, player_generate


def game():
    # Teste de execução do jogo
    try:
        pygame.init()
    except ImportError:
        print('O módulo pygame não foi inicializado com sucesso')

    # Parâmetros da tela
    width = 800
    height = 700

    # Interface
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Bilu's Arcade")
    FPS = pygame.time.Clock()
    background = pygame.image.load("sprites/bac_area51.png").convert()
    hud = pygame.image.load("sprites/hud.png").convert()
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
    mousec = pygame.image.load('sprites/target2.png').convert_alpha()
    pygame.mouse.set_visible(False)
    enemy_pos = []
    enemys = []
    time = 0

    while(exit):

        # Alguns parêmtros
        mouse_pos = pygame.mouse.get_pos()
        mousec_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], 10, 10)

        # Condição de saída
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit = False
            if (event.type == pygame.QUIT):
                exit = False
            for i in range(len(enemy_pos)):
                if mousec_rect.colliderect(enemys[i]) > 0:
                    if event.type == pygame.MOUSEBUTTONUP:
                        enemy_pos.pop(i)

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

        # Geração inimigos
        time += 1
        if (time % 20 == 0):
            positions = [[100, 150], [100, 600], [700, 150], [700, 600]]
            position = positions[random.randrange(4)]
            enemy_pos.append(position)
            enemys.append(0)

        for i in range(len(enemy_pos)):
            if player_x > enemy_pos[i][0] and enemy_pos[i][0] < player_x - 30:
                enemy_pos[i][0] += 3
            if player_x < enemy_pos[i][0] and enemy_pos[i][0] > player_x + 30:
                enemy_pos[i][0] -= 3
            if player_y > enemy_pos[i][1] and enemy_pos[i][1] < player_y - 30:
                enemy_pos[i][1] += 3
            if player_y < enemy_pos[i][1] and enemy_pos[i][1] > player_y + 30:
                enemy_pos[i][1] -= 3

            enemy_generate(screen, player_x, player_y,
                           enemy_pos[i][0], enemy_pos[i][1])
            enemys[i] = pygame.Rect(enemy_pos[i][0], enemy_pos[i][1], 50, 50)

        # Mira do player
        player_generate(screen, player_x, player_y, mousec, mouse_pos)

        # Colisão parede
        if player_y >= 650:
            player_y = 650
        if player_y <= 100:
            player_y = 100
        if player_x >= 750:
            player_x = 750
        if player_x <= 50:
            player_x = 50

        pygame.display.update()
        screen.blit(background, (0, 50))
        screen.blit(hud, (0, 0))
        FPS.tick(25)
