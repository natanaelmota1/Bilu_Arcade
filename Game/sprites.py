import pygame
import math


def enemy_generate(screen, player_x, player_y, enemy_x, enemy_y):
    enemy_sprite = pygame.image.load("sprites/spr_grey.png").convert_alpha()
    angle = 360-math.atan2(player_y-enemy_y, player_x-enemy_x)*180/math.pi
    enemy = pygame.transform.rotate(enemy_sprite, angle)
    rect = enemy.get_rect(center=(enemy_x, enemy_y))
    screen.blit(enemy, rect)


def player_generate(screen, player_x, player_y, mousec, mouse_pos):
    screen.blit(mousec, (mouse_pos))
    player_sprite = pygame.image.load("sprites/spr_bilu.png").convert_alpha()
    angle = 360-math.atan2(mouse_pos[1]-player_y,
                           mouse_pos[0]-player_x)*180/math.pi
    player = pygame.transform.rotate(player_sprite, angle)
    rect = player.get_rect(center=(player_x, player_y))
    screen.blit(player, rect)


def lives_generate(screen, lives):
    lives_sprite = pygame.image.load(
        "sprites/spr_bilulife1.png").convert_alpha()
    lives_posx = 100
    for i in range(lives):
        screen.blit(lives_sprite, (lives_posx, 10))
        lives_posx += 20


def portal(screen):
    positions = [[5, 50], [5, 620], [720, 50], [720, 620]]
    for i in range(len(positions)):
        if positions[i] == [720, 620] or positions[i] == [5, 50]:
            portal_sprite = pygame.image.load(
                "sprites/portal.png").convert_alpha()
            portal_sprite = pygame.transform.rotate(portal_sprite, 225)
            screen.blit(portal_sprite, (positions[i][0], positions[i][1]))
        else:
            portal_sprite = pygame.image.load(
                "sprites/portal.png").convert_alpha()
            portal_sprite = pygame.transform.rotate(portal_sprite, 135)
            screen.blit(portal_sprite, (positions[i][0], positions[i][1]))


def write_text(screen, text, color, posx, posy, font, size):
    font = pygame.font.SysFont(font, size)
    text1 = font.render(text, True, color)
    screen.blit(text1, [posx, posy])
