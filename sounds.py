import pygame


pygame.mixer.init()


current_op_sound = pygame.mixer.Sound('The_good_count/sounds/current_op.wav')
menu_sound = pygame.mixer.Sound('The_good_count/sounds/menu.wav')
current_num_sound = pygame.mixer.Sound('The_good_count/sounds/current_num.wav')
reset_sound = pygame.mixer.Sound('The_good_count/sounds/reset.wav')
collide_sound = pygame.mixer.Sound('The_good_count/sounds/collide.wav')
won_stage = pygame.mixer.Sound('The_good_count/sounds/won_stage.wav')
music = pygame.mixer.music.load('The_good_count/sounds/The_good_count_BO.wav')