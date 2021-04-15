"""
Main module
"""
import pygame
from sys import exit
import buttons
from Manager import NumManager
from time import sleep


#                                               GLOBAL VARIABLES
#------------------------------------------------------------------------------------------------------------
    # Screen
pygame.init()
SCREEN_W = 1200
SCREEN_H = 600
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption('The Good Count')

    # Game
GAME = "running"

CURRENT_OP = None
CURRENT_NUM = None
RUNNING = True

clock = pygame.time.Clock()
BG_X = 0

    # Images
#Background
BG_IMAGE1 = pygame.image.load('Maka/assets/BG.JFIF').convert_alpha()
BG_IMAGE2 = pygame.image.load('Maka/assets/BG.JFIF').convert_alpha()
BG_IMAGE2 = pygame.transform.flip(BG_IMAGE2, True, False)
#Operands
ADD_IMAGE = pygame.image.load('Maka/assets/add.png').convert_alpha()
SUB_IMAGE = pygame.image.load('Maka/assets/sub.png').convert_alpha()
MUL_IMAGE = pygame.image.load('Maka/assets/mul.png').convert_alpha()
DIV_IMAGE = pygame.image.load('Maka/assets/div.png').convert_alpha()

    # Fonts
GAME_FONT = pygame.font.Font('Maka/assets/MAGNETOB.TTF', 50)
TITLE_FONT = pygame.font.Font('Maka/assets/MAGNETOB.TTF', 100)
#Levels
LEVEL1_SURFACE = GAME_FONT.render("Level 1", False, (255, 230, 230))
LEVEL1_RECT = LEVEL1_SURFACE.get_rect(center = (475, 30))

LEVEL2_SURFACE = GAME_FONT.render("Level 2", False, (255, 230, 230))
LEVEL2_RECT = LEVEL2_SURFACE.get_rect(center = (475, 30))

LEVEL3_SURFACE = GAME_FONT.render("Level 3", False, (255, 230, 230))
LEVEL3_RECT = LEVEL3_SURFACE.get_rect(center = (475, 30))
#Intro
INTRO_FONT_SURFACE1 = TITLE_FONT.render("The Good Count", False, (255, 255, 255))
INTRO_FONT_RECT1 = INTRO_FONT_SURFACE1.get_rect(center = (600, 250))

INTRO_FONT_SURFACE2 = GAME_FONT.render("Click to start", False, (255, 255, 255))
INTRO_FONT_RECT2 = INTRO_FONT_SURFACE2.get_rect(center = (600, 350))

INTRO_FONT_SURFACE3 = GAME_FONT.render("Press space to restart", False, (255, 255, 255))
INTRO_FONT_RECT3 = INTRO_FONT_SURFACE3.get_rect(center = (600, 450))
#Game won
WON_FONT_SURFACE1 = TITLE_FONT.render("Good Count !", False, (255, 255, 255))
WON_FONT_RECT1 = WON_FONT_SURFACE1.get_rect(center = (600, 250))

WON_FONT_SURFACE2 = GAME_FONT.render("Click for next level", False, (255, 255, 255))
WON_FONT_RECT2 = WON_FONT_SURFACE2.get_rect(center = (600, 350))

    # Buttons
#Operands
ADD_BUTTON = buttons.OpButton(1000, 25, ADD_IMAGE, 0.4)
SUB_BUTTON = buttons.OpButton(1000, 175, SUB_IMAGE, 0.4)
MUL_BUTTON = buttons.OpButton(1000, 325, MUL_IMAGE, 0.4)
DIV_BUTTON = buttons.OpButton(1000, 475, DIV_IMAGE, 0.4)
#Num sprite group
num_group = NumManager()

#                                               FUNCS
#------------------------------------------------------------------------------------------------------------

def display_BG():
    """Display endless moving background"""
    global BG_X
    screen.blit(BG_IMAGE1, (BG_X, 0))
    screen.blit(BG_IMAGE2, (BG_X + 1000, 0))
    screen.blit(BG_IMAGE1, (BG_X + 2000, 0))
    BG_X -= 2
    if BG_X <= - 2000:
        BG_X = 0

def display_inner_window():
    """Display the inner grey window"""
    inner1 = pygame.Surface((850, 500)).fill((0, 0, 0))
    inner1.x = 50
    inner1.y = 50
    pygame.draw.rect(screen, (60, 50, 50), inner1, 0, 0, 20, 20, 20, 20)

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

