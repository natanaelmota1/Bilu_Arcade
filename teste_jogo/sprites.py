import pygame
import math

def enemy_generate (screen, player_x, player_y, enemy_x, enemy_y):
    enemy_sprite = pygame.image.load("sprites/spr_grey.png").convert_alpha()
    angle = 360-math.atan2(player_y-enemy_y, player_x-enemy_x)*180/math.pi
    rotimage = pygame.transform.rotate(enemy_sprite, angle)
    rect = rotimage.get_rect(center=(enemy_x, enemy_y))
    enemy = screen.blit(rotimage, rect)