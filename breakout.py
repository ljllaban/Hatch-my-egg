
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

block_width = 53
block_height = 30

class Block(pygame.sprite.Sprite):
    

    def __init__(self, color, x, y):
        """ Constructor. Pass in the color of the block, 
            and its x and y position. """ # Jesus Abordo
        
        
        super().__init__()
        
        # Create the image of the block of appropriate size
    
        self.image = pygame.Surface([block_width, block_height])
        
        # Fill the image with the appropriate color
        self.image.fill(color)
        
        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()
        
        
        # This is where our block will appear..
        self.rect.x = x
        self.rect.y = y

class Ball(pygame.sprite.Sprite):
    """ This class represents the ball        
        """
    
    speed = 10.0
    
    x = 0.0
    y = 180.0
    
    direction = 200

    width = 10 
    height = 10

    
    def __init__(self):
        
        super().__init__()
        
        self.image = pygame.image.load("ball1.png")
        
        self.rect = self.image.get_rect()
        
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
    
    def bounce(self, diff):
        """ This function will bounce the ball 
            off a horizontal surface (not a vertical one) """
        
        self.direction = (180 - self.direction) % 360
        self.direction -= diff
    
    def update(self):
        """ Update the position of the ball. """
        direction_radians = math.radians(self.direction)
        
        self.x += self.speed * math.sin(direction_radians)
        self.y -= self.speed * math.cos(direction_radians)
        
        self.rect.x = self.x
        self.rect.y = self.y
        
        if self.y <= 0:
            self.bounce(0)
            self.y = 1
            
        if self.x <= 0:
            self.direction = (360 - self.direction) % 360
            self.x = 1
            
        if self.x > self.screenwidth - self.width:
            self.direction = (360 - self.direction) % 360
            self.x = self.screenwidth - self.width - 1
        
        if self.y > 600:
            return True
        else:
            return False

class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player controls. """
    
    def __init__(self):
        """ Constructor for Player. """
        super().__init__()
        
        self.width = 75
        self.height = 15
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((black))
        
        self.rect = self.image.get_rect()
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()

        self.rect.x = 0
        self.rect.y = self.screenheight-self.height
    
    def update(self):
        """ Update the player position. """
        
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        if self.rect.x > self.screenwidth - self.width:
            self.rect.x = self.screenwidth - self.width

    
play=True
while play:

    pygame.init()

    screen = pygame.display.set_mode([1100, 600])

    pygame.display.set_caption('Breakout')

    pygame.mouse.set_visible(1)

    font = pygame.font.Font(None, 36)

    background = pygame.Surface(screen.get_size())


    blocks = pygame.sprite.Group()
    balls = pygame.sprite.Group()
    allsprites = pygame.sprite.Group()


    player = Player()
    allsprites.add(player)


    ball = Ball()
    allsprites.add(ball)
    balls.add(ball)

    top = 80


    blockcount = 20

    # --- Create blocks


    for row in range(5):
        
        for column in range(0, blockcount):
            
            block = Block(white, column * (block_width + 2) + 1, top)
            blocks.add(block)
            allsprites.add(block)
        
        top += block_height + 2

    clock = pygame.time.Clock()

    # Is the game over?
    game_over = False


    # Exit the program?
    exit_program = False

    # Main program loop
    while exit_program != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 exit_program=True
                 play = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            exit_program=True
                    #__init__()
        # Limit to 30 fps
        clock.tick(30)

        # Clear the screen
        screen.fill(lime)
        
        # Process the events in the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_program = True
        
        # Update the ball and player position as long
        # as the game is not over.
        if not game_over:
            # Update the player and ball positions
            player.update()
            game_over = ball.update()
           

        # If we are done, print game over
        if game_over:
            text = font.render("GAME OVER", True, white)
            textpos = text.get_rect(centerx=background.get_width()/2)
            textpos.top = 300
            screen.blit(text, textpos)
           
        # See if the ball hits the player paddle
        if pygame.sprite.spritecollide(player, balls, False):
            # The 'diff' lets you try to bounce the ball left or right 
            # depending where on the paddle you hit it
            diff = (player.rect.x + player.width/2) - (ball.rect.x+ball.width/2)
            
            # Set the ball's y position in case 
            # we hit the ball on the edge of the paddle
            ball.rect.y = screen.get_height() - player.rect.height - ball.rect.height - 1
            ball.bounce(diff)
        
        # Check for collisions between the ball and the blocks
        deadblocks = pygame.sprite.spritecollide(ball, blocks, True)
        
        # If we actually hit a block, bounce the ball
        if len(deadblocks) > 0:
            ball.bounce(0)
            
            # Game ends if all the blocks are gone
            if len(blocks) == 0:
                game_over = True
        
        # Draw Everything
        allsprites.draw(screen)

        # Flip the screen and show what we've drawn
        pygame.display.flip()
#pygame.quit()