def display_remain():
    """Display number remaining to reach goal, during calculation"""
    remain = GOAL - CURRENT_NUM.num if CURRENT_NUM else GOAL
    curr = CURRENT_NUM.num if CURRENT_NUM else 0
    result = "Actual: {}        Goal: {}        Need: {}".format(curr, GOAL, remain)

    font = pygame.font.Font('Maka/assets/MAGNETOB.TTF', 30)
    surface = font.render(str(result), False, (255, 255, 255))
    rect = surface.get_rect(topleft = (150, 560))
    screen.blit(surface, rect)

def collide_nums():
    """Check collision and compute solution"""
    global CURRENT_NUM
    global CURRENT_OP
    other_nums = list(num_group.all_nums)

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
    if CURRENT_NUM.num == GOAL:
        CURRENT_OP = None

def reset_nums(number1, number2, number3, number4, goal):
    global GOAL
    num1 = num_group.create_num_button(160, 110, number1)
    num2 = num_group.create_num_button(700, 110, number2)
    num3 = num_group.create_num_button(160, 375, number3)
    num4 = num_group.create_num_button(700, 375, number4)
    GOAL = goal

#                                               STAGE MANAGER CLASS
#------------------------------------------------------------------------------------------------------------
class StageManager():
    """
    Manage all stages (intro, levels, game over)
    """

    def __init__(self):
        """Constructor"""
        self.state = "intro"
        self.level = 1

    def state_manager(self):
        """Switch game stage"""
        #Intro
        if self.state == "intro":
            self.intro()
        #Levels
        elif self.state == "level1switch":
            reset_nums(6, 2, 10, 7, 31)
            self.state = "level1"
        elif self.state == "level1":
            self.main()
            screen.blit(LEVEL1_SURFACE, LEVEL1_RECT)
        elif self.state == "level2switch":
            reset_nums(12, 8, 3, 1, 33)
            self.state = "level2"
        elif self.state == "level2":
            self.main()
            screen.blit(LEVEL2_SURFACE, LEVEL2_RECT)
        elif self.state == "level3switch":
            reset_nums(13, 3, 4, 26, 27)
            self.state = "level3"
        elif self.state == "level3":
            self.main()
            screen.blit(LEVEL3_SURFACE, LEVEL3_RECT)
        #Game over
        elif self.state == "won":
            self.won()

    def intro(self):
        """Intro stage"""
        #Event loop
        for event in pygame.event.get():
            #Quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            #Click to start
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = "level{}switch".format(self.level)

        display_BG()
        screen.blit(INTRO_FONT_SURFACE1, INTRO_FONT_RECT1)
        screen.blit(INTRO_FONT_SURFACE2, INTRO_FONT_RECT2)
        screen.blit(INTRO_FONT_SURFACE3, INTRO_FONT_RECT3)

    def main(self):
        """Main stage"""
        display_BG()
        display_inner_window()
        display_remain()
        display_nums()
        display_operands_buttons()
        collide_nums()
        #Switch to "won" state
        if CURRENT_NUM and CURRENT_NUM.num == GOAL:
            self.state = "won"

    def won(self):
        """Clear sprite group and current num then switch to next level"""
        global CURRENT_NUM

        num_group.all_nums.empty()
        CURRENT_NUM = None

        for event in pygame.event.get():
            #Quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            #Click to switch level
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.level += 1
                self.state = "level{}switch".format(self.level)

        display_BG()
        screen.blit(WON_FONT_SURFACE1, WON_FONT_RECT1)
        screen.blit(WON_FONT_SURFACE2, WON_FONT_RECT2)

#                                               MAIN LOOP
#------------------------------------------------------------------------------------------------------------
def main():

    global CURRENT_NUM
    rectangle_dragging = False
    game_state = StageManager()
    
    while RUNNING:

        game_state.state_manager()

        #Event loop
        for event in pygame.event.get():
            #Quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            #Restart level
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    num_group.all_nums.empty()
                    CURRENT_NUM = None
                    game_state.state = "level{}switch".format(game_state.level)
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
                        NUM.reset()

                if event.type == pygame.MOUSEMOTION:
                    if rectangle_dragging:
                        mouse_x, mouse_y = event.pos
                        if 50 < mouse_x < 900 and 100 < mouse_y < 700:
                            NUM.x = mouse_x + offset_x
                            NUM.y = mouse_y + offset_y
        
        pygame.display.flip()
        clock.tick(60)

main()