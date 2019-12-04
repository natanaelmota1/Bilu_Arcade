import pygame
import os
import sys


def menu():
    # Inicialização do módulo
    pygame.init()

    # Definindo cores
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    # Parâmetros da tela
    width = 800
    height = 700

    # Interface
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Bilu's Arcade")
    FPS = pygame.time.Clock()
    background = screen.fill(black)

    on_menu = True

    while (on_menu):
        # Condição de saída
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    on_menu = False
            if (event.type == pygame.QUIT):
                on_menu = False
        pygame.display.update()
        FPS.tick(25)
