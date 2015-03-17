class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player controls. """
    
    def __init__(self):
        """ Constructor for Player. """
        super().__init__()
        
        self.width = 75
        self.height = 15
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((white))
        
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
