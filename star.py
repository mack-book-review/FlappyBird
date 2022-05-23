import pygame
from pygame.locals import *

class Star(pygame.sprite.Sprite):

    def __init__(self,pos,color_number):
        super().__init__()
        colors = [None,"Bronze","Silver","Gold"]
        self.points = color_number
        self.color = colors[self.points]
        self.image = pygame.image.load("images/star{}.png".format(self.color))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = [-2,0]


    def update(self):
        self.rect.move_ip(self.speed)
        if self.rect.left < 0:
            self.kill()

    def draw(self,screen):
        screen.blit(self.image,self.rect)