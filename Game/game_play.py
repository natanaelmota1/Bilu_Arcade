import pygame
import random
import os
import sys
import math
from sprites import*


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
    background = pygame.image.load("sprites/background.png").convert()
    hud = pygame.image.load("sprites/hud.png").convert()
    knowledge = pygame.image.load("sprites/brain.png").convert_alpha()
    exit = True

    # Definindo cores
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 128, 0)
    blue = (0, 0, 255)

    # Parâmetros do player
    player_x = 400
    player_y = 300
    mousec = pygame.image.load('sprites/target2.png').convert_alpha()
    pygame.mouse.set_visible(False)
    enemy_pos = []
    enemys = []
    time = 0
    lives = 5
    knowledge_pos = []
    knowledge_rects = []
    score = 0

    while(exit):

        # Alguns parêmtros
        mouse_pos = pygame.mouse.get_pos()
        player_rect = pygame.Rect(player_x, player_y, 50, 50)

        # Condição de saída
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit = False
            if (event.type == pygame.QUIT):
                exit = False

            # Tiro nos inimigos
            i = 0
            while i < len(enemy_pos):
                if (mouse_pos[0] >= enemy_pos[i][0]-20 and
                    mouse_pos[0] <= enemy_pos[i][0]+20 and
                    mouse_pos[1] >= enemy_pos[i][1]-20 and
                        mouse_pos[1] <= enemy_pos[i][1]+20):
                    if event.type == pygame.MOUSEBUTTONUP:
                        enemy_pos.pop(i)
                        enemys.pop(i)
                i += 1

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
        portal(screen)
        if (time % 30 == 0):
            positions = [[60, 80], [60, 640], [740, 80], [740, 640]]
            position = positions[random.randrange(4)]
            enemy_pos.append(position)
            enemys.append(0)
            position = 0

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
            enemys[i] = pygame.Rect(enemy_pos[i][0], enemy_pos[i][1], 40, 40)

        # Geração do conhecimento
        if time % 60 == 0:
            pos = [random.randrange(200, 600, 20),
                   random.randrange(200, 500, 20)]
            knowledge_pos.append(pos)
            knowledge_rects.append(0)
        for i in range(len(knowledge_pos)):
            screen.blit(knowledge, (knowledge_pos[i][0], knowledge_pos[i][1]))
            knowledge_rects[i] = pygame.Rect(
                knowledge_pos[i][0], knowledge_pos[i][1], 30, 30)

        # Geração do player
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

        for i in range(len(enemy_pos)):
            if enemy_pos[i][0] >= 750:
                enemy_pos[i][0] = 750
            if enemy_pos[i][0] <= 50:
                enemy_pos[i][0] = 50
            if enemy_pos[i][1] >= 650:
                enemy_pos[i][1] = 650
            if enemy_pos[i][1] <= 100:
                enemy_pos[i][1] = 100

        # Vidas
        for i in range(len(enemys)):
            if player_rect.colliderect(enemys[i]):
                if enemy_pos[i][0] > player_x:
                    enemy_pos[i][0] += 50
                if enemy_pos[i][0] < player_x:
                    enemy_pos[i][0] -= 50
                if enemy_pos[i][1] > player_y:
                    enemy_pos[i][1] += 50
                if enemy_pos[i][1] < player_y:
                    enemy_pos[i][1] -= 50
                lives -= 1
        if lives < 1:
            exit = False

        # Pontuação
        i = 0
        while i < len(knowledge_pos):
            if player_rect.colliderect(knowledge_rects[i]):
                knowledge_pos.pop(i)
                score += 10
            i += 1

        # Hud
        write_text(screen, "LIVES:", green, 10, 10, "stencil", 35)
        lives_generate(screen, lives)
        write_text(screen, "KNOWLEDGE:", green, 400, 10, "stencil", 35)
        write_text(screen, "{0:>15}".format(score),
                   white, 600, 10, "stencil", 40)

        pygame.display.update()
        screen.blit(background, (0, 0))
        screen.blit(hud, (0, 0))
        screen.blit(knowledge, (750, 10))
        FPS.tick(25)
