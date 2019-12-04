import pygame

# Variáveis com os nomes e o diretório dos sons


# Função para tocar um som
def play_sound(sound):
    pygame.mixer.init()
    effect = pygame.mixer.Sound(sound)
    effect.play()


# Função para tocar uma música até o jogo fechar
def play_song(song):
    pygame.mixer.init()
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(-1)
