#Tetris

import sys
import random
import pygame as game
from pygame.locals import *

game.init()

block_list = ["Stairs.png","Other L.png","Other Stairs.png","L.png","Square.png","Stick.png","Rocket Launcher.png"]
counter = 0

FPS = 20
FramesPerSec = game.time.Clock()

WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 850

DISPLAYSURF = game.display.set_mode((500,850))
DISPLAYSURF.fill(WHITE)
game.display.set_caption("Tetris Block Generator")

class Block(game.sprite.Sprite):
    global block_list
    global counter

    def __init__(self,image):
        super().__init__()

        self.image = game.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(100,SCREEN_WIDTH-100),0)

    def move(self):
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 850):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
            return True
        else:
            return False

    def key_move(self):
        key_press = game.key.get_pressed()

        if self.rect.right < SCREEN_WIDTH:
            if key_press[K_RIGHT]:
                self.rect.move_ip(10,0)
                
        if self.rect.left > 0:  
            if key_press[K_LEFT]:
                self.rect.move_ip(-10,0)
        

    def draw(self, surface):
        surface.blit(self.image, self.rect)

block = Block(block_list[0])

while True:
    for event in game.event.get():
        if event.type == QUIT:
            game.quit()
            sys.exit()

    block.key_move()

    if block.move() == True:
        if counter + 1 < len(block_list) or counter + 1 == len(block_list):
            block = Block(block_list[counter])
        else:
            counter = 0
            block = Block(block_list[counter])
    
    DISPLAYSURF.fill(WHITE)
    block.draw(DISPLAYSURF)
    game.display.update()
    FramesPerSec.tick(FPS)

    if counter +1 > 6:
        counter = 0
    else:
        counter += 1
