"""
Main module
"""
import pygame
from sys import exit
import buttons
from Manager import NumManager
from fonts import *
from images import *
import re


#------------------------------------------------------------------------------------------------------------
#                                               GLOBAL VARIABLES
#------------------------------------------------------------------------------------------------------------
    # Screen
SCREEN_W = 1200
SCREEN_H = 600
pygame.init()
pygame.display.set_caption('The Good Count')
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

    # Game
CURRENT_OP = None
CURRENT_NUM = None
RUNNING = True

clock = pygame.time.Clock()
START_TIME = 0
STAGE_TIME = 0
BG_X = 0

    # Buttons
#Operators
ADD_BUTTON = buttons.OpButton(1000, 25, ADD_IMAGE, ADD_CLICKED_IMAGE, 0.4)
SUB_BUTTON = buttons.OpButton(1000, 175, SUB_IMAGE, SUB_CLICKED_IMAGE, 0.4)
MUL_BUTTON = buttons.OpButton(1000, 325, MUL_IMAGE, MUL_CLICKED_IMAGE, 0.4)
DIV_BUTTON = buttons.OpButton(1000, 475, DIV_IMAGE, DIV_CLICKED_IMAGE, 0.4)
#Num sprite group
num_group = NumManager()


#------------------------------------------------------------------------------------------------------------
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

def display_operators_buttons():
    """Display and save the current operand button""" 
    global CURRENT_OP

    pygame.draw.line(screen, (0, 0, 0), (900, 80), (900, 570))
    #Draw and save clicked button
    if ADD_BUTTON.draw_check_click(screen):
        CURRENT_OP = ADD_BUTTON
    elif SUB_BUTTON.draw_check_click(screen):
        CURRENT_OP = SUB_BUTTON
    elif MUL_BUTTON.draw_check_click(screen):
        CURRENT_OP = MUL_BUTTON
    elif DIV_BUTTON.draw_check_click(screen):
        CURRENT_OP = DIV_BUTTON

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

def collide_nums(goal):
    """Check collision and compute solution, return true when level finished"""
    global CURRENT_NUM
    global CURRENT_OP

    other_nums = list(num_group.all_nums)

    if not CURRENT_NUM:
        return
    #Remove current from all sprites, in order to check collision against others (and not himself)
    if CURRENT_NUM in other_nums:
        other_nums.remove(CURRENT_NUM)
    #Compute
    if CURRENT_OP:
        for other_num in other_nums:
            if CURRENT_NUM.rect.colliderect(other_num.rect):
                if CURRENT_OP == ADD_BUTTON:
                    CURRENT_NUM.num += other_num.num
                elif CURRENT_OP == SUB_BUTTON:
                    CURRENT_NUM.num -= other_num.num
                elif CURRENT_OP == MUL_BUTTON:
                    CURRENT_NUM.num *= other_num.num
                elif CURRENT_OP == DIV_BUTTON:
                    CURRENT_NUM.num //= other_num.num
                other_num.kill()
    #Check win condition
    if CURRENT_NUM.num == goal:
        CURRENT_OP = None
        return True

def timer(state, goal):
    """Display timer"""
    global START_TIME
    global STAGE_TIME

    time_init = pygame.time.get_ticks()
    
    #Save tick in variable to set stage timer
    if re.match(r'level\dswitch', state):
        START_TIME = pygame.time.get_ticks()

    #Clean stage time from milisecs to secs
    stage_timer = int((time_init - START_TIME) / 1000)
    
    TIMER_SURFACE = pygame.font.Font('The_good_count/assets/BRITANIC.TTF', 30).render("Timer: {}secs".format(stage_timer), False, (200, 200, 200))
    TIMER_RECT = TIMER_SURFACE.get_rect(center = (110, 35))
    if re.match(r'level\d', state) and not re.match(r'level\dswitch', state):
        screen.blit(TIMER_SURFACE, TIMER_RECT)

    if collide_nums(goal) == True:
        STAGE_TIME = stage_timer

#------------------------------------------------------------------------------------------------------------
#                                         STAGE MANAGER CLASS
#------------------------------------------------------------------------------------------------------------
class StageManager():
    """
    Manage all stages (intro, levels, game over)
    """

    def __init__(self, state):
        """Constructor"""
        self.state = state
        self.level = 1
        self.tuto_page = 1
        self.score = 0
        self.score_list = []
        self.goal = 99

    def display_level(self):
        """Display stage/level in full screen before starting it"""
        display_BG()

        LEVEL_SURFACE = TITLE_FONT.render("Stage {}".format(self.level), False, (255, 230, 230))
        LEVEL_RECT = LEVEL_SURFACE.get_rect(center = (600, 300))

        screen.blit(LEVEL_SURFACE, LEVEL_RECT)

    def state_manager(self):
        """Switch game stages"""
        #Intro
        if self.state == "intro":
            self.intro()
        #Flash Tuto
        elif self.state == "tuto":
            self.tuto()
        #Levels
        elif self.state == "level1switch":
            self.display_level()
        elif self.state == "reset1":
            self.reset_nums(6, 2, 10, 7, 31)
            self.state = "level1"
        elif self.state == "level1":
            self.main()
        elif self.state == "level2switch":
            self.display_level()
        elif self.state == "reset2":
            self.reset_nums(12, 8, 3, 1, 33)
            self.state = "level2"
        elif self.state == "level2":
            self.main()
        elif self.state == "level3switch":
            self.display_level()
        elif self.state == "reset3":
            self.reset_nums(13, 3, 4, 3, 27)
            self.state = "level3"
        elif self.state == "level3":
            self.main()
        elif self.state == "level4switch":
            self.display_level()
        elif self.state == "reset4":
            self.reset_nums(7, 20, 7, 2, 35)
            self.state = "level4"
        elif self.state == "level4":
            self.main()
        elif self.state == "level5switch":
            self.display_level()
        elif self.state == "reset5":
            self.reset_nums(44, 5, 15, 2, 19)
            self.state = "level5"
        elif self.state == "level5":
            self.main()
        elif self.state == "level6switch":
            self.display_level()
        elif self.state == "reset6":
            self.reset_nums(3, 90, 12, 3, 120)
            self.state = "level6"
        elif self.state == "level6":
            self.main()
        elif self.state == "level7switch":
            self.display_level()
        elif self.state == "reset7":
            self.reset_nums(3, 6, 9, 5, 99)
            self.state = "level7"
        elif self.state == "level7":
            self.main()
        elif self.state == "level8switch":
            self.display_level()
        elif self.state == "reset8":
            self.reset_nums(3, 2, 15, 26, 32)
            self.state = "level8"
        elif self.state == "level8":
            self.main()
        elif self.state == "level9switch":
            self.display_level()
        elif self.state == "reset9":
            self.reset_nums(17, 9, 12, 2, 57)
            self.state = "level9"
        elif self.state == "level9":
            self.main()
        elif self.state == "level10switch":
            self.display_level()
        elif self.state == "reset10":
            self.reset_nums(40, 7, 27, 2, 1)
            self.state = "level10"
        elif self.state == "level10":
            self.main()
        #Stage over
        elif self.state == "won":
            self.won()
        #Game over
        elif self.state == "over":
            self.over()
        elif self.state == "scores":
            self.scores()

    def intro(self):
        """Intro stage"""
        display_BG()
        screen.blit(INTRO_FONT_SURFACE1, INTRO_FONT_RECT1)
        screen.blit(INTRO_FONT_SURFACE2, INTRO_FONT_RECT2)
        screen.blit(INTRO_FONT_SURFACE3, INTRO_FONT_RECT3)

        pos = pygame.mouse.get_pos()
        #Event loop
        for event in pygame.event.get():
            #Quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
        #Click menu
        if INTRO_FONT_RECT2.collidepoint(pos):
            #Mouseover
            INTRO_FONT_SURFACE2B = GAME_FONT.render("Start game", False, (200, 200, 200))
            screen.blit(INTRO_FONT_SURFACE2B, INTRO_FONT_RECT2)
            if pygame.mouse.get_pressed()[0] == 1:
                self.state = "level{}switch".format(self.level)
        if INTRO_FONT_RECT3.collidepoint(pos):
            #Mouseover
            INTRO_FONT_SURFACE3B = GAME_FONT.render("Quick tutorial", False, (200, 200, 200))
            screen.blit(INTRO_FONT_SURFACE3B, INTRO_FONT_RECT3)
            if pygame.mouse.get_pressed()[0] == 1:
                self.state = "tuto"

    def tuto(self):
        """Flash tutorial to teach commands"""
        #Event loop
        for event in pygame.event.get():
            #Quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            #Click to switch pages
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.tuto_page += 1
        #Reset to intro
        if self.tuto_page == 6:
            self.state = "intro"
            self.tuto_page = 1

        #Tuto pages
        if self.tuto_page == 1:
            screen.blit(TUTO_IMAGE1, TUTO_RECT1)
        elif self.tuto_page == 2:
            screen.blit(TUTO_IMAGE2, TUTO_RECT2)
        elif self.tuto_page == 3:
            screen.blit(TUTO_IMAGE3, TUTO_RECT3)
        elif self.tuto_page == 4:
            screen.blit(TUTO_IMAGE4, TUTO_RECT4)
        elif self.tuto_page == 5:
            screen.blit(TUTO_IMAGE5, TUTO_RECT5)

    def main(self):
        """Main stage"""
        display_BG()
        display_nums()
        self.display_remain()
        display_operators_buttons()
        collide_nums(self.goal)
        #Switch to "won" or "over" state
        if CURRENT_NUM and CURRENT_NUM.num == self.goal:
            if self.level == 10:
                self.state = "over"
            else:
                self.state = "won"        
        self.reset_button()

    def won(self):
        """Clear sprite group and current num then switch to next level"""
        global CURRENT_NUM
        #Reset sprites
        num_group.all_nums.empty()
        CURRENT_NUM = None

        time = STAGE_TIME
        minutes, seconds = self.convert_to_minute(self.score + time)

        stage_time = GAME_FONT.render("Level completed in {} seconds".format(time), False, (255, 255, 255))
        current_score = GAME_FONT.render("Your actual score is {}min {}secs".format(minutes, seconds), False, (255, 255, 255))
        stage_time_rect = stage_time.get_rect(center = (600, 350))
        current_score_rect = current_score.get_rect(center = (600, 400))

        for event in pygame.event.get():
            #Quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            #Click to switch level
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.score += time
                self.score_list.append(time)
                self.level += 1
                self.state = "level{}switch".format(self.level)

        display_BG()
        screen.blit(WON_FONT_SURFACE1, WON_FONT_RECT1)
        screen.blit(stage_time, stage_time_rect)
        screen.blit(current_score, current_score_rect)
        screen.blit(WON_FONT_SURFACE2, WON_FONT_RECT2)

    def convert_to_minute(self, seconds):
        """Convert seconds score to min"""
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60

        return minutes, seconds

    def display_remain(self):
        """Display number remaining to reach goal, during calculation"""
        curr = CURRENT_NUM.num if CURRENT_NUM else 0
        rest = self.goal - curr
        result = "Goal: {}          Actual: {}         Rest: {}".format(self.goal, curr, rest)

        font = pygame.font.Font('The_good_count/assets/BRITANIC.TTF', 30)
        surface = font.render(str(result), False, (200, 200, 200))
        rect = surface.get_rect(center = (550, 35))
        screen.blit(surface, rect)

    def reset_button(self):
        """Reset level, but keep timer going on !"""
        pos = pygame.mouse.get_pos()

        screen.blit(RESET_SURFACEA, RESET_RECTA)

        if RESET_RECTA.collidepoint(pos):
            #Mouseover
            screen.blit(RESET_SURFACEB, RESET_RECTB)
            if pygame.mouse.get_pressed()[0] == 1:
                num_group.all_nums.empty()
                CURRENT_NUM = None
                self.state = "reset{}".format(self.level)

    def reset_nums(self, number1, number2, number3, number4, goal):
        global CURRENT_NUM

        num_group.all_nums.empty()
        CURRENT_NUM = None
        num1 = num_group.create_num_button(220, 190, number1)
        num2 = num_group.create_num_button(720, 190, number2)
        num3 = num_group.create_num_button(220, 455, number3)
        num4 = num_group.create_num_button(720, 455, number4)
        self.goal = goal

    def over(self):
        """Game over"""
        global CURRENT_NUM

        num_group.all_nums.empty()
        CURRENT_NUM = None
        minutes, seconds = self.convert_to_minute(self.score)
        total_score = GAME_FONT.render("Your total score is {}min {}secs ({}secs)".format(minutes, seconds, self.score), False, (255, 255, 255))
        total_score_rect = total_score.get_rect(center = (600, 400))

        for event in pygame.event.get():
            #Quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            #Click to see details
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = "scores"

        display_BG()
        screen.blit(OVER_FONT_SURFACE1, OVER_FONT_RECT1)
        screen.blit(OVER_FONT_SURFACE2, OVER_FONT_RECT2)
        screen.blit(total_score, total_score_rect)
        screen.blit(OVER_FONT_SURFACE3, OVER_FONT_RECT3)

    def scores(self):
        """Display score for each level"""
        for event in pygame.event.get():
            #Quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            #Click to restart game
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.level = 1
                self.state = "intro"

        display_BG()
        
        i = 1
        y = 50
        for score in self.score_list:
            table_score = GAME_FONT.render("Level{}: {}secs".format(i, score), False, (255, 255, 255))
            if i % 2 != 0:
                table_score_rect = table_score.get_rect(topleft = (150, y))
                screen.blit(table_score, table_score_rect)
            if i % 2 == 0:
                table_score_rect = table_score.get_rect(topleft = (700, y))
                screen.blit(table_score, table_score_rect)
                y += 100
                pass
            i += 1
        tot = GAME_FONT.render("Total: {}secs".format(self.score), False, (255, 255, 255))
        tot_rect = tot.get_rect(topleft = (400, 550))
        screen.blit(tot, tot_rect)


