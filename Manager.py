import pygame
from buttons import FontButton

class Manager():
    def __init__(self):
        self.all_nums = pygame.sprite.Group()

    def create_num_button(self, x, y, number):
        num = FontButton(x, y, number)
        self.all_nums.add(num)
        return num
    
    def draw(self, screen):
        self.all_nums.draw(screen)

    def remove(self, num):
        self.all_nums.remove(num)