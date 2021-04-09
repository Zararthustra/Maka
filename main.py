"""
Main module
"""
import pygame
from sys import exit
import button
from time import sleep


#                                               GLOBAL VARIABLES
# Screen
SCREEN_W = 1200
SCREEN_H = 900
INNER_SCREEN_S = 500
MARGIN_LEFT = 50
MARGIN_TOP = 100
MARGIN_RIGHT = 350
MARGIN_BOT = 300

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption('Maka')

# Game
RUNNING = True
CURRENT_BUTTON = None
CURRENT_BLOCK = None
RECTANGLE_DRAGING = False
clock = pygame.time.Clock()

# Images
BG_IMAGE = pygame.transform.scale2x(pygame.image.load('Maka/assets/BG.JFIF').convert_alpha())

ADD_IMAGE = pygame.transform.scale2x(pygame.image.load('Maka/assets/plus.png').convert_alpha())
SUB_IMAGE = pygame.transform.scale2x(pygame.image.load('Maka/assets/moins.png').convert_alpha())
MUL_IMAGE = pygame.transform.scale2x(pygame.image.load('Maka/assets/fois.png').convert_alpha())
DIV_IMAGE = pygame.transform.scale2x(pygame.image.load('Maka/assets/divise.png').convert_alpha())

BLOCK1_IMAGE = pygame.transform.scale2x(pygame.image.load('Maka/assets/num1.png').convert_alpha())
BLOCK2_IMAGE = pygame.transform.scale2x(pygame.image.load('Maka/assets/num2.png').convert_alpha())
BLOCK3_IMAGE = pygame.transform.scale2x(pygame.image.load('Maka/assets/num3.png').convert_alpha())
BLOCK4_IMAGE = pygame.transform.scale2x(pygame.image.load('Maka/assets/num4.png').convert_alpha())

# Buttons
ADD_BUTTON = button.Button(990, 125, ADD_IMAGE, 0.5)
SUB_BUTTON = button.Button(990, 275, SUB_IMAGE, 0.5)
MUL_BUTTON = button.Button(990, 425, MUL_IMAGE, 0.5)
DIV_BUTTON = button.Button(990, 575, DIV_IMAGE, 0.5)

BLOCK1 = button.Button(200, 200, BLOCK1_IMAGE, 0.5)
BLOCK2 = button.Button(650, 200, BLOCK2_IMAGE, 0.5)
BLOCK3 = button.Button(200, 500, BLOCK3_IMAGE, 0.5)
BLOCK4 = button.Button(650, 500, BLOCK4_IMAGE, 0.5)

# Display funcs
def display_BG():
    screen.blit(BG_IMAGE, (0, 0))

def display_inner_windows():
    #Blocks
    inner1 = pygame.Surface((850, 600)).fill((0, 0, 0))
    inner1.x = 50
    inner1.y = 100
    pygame.draw.rect(screen, (60, 50, 50), inner1, 0, 0, 20, 20, 20, 0)
    #Operands
    inner2 = pygame.Surface((200, 600)).fill((0, 0, 0))
    inner2.x = 950
    inner2.y = 100
    pygame.draw.rect(screen, (60, 50, 50), inner2, 0, 0, 20, 20, 0, 20)
    #Result
    inner3 = pygame.Surface((850, 100)).fill((0, 0, 0))
    inner3.x = 50
    inner3.y = 750
    pygame.draw.rect(screen, (60, 50, 50), inner3, 0, 0, 20, 0, 20, 20)
    #Goal
    inner4 = pygame.Surface((200, 100)).fill((0, 0, 0))
    inner4.x = 950
    inner4.y = 750
    pygame.draw.rect(screen, (60, 50, 50), inner4, 0, 0, 0, 20, 20, 20)

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

def display_blocks():
    global CURRENT_BLOCK
    #Draw button
    BLOCK1.draw(screen)
    BLOCK2.draw(screen)
    BLOCK3.draw(screen)
    BLOCK4.draw(screen)
    #Save clicked button
    if BLOCK1.clicked:
        CURRENT_BLOCK = BLOCK1
    if BLOCK2.clicked:
        CURRENT_BLOCK = BLOCK2
    if BLOCK3.clicked:
        CURRENT_BLOCK = BLOCK3
    if BLOCK4.clicked:
        CURRENT_BLOCK = BLOCK4
    #Highlighting
    if CURRENT_BLOCK:
        pygame.draw.rect(screen, (0, 120, 155), CURRENT_BLOCK.rect, 4)

#                                                   MAIN LOOP
while RUNNING:

    clock.tick(120)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if CURRENT_BLOCK:
            BLOCK = CURRENT_BLOCK.rect
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if BLOCK.collidepoint(event.pos):
                        RECTANGLE_DRAGING = True
                        mouse_x, mouse_y = event.pos
                        offset_x = BLOCK.x - mouse_x
                        offset_y = BLOCK.y - mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:            
                    RECTANGLE_DRAGING = False

            elif event.type == pygame.MOUSEMOTION:
                if RECTANGLE_DRAGING:
                    mouse_x, mouse_y = event.pos
                    BLOCK.x = mouse_x + offset_x
                    BLOCK.y = mouse_y + offset_y
    
    display_BG()
    display_inner_windows()
    display_blocks()
    display_operands_buttons()

    pygame.display.flip()