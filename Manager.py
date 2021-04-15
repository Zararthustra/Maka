"""
Manager module
"""
import pygame
from buttons import NumButton


class NumManager():
    """
    Manage NumButton sprites group
    """

    def __init__(self):
        """Constructor"""
        self.all_nums = pygame.sprite.Group()

    def create_num_button(self, x, y, number):
        """Create and return an instance with args"""
        num = NumButton(x, y, number)
        self.all_nums.add(num)
        return num
    
    def draw(self, screen):
        """Draw function"""
        self.all_nums.draw(screen)

    def remove(self, num):
        """Remove function"""
        self.all_nums.remove(num)

