"""
Main module
"""
import pygame
from sys import exit
import button


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

# Images
BG_IMAGE = pygame.transform.scale2x(pygame.image.load('Maka/assets/BG.JFIF').convert_alpha())
ADD_IMAGE = pygame.transform.scale2x(pygame.image.load('Maka/assets/plus.png').convert_alpha())
SUB_IMAGE = pygame.transform.scale2x(pygame.image.load('Maka/assets/moins.png').convert_alpha())
MUL_IMAGE = pygame.transform.scale2x(pygame.image.load('Maka/assets/fois.png').convert_alpha())
DIV_IMAGE = pygame.transform.scale2x(pygame.image.load('Maka/assets/divise.png').convert_alpha())

# Display funcs
def display_BG():
    screen.blit(BG_IMAGE, (0, 0))

def display_inner_windows():
    #Blocks
    inner1 = pygame.Surface((850, 600)).fill((0, 0, 0))
    inner1.x = 50
    inner1.y = 100
    pygame.draw.rect(screen, (60, 50, 50), inner1)
    #Operands
    inner2 = pygame.Surface((200, 600)).fill((0, 0, 0))
    inner2.x = 950
    inner2.y = 100
    pygame.draw.rect(screen, (60, 50, 50), inner2)
    #Result
    inner3 = pygame.Surface((850, 100)).fill((0, 0, 0))
    inner3.x = 50
    inner3.y = 750
    pygame.draw.rect(screen, (60, 50, 50), inner3)
    #Goal
    inner4 = pygame.Surface((200, 100)).fill((0, 0, 0))
    inner4.x = 950
    inner4.y = 750
    pygame.draw.rect(screen, (60, 50, 50), inner4)

def display_operands_buttons():
    add_button = button.Button(990, 125, ADD_IMAGE, 0.5)
    sub_button = button.Button(990, 275, SUB_IMAGE, 0.5)
    mul_button = button.Button(990, 425, MUL_IMAGE, 0.5)
    div_button = button.Button(990, 575, DIV_IMAGE, 0.5)

    add_button.draw(screen)
    sub_button.draw(screen)
    mul_button.draw(screen)
    div_button.draw(screen)

# Game
RUNNING = True

#                                               CLASS DEFINITION


#                                                   MAIN LOOP
while RUNNING:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    display_BG()
    display_inner_windows()
    display_operands_buttons()
    pygame.display.update()