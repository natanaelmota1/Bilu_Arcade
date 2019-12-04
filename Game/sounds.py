import pygame


# Função para tocar um som
def play_sound(sound):
    effect = pygame.mixer.Sound(sound)
    effect.play()


# Função para tocar uma música até o jogo fechar
def play_song(song):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(-1)
