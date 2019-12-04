import pygame
import os
import sys


def credit():
    # Inicialização do módulo
    pygame.init()

    # Parâmetros da tela
    width = 800
    height = 700

    # Definindo cores
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    midnight_blue = (20, 20, 90)

    # Texto
    def write_text(text, color, posx, posy, font, size):
        font = pygame.font.SysFont(font, size)
        text1 = font.render(text, True, color)
        screen.blit(text1, [posx, posy])

    # Interface
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Bilu's Arcade: Credits")
    FPS = pygame.time.Clock()
    background = screen.fill(midnight_blue)

    on_credits = True

    while (on_credits):
        # Eventos
        for event in pygame.event.get():
            # Condição de saída
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    on_credits = False
            if event.type == pygame.QUIT:
                on_credits = False
        write_text("UNIVERSIDADE DO ESTADO DO AMAZONAS - UEA",
                   white, 120, 10, "stencil", 30)
        write_text("BACHARELADO EM SISTEMAS DE INFORMAÇÃO",
                   white, 120, 35, "stencil", 30)
        write_text("LABORATÓRIO DE PROGRAMAÇÃO DE COMPUTADORES",
                   white, 100, 60, "stencil", 30)
        write_text("PROF. DR. JUCIMAR JR",
                   white, 260, 85, "stencil", 30)
        write_text("DEVELOPERS:",
                   white, 5, 140, "stencil", 50)
        write_text("PAULO ANDRÉ FERNANDES",
                   white, 5, 180, "stencil", 35)
        write_text("NATANAEL DA MOTA FIGUEIRA",
                   white, 5, 205, "stencil", 35)
        write_text("MAX BARROS DE SALES",
                   white, 5, 230, "stencil", 35)
        write_text("DESIGNER:",
                   white, 5, 270, "stencil", 50)
        write_text("JOÃO ROBERTO FERNANDES",
                   white, 5, 310, "stencil", 35)
        write_text("THIRD PARTY ASSETS:",
                   white, 5, 350, "stencil", 50)
        write_text("Menu's song: https://www.youtube.com/watch?v=LGzoJYMhwKo",
                   white, 5, 385, "stencil", 35)
        write_text("Game's song: freesound.org/people/zikeda/sounds/495899/",
                   white, 5, 410, "stencil", 35)
        write_text("Conhecimento: https://www.youtube.com/watch?v=CHxQ8Vp6IpU",
                   white, 5, 435, "stencil", 35)
        write_text("Selection: https://github.com/NatanSIsantos/pong_madness",
                   white, 5, 460, "stencil", 35)
        write_text("Shot: https://www.youtube.com/watch?v=fO9tao41HcE",
                   white, 5, 485, "stencil", 35)
        write_text("Hit: https://www.youtube.com/watch?v=bPIyOaSwFos",
                   white, 5, 510, "stencil", 35)
        write_text("Game over: https://www.youtube.com/watch?v=br3OzOrARh4",
                   white, 5, 535, "stencil", 35)
        write_text("Portal: https://br.pinterest.com/pin/740490363705675693/",
                   white, 5, 560, "stencil", 35)
        pygame.display.update()
        FPS.tick(25)
