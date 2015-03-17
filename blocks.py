import math
import pygame
from tkinter import *
import random


black = (0, 0, 0)
white = (255, 255, 255)
green = (100, 200, 100)
yellow = (0, 0, 0)
lime = (  0, 255,   0)
blue =(  0,   0, 128)
red = (255,0,0)
purple = (0xBF,0x0F,0xB5)

block_width = 53
block_height = 30

class Block(pygame.sprite.Sprite):
    """This class represents each block that will get knocked out by the ball
    It derives from the "Sprite" class in Pygame """

    def __init__(self ,color,x ,y):
        
        
    
        super().__init_()
        
        self.image = pygame.Surface([block_width, block_height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
