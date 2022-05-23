import pygame,random
from pygame.locals import *

class Rock(pygame.sprite.Sprite):

    def __init__(self,isTop):
        super().__init__()
        self.images = {
            True: pygame.transform.smoothscale(pygame.image.load("images/rockDown.png"),(40,150)),
            False: pygame.transform.smoothscale(pygame.image.load("images/rock.png"),(40,150))
        }
        self.isTop = isTop
        self.image = self.images[self.isTop]
        self.rect = self.image.get_rect()

        if self.isTop:
            self.rect.top = random.randint(-100,0)
        else:
            self.rect.bottom = 400 + random.randint(0,100)

        self.speed = [-2,0]

    def update(self):
        self.rect.move_ip(self.speed)

        if self.rect.left < 0:
            self.rect.left = 700
            if self.isTop:
                self.rect.top = random.randint(-100,0)
            else:
                self.rect.bottom = 400 + random.randint(0,100)


    def draw(self,screen):
        screen.blit(self.image,self.rect)


