"""
Main module
"""
import pygame
from sys import exit
import buttons
from Manager import Manager
from time import sleep

#                                               GLOBAL VARIABLES

    # Screen
pygame.init()
SCREEN_W = 1200
SCREEN_H = 900
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption('Maka')

    # Game
GAME = "running"
GOAL = 24
NUM1 = 1
NUM2 = 2
NUM3 = 3
NUM4 = 4

CURRENT_OP = None
CURRENT_NUM = None
RUNNING = True

clock = pygame.time.Clock()
BG_X = 0

    # Images
#Background
BG_IMAGE1 = pygame.transform.scale2x(pygame.image.load('Maka/assets/BG.JFIF').convert_alpha())
BG_IMAGE2 = pygame.transform.scale2x(pygame.image.load('Maka/assets/BG.JFIF').convert_alpha())
BG_IMAGE2 = pygame.transform.flip(BG_IMAGE2, True, False)
#Operands
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
#Game won
WON_FONT_SURFACE = GAME_FONT.render("GG", False, (255, 255, 255))
WON_FONT_RECT = GOAL_FONT_SURFACE.get_rect(center = (600, 450))

    # Buttons
#Operands
ADD_BUTTON = buttons.OpButton(990, 125, ADD_IMAGE, 0.4)
SUB_BUTTON = buttons.OpButton(990, 275, SUB_IMAGE, 0.4)
MUL_BUTTON = buttons.OpButton(990, 425, MUL_IMAGE, 0.4)
DIV_BUTTON = buttons.OpButton(990, 575, DIV_IMAGE, 0.4)
#Nums
num_group = Manager()
num1 = num_group.create_num_button(200, 200, NUM1)
num2 = num_group.create_num_button(650, 200, NUM2)
num3 = num_group.create_num_button(200, 500, NUM3)
num4 = num_group.create_num_button(650, 500, NUM4)

#                                               FUNCS
def display_BG():
    """Display endless moving background"""
    global BG_X
    screen.blit(BG_IMAGE1, (BG_X, 0))
    screen.blit(BG_IMAGE2, (BG_X + 2000, 0))
    screen.blit(BG_IMAGE1, (BG_X + 4000, 0))
    BG_X -= 2
    if BG_X <= - 4000:
        BG_X = 0

def display_inner_windows():
    """Display inner grey windows"""
    #Nums window
    inner1 = pygame.Surface((850, 600)).fill((0, 0, 0))
    inner1.x = 50
    inner1.y = 100
    pygame.draw.rect(screen, (60, 50, 50), inner1, 0, 0, 20, 20, 20, 0)
    #Result window
    inner3 = pygame.Surface((850, 100)).fill((0, 0, 0))
    inner3.x = 50
    inner3.y = 750
    pygame.draw.rect(screen, (60, 50, 50), inner3, 0, 0, 20, 0, 20, 20)

def display_operands_buttons():
    """Display and save the current operand button""" 
    global CURRENT_OP
    #Draw and save clicked button
    if ADD_BUTTON.draw_check_click(screen):
        CURRENT_OP = ADD_BUTTON
    elif SUB_BUTTON.draw_check_click(screen):
        CURRENT_OP = SUB_BUTTON
    elif MUL_BUTTON.draw_check_click(screen):
        CURRENT_OP = MUL_BUTTON
    elif DIV_BUTTON.draw_check_click(screen):
        CURRENT_OP = DIV_BUTTON
    #Highlighting
    if CURRENT_OP:
        pygame.draw.rect(screen, (120, 0, 155), CURRENT_OP.rect, 4)

def display_nums():
    """Display and update nums, and save the current number"""
    global CURRENT_NUM
    #Draw updated nums
    num_group.all_nums.update()
    num_group.draw(screen)
    #Save the clicked button to CURRENT_NUM
    nums = num_group.all_nums
    for num in nums:
        if num.get_clicked():
            CURRENT_NUM = num

def collide_nums():
    """Check collision and compute solution"""
    global CURRENT_NUM
    other_nums = [num1, num2, num3, num4]

    if not CURRENT_NUM:
        return
    if CURRENT_NUM in other_nums:
        other_nums.remove(CURRENT_NUM)
    if CURRENT_OP:
        for other_num in other_nums:
            if CURRENT_NUM.rect.colliderect(other_num.rect):
                if CURRENT_OP == ADD_BUTTON:
                    CURRENT_NUM.num += other_num.num
                    # Throwing the rect far away from screen because :
                    # persistent "rect ghost" after remove sprite,
                    # which was colliding with nums
                    other_num.rect.x = -2500
                elif CURRENT_OP == SUB_BUTTON:
                    CURRENT_NUM.num -= other_num.num
                    other_num.rect.x = -2500
                elif CURRENT_OP == MUL_BUTTON:
                    CURRENT_NUM.num *= other_num.num
                    other_num.rect.x = -2500
                elif CURRENT_OP == DIV_BUTTON:
                    CURRENT_NUM.num //= other_num.num
                    other_num.rect.x = -2500
                other_num.kill()
                return True

def game_state(game_status):
    """Return game state"""
    if CURRENT_NUM and CURRENT_NUM.num == GOAL:
        return "won"
    else:
        return "running"

#                                               MAIN LOOP
def main():
    global CURRENT_NUM
    rectangle_dragging = False
    game = "running"

    while RUNNING:
        #Event loop
        for event in pygame.event.get():
            #Quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            #Handle the drag & drop mechanic for NUM_BUTTONS
            if CURRENT_NUM:
                NUM = CURRENT_NUM
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if NUM.rect.collidepoint(event.pos):
                            rectangle_dragging = True
                            mouse_x, mouse_y = event.pos
                            offset_x = NUM.rect.x - mouse_x
                            offset_y = NUM.rect.y - mouse_y

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:            
                        rectangle_dragging = False
                        CURRENT_NUM.reset()


                elif event.type == pygame.MOUSEMOTION:
                    if rectangle_dragging:
                        mouse_x, mouse_y = event.pos
                        if 50 < mouse_x < 900 and 100 < mouse_y < 700:
                            NUM.x = mouse_x + offset_x
                            NUM.y = mouse_y + offset_y

        if game == "running":
            display_BG()
            screen.blit(TITLE_SURFACE, TITLE_RECT)
            display_inner_windows()
            display_nums()
            display_operands_buttons()
            screen.blit(GOAL_FONT_SURFACE, GOAL_FONT_RECT)
            if collide_nums():
                game = game_state(game)
        elif game == "won":
            display_BG()
            screen.blit(WON_FONT_SURFACE, WON_FONT_RECT)
        elif game == "over":
            pass

        pygame.display.flip()
        clock.tick(120)

main()