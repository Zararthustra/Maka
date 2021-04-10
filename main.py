"""
Main module
"""
import pygame
from sys import exit
import buttons
from time import sleep

#                                               GLOBAL VARIABLES

    # Screen
pygame.init()
SCREEN_W = 1200
SCREEN_H = 900
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption('Maka')

    # Game
GOAL = 19
NUM1 = 5
NUM2 = 7
NUM3 = 4
NUM4 = 2

CURRENT_BUTTON = None
CURRENT_NUM = None

RUNNING = True
RECTANGLE_DRAGING = False
clock = pygame.time.Clock()
BG_X = 0

    # Images
BG_IMAGE1 = pygame.transform.scale2x(pygame.image.load('Maka/assets/BG.JFIF').convert_alpha())
BG_IMAGE2 = pygame.transform.scale2x(pygame.image.load('Maka/assets/BG.JFIF').convert_alpha())
BG_IMAGE2 = pygame.transform.flip(BG_IMAGE2, True, False)

ADD_IMAGE = pygame.image.load('Maka/assets/add.png').convert_alpha()
SUB_IMAGE = pygame.image.load('Maka/assets/sub.png').convert_alpha()
MUL_IMAGE = pygame.image.load('Maka/assets/mul.png').convert_alpha()
DIV_IMAGE = pygame.image.load('Maka/assets/div.png').convert_alpha()

    # Fonts
GAME_FONT = pygame.font.Font('Maka/assets/MAGNETOB.TTF', 80)
#Title
TITLE_SURFACE = GAME_FONT.render("Maka", False, (255, 230, 230))
TITLE_RECT = TITLE_SURFACE.get_rect(center = (475, 50))
#Goal
GOAL_FONT_SURFACE = GAME_FONT.render(str(GOAL), False, (255, 255, 255))
GOAL_FONT_RECT = GOAL_FONT_SURFACE.get_rect(center = (1050, 800))

    # Buttons
ADD_BUTTON = buttons.ImageButton(990, 125, ADD_IMAGE, 0.4)
SUB_BUTTON = buttons.ImageButton(990, 275, SUB_IMAGE, 0.4)
MUL_BUTTON = buttons.ImageButton(990, 425, MUL_IMAGE, 0.4)
DIV_BUTTON = buttons.ImageButton(990, 575, DIV_IMAGE, 0.4)

NUM1_BUTTON = buttons.FontButton(200, 200, NUM1, 1)
NUM2_BUTTON = buttons.FontButton(650, 200, NUM2, 1)
NUM3_BUTTON = buttons.FontButton(200, 500, NUM3, 1)
NUM4_BUTTON = buttons.FontButton(650, 500, NUM4, 1)

#                                               DISPLAY FUNCS
def display_BG():
    global BG_X
    #Endless moving BG
    screen.blit(BG_IMAGE1, (BG_X, 0))
    screen.blit(BG_IMAGE2, (BG_X + 2000, 0))
    screen.blit(BG_IMAGE1, (BG_X + 4000, 0))
    BG_X -= 2
    if BG_X <= - 4000:
        BG_X = 0

def display_inner_windows():
    #Blocks window
    inner1 = pygame.Surface((850, 600)).fill((0, 0, 0))
    inner1.x = 50
    inner1.y = 100
    pygame.draw.rect(screen, (60, 50, 50), inner1, 0, 0, 20, 20, 20, 0)
    #Operands window
    """inner2 = pygame.Surface((200, 600)).fill((0, 0, 0))
    inner2.x = 950
    inner2.y = 100
    pygame.draw.rect(screen, (60, 50, 50), inner2, 0, 0, 20, 20, 0, 20)"""
    #Result window
    inner3 = pygame.Surface((850, 100)).fill((0, 0, 0))
    inner3.x = 50
    inner3.y = 750
    pygame.draw.rect(screen, (60, 50, 50), inner3, 0, 0, 20, 0, 20, 20)
    #Goal window
    """inner4 = pygame.Surface((200, 100)).fill((0, 0, 0))
    inner4.topleft = (950, 750)
    pygame.draw.rect(screen, (60, 50, 50), inner4, 0, 0, 0, 20, 20, 20)"""

def display_operands_buttons():
    global CURRENT_BUTTON
    #Draw button
    ADD_BUTTON.draw(screen)
    SUB_BUTTON.draw(screen)
    MUL_BUTTON.draw(screen)
    DIV_BUTTON.draw(screen)
    #Save clicked button
    if ADD_BUTTON.clicked:
        CURRENT_BUTTON = ADD_BUTTON
    elif SUB_BUTTON.clicked:
        CURRENT_BUTTON = SUB_BUTTON
    elif MUL_BUTTON.clicked:
        CURRENT_BUTTON = MUL_BUTTON
    elif DIV_BUTTON.clicked:
        CURRENT_BUTTON = DIV_BUTTON
    #Highlighting
    if CURRENT_BUTTON:
        pygame.draw.rect(screen, (120, 0, 155), CURRENT_BUTTON.rect, 4)

def display_nums():
    global CURRENT_NUM
    #Draw button
    NUM1_BUTTON.draw(screen)
    NUM2_BUTTON.draw(screen)
    NUM3_BUTTON.draw(screen)
    NUM4_BUTTON.draw(screen)
    #Save clicked button
    if NUM1_BUTTON.clicked:
        CURRENT_NUM = NUM1_BUTTON
    if NUM2_BUTTON.clicked:
        CURRENT_NUM = NUM2_BUTTON
    if NUM3_BUTTON.clicked:
        CURRENT_NUM = NUM3_BUTTON
    if NUM4_BUTTON.clicked:
        CURRENT_NUM = NUM4_BUTTON
    #Highlighting
    if CURRENT_NUM:
        pygame.draw.rect(screen, (0, 120, 155), CURRENT_NUM.rect, 4)
        if CURRENT_NUM.rect.colliderect(NUM1_BUTTON.rect):
            print("Fusion -> New rect")

            


#                                               MAIN LOOP
while RUNNING:

    clock.tick(120)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #Handle the drag & drop mechanic for NUM_BUTTONS
        if CURRENT_NUM:
            NUM = CURRENT_NUM.rect
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if NUM.collidepoint(event.pos):
                        RECTANGLE_DRAGING = True
                        mouse_x, mouse_y = event.pos
                        offset_x = NUM.x - mouse_x
                        offset_y = NUM.y - mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:            
                    RECTANGLE_DRAGING = False

            elif event.type == pygame.MOUSEMOTION:
                if RECTANGLE_DRAGING:
                    mouse_x, mouse_y = event.pos
                    if 50 < mouse_x < 900 and 100 < mouse_y < 700: 
                        NUM.x = mouse_x + offset_x
                        NUM.y = mouse_y + offset_y
    

    display_BG()
    screen.blit(TITLE_SURFACE, TITLE_RECT)
    display_inner_windows()
    display_nums()
    display_operands_buttons()
    screen.blit(GOAL_FONT_SURFACE, GOAL_FONT_RECT)
    """if NUM1_BUTTON.rect.colliderect(NUM2_BUTTON.rect):
        new = NUM1_BUTTON.rect.union(NUM2_BUTTON.rect)
        pygame.draw.rect(screen, (0, 0, 0), new)"""

    pygame.display.flip()