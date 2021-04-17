import pygame

SCREEN_W = 1200
SCREEN_H = 600
ICON_IMAGE = pygame.image.load('The_good_count/assets/add.png')
pygame.display.set_icon(ICON_IMAGE)
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

    #Background
BG_IMAGE1 = pygame.image.load("The_good_count/assets/BG.jfif").convert_alpha()
BG_IMAGE2 = pygame.image.load('The_good_count/assets/BG.JFIF').convert_alpha()
BG_IMAGE2 = pygame.transform.flip(BG_IMAGE2, True, False)


    #Operators
#Neutral
ADD_IMAGE = pygame.image.load('The_good_count/assets/add.png').convert_alpha()
SUB_IMAGE = pygame.image.load('The_good_count/assets/sub.png').convert_alpha()
MUL_IMAGE = pygame.image.load('The_good_count/assets/mul.png').convert_alpha()
DIV_IMAGE = pygame.image.load('The_good_count/assets/div.png').convert_alpha()

#Clicked
ADD_CLICKED_IMAGE = pygame.image.load('The_good_count/assets/add_clicked.png').convert_alpha()
SUB_CLICKED_IMAGE = pygame.image.load('The_good_count/assets/sub_clicked.png').convert_alpha()
MUL_CLICKED_IMAGE = pygame.image.load('The_good_count/assets/mul_clicked.png').convert_alpha()
DIV_CLICKED_IMAGE = pygame.image.load('The_good_count/assets/div_clicked.png').convert_alpha()


    #Replay button
RESET_SURFACEA = pygame.image.load('The_good_count/assets/resetA.png').convert_alpha()
RESET_SURFACEA = pygame.transform.scale(RESET_SURFACEA, (int(RESET_SURFACEA.get_width() * 0.25), int(RESET_SURFACEA.get_height() * 0.25)))
RESET_SURFACEB = pygame.image.load('The_good_count/assets/resetB.png').convert_alpha()
RESET_SURFACEB = pygame.transform.scale(RESET_SURFACEB, (int(RESET_SURFACEB.get_width() * 0.26), int(RESET_SURFACEB.get_height() * 0.26)))
RESET_RECTA = RESET_SURFACEA.get_rect(center = (900, 35))
RESET_RECTB = RESET_SURFACEB.get_rect(center = (900, 35))


    #Tuto
TUTO_IMAGE1 = pygame.image.load('The_good_count/assets/first_tuto.png').convert_alpha()
TUTO_RECT1 = TUTO_IMAGE1.get_rect(topleft = (2, 3))

TUTO_IMAGE2 = pygame.image.load('The_good_count/assets/second_tuto.png').convert_alpha()
TUTO_RECT2 = TUTO_IMAGE2.get_rect(topleft = (3, 3))

TUTO_IMAGE3 = pygame.image.load('The_good_count/assets/third_tuto.png').convert_alpha()
TUTO_RECT3 = TUTO_IMAGE3.get_rect(topleft = (3, 3))

TUTO_IMAGE4 = pygame.image.load('The_good_count/assets/fourth_tuto.png').convert_alpha()
TUTO_RECT4 = TUTO_IMAGE4.get_rect(topleft = (3, 3))

TUTO_IMAGE5 = pygame.image.load('The_good_count/assets/fifth_tuto.png').convert_alpha()
TUTO_RECT5 = TUTO_IMAGE5.get_rect(topleft = (3, 3))

TUTO_IMAGE6 = pygame.image.load('The_good_count/assets/sixth_tuto.png').convert_alpha()
TUTO_RECT6 = TUTO_IMAGE6.get_rect(topleft = (3, 3))