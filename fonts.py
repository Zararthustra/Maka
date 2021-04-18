import pygame

TITLE_FONT = pygame.font.Font('assets/MAGNETOB.TTF', 130)
LEVEL_FONT = pygame.font.Font('assets/MAGNETOB.TTF', 50)
GAME_FONT = pygame.font.Font('assets/BRITANIC.TTF', 50)


# Intro

INTRO_FONT_SURFACE1 = TITLE_FONT.render("The Good Count", False, (255, 255, 255))
INTRO_FONT_RECT1 = INTRO_FONT_SURFACE1.get_rect(center = (600, 250))

INTRO_FONT_SURFACE2 = GAME_FONT.render("Start game", False, (100, 100, 100))
INTRO_FONT_RECT2 = INTRO_FONT_SURFACE2.get_rect(center = (600, 450))

INTRO_FONT_SURFACE3 = GAME_FONT.render("Quick tutorial", False, (100, 100, 100))
INTRO_FONT_RECT3 = INTRO_FONT_SURFACE3.get_rect(center = (600, 500))


# Timer




# Stage won

WON_FONT_SURFACE1 = TITLE_FONT.render("Good Count !", False, (255, 255, 255))
WON_FONT_RECT1 = WON_FONT_SURFACE1.get_rect(center = (600, 200))

WON_FONT_SURFACE2 = GAME_FONT.render("Click for next level", False, (100, 100, 100))
WON_FONT_RECT2 = WON_FONT_SURFACE2.get_rect(center = (600, 550))


# Game over

OVER_FONT_SURFACE1 = TITLE_FONT.render("Congratulation", False, (255, 255, 255))
OVER_FONT_RECT1 = OVER_FONT_SURFACE1.get_rect(center = (600, 150))

OVER_FONT_SURFACE2 = TITLE_FONT.render("You win !!!", False, (255, 255, 255))
OVER_FONT_RECT2 = OVER_FONT_SURFACE2.get_rect(center = (600, 250))

OVER_FONT_SURFACE3 = GAME_FONT.render("Click to see details", False, (100, 100, 100))
OVER_FONT_RECT3 = OVER_FONT_SURFACE3.get_rect(center = (600, 550))