import pygame

TITLE_FONT = pygame.font.Font('The_good_count/assets/MAGNETOB.TTF', 100)
LEVEL_FONT = pygame.font.Font('The_good_count/assets/MAGNETOB.TTF', 50)
GAME_FONT = pygame.font.Font('The_good_count/assets/BRITANIC.TTF', 50)


# Levels

LEVEL1_SURFACE = LEVEL_FONT.render("Level 1", False, (255, 230, 230))
LEVEL1_RECT = LEVEL1_SURFACE.get_rect(center = (475, 30))

LEVEL2_SURFACE = LEVEL_FONT.render("Level 2", False, (255, 230, 230))
LEVEL2_RECT = LEVEL2_SURFACE.get_rect(center = (475, 30))

LEVEL3_SURFACE = LEVEL_FONT.render("Level 3", False, (255, 230, 230))
LEVEL3_RECT = LEVEL3_SURFACE.get_rect(center = (475, 30))

LEVEL4_SURFACE = LEVEL_FONT.render("Level 4", False, (255, 230, 230))
LEVEL4_RECT = LEVEL4_SURFACE.get_rect(center = (475, 30))

LEVEL5_SURFACE = LEVEL_FONT.render("Level 5", False, (255, 230, 230))
LEVEL5_RECT = LEVEL5_SURFACE.get_rect(center = (475, 30))

LEVEL6_SURFACE = LEVEL_FONT.render("Level 6", False, (255, 230, 230))
LEVEL6_RECT = LEVEL6_SURFACE.get_rect(center = (475, 30))

LEVEL7_SURFACE = LEVEL_FONT.render("Level 7", False, (255, 230, 230))
LEVEL7_RECT = LEVEL7_SURFACE.get_rect(center = (475, 30))

LEVEL8_SURFACE = LEVEL_FONT.render("Level 8", False, (255, 230, 230))
LEVEL8_RECT = LEVEL8_SURFACE.get_rect(center = (475, 30))

LEVEL9_SURFACE = LEVEL_FONT.render("Level 9", False, (255, 230, 230))
LEVEL9_RECT = LEVEL9_SURFACE.get_rect(center = (475, 30))

LEVEL10_SURFACE = LEVEL_FONT.render("Level 10", False, (255, 230, 230))
LEVEL10_RECT = LEVEL10_SURFACE.get_rect(center = (475, 30))


# Intro

INTRO_FONT_SURFACE1 = TITLE_FONT.render("The Good Count", False, (255, 255, 255))
INTRO_FONT_RECT1 = INTRO_FONT_SURFACE1.get_rect(center = (600, 250))

INTRO_FONT_SURFACE2 = GAME_FONT.render("Start game", False, (100, 100, 100))
INTRO_FONT_RECT2 = INTRO_FONT_SURFACE2.get_rect(center = (600, 450))

INTRO_FONT_SURFACE3 = GAME_FONT.render("Quick tutorial", False, (100, 100, 100))
INTRO_FONT_RECT3 = INTRO_FONT_SURFACE3.get_rect(center = (600, 500))

# Tuto


# Stage won

WON_FONT_SURFACE1 = TITLE_FONT.render("Good Count !", False, (255, 255, 255))
WON_FONT_RECT1 = WON_FONT_SURFACE1.get_rect(center = (600, 250))

WON_FONT_SURFACE2 = GAME_FONT.render("Click for next level", False, (255, 255, 255))
WON_FONT_RECT2 = WON_FONT_SURFACE2.get_rect(center = (600, 350))


# Game over

OVER_FONT_SURFACE1 = TITLE_FONT.render("Congratulation", False, (255, 255, 255))
OVER_FONT_RECT1 = OVER_FONT_SURFACE1.get_rect(center = (600, 150))

OVER_FONT_SURFACE2 = TITLE_FONT.render("You win !!!", False, (255, 255, 255))
OVER_FONT_RECT2 = OVER_FONT_SURFACE2.get_rect(center = (600, 250))

OVER_FONT_SURFACE3 = GAME_FONT.render("Click to restart the game", False, (255, 255, 255))
OVER_FONT_RECT3 = OVER_FONT_SURFACE3.get_rect(center = (600, 350))