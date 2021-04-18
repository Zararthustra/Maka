import pygame


pygame.mixer.init()


current_op_sound = pygame.mixer.Sound('sounds/current_op.wav')
menu_sound = pygame.mixer.Sound('sounds/menu.wav')
current_num_sound = pygame.mixer.Sound('sounds/current_num.wav')
reset_sound = pygame.mixer.Sound('sounds/reset.wav')
collide_sound = pygame.mixer.Sound('sounds/collide.wav')
won_stage = pygame.mixer.Sound('sounds/won_stage.wav')
music = pygame.mixer.music.load('sounds/The_good_count_BO.wav')