import pygame

from colors import *


class Toggle_Button():
    def __init__(self, rect, screen, toggle, disabled):
        self.rect = rect
        self.screen = screen
        self.toggle = toggle
        self.disabled = disabled


    def clicked(self):
        if self.toggle == 0:
            self.toggle = 1
            return True
        else:
            self.toggle = 0
            return False


    def draw(self):
        if self.disabled == True:
            pygame.draw.rect(self.screen, D_GRAY, self.rect)
        else:
            if self.toggle == 1:
                pygame.draw.rect(self.screen, GREEN, self.rect)
            else:
                pygame.draw.rect(self.screen, RED, self.rect)



class Slider():
    def __init__(self, screen, position, value, circle_rect):
        self.screen = screen
        self.position = position
        self.value = value
        self.circle_rect = circle_rect


    def draw(self):
        pygame.draw.rect(self.screen, D_GRAY, pygame.Rect(self.position, (150, 7)))
        pygame.draw.circle(self.screen, RED, (self.position[0] + self.value, self.position[1] + 4), 10)



class Light():
    def __init__(self, position, radius, intensity, sprite):
        self.position = position
        self.radius = radius
        self.intensity = intensity

        self.sprite = sprite