class Ball(pygame.sprite.Sprite):
    
    
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