#------------------------------------------------------------------------------------------------------------
#                                               MAIN LOOP
#------------------------------------------------------------------------------------------------------------
def main():

    global CURRENT_NUM
    global STAGE_TIME
    rectangle_dragging = False
    game_state = StageManager("intro")
    
    while RUNNING:

        game_state.state_manager()

        #Event loop
        for event in pygame.event.get():
            #Quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if re.match(r'level\dswitch', game_state.state):
                        game_state.state = "reset{}".format(game_state.level)
            #Handle the drag & drop mechanic for NUM_BUTTONS
            if CURRENT_NUM:
                NUM = CURRENT_NUM
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if NUM.rect.collidepoint(event.pos):
                            rectangle_dragging = True
                            mouse_x, mouse_y = event.pos
                            offset_x = NUM.rect.centerx - mouse_x
                            offset_y = NUM.rect.centery - mouse_y

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:            
                        rectangle_dragging = False

                if event.type == pygame.MOUSEMOTION:
                    if rectangle_dragging:
                        mouse_x, mouse_y = event.pos
                        if 0 < mouse_x < 900 and 50 < mouse_y < 600:
                            NUM.x = mouse_x + offset_x
                            NUM.y = mouse_y + offset_y

        timer(game_state.state, game_state.goal)

        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

main()