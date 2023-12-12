#--// IMPORTS
import pygame as Pygame

#--// VARIABLES
# MAIN
Running: bool    = True
renderSpeed: int = 60
deltaTime: int   = 0
screenResolution: tuple = (
    1920, #-- WIDTH
    1080  #-- HEIGHT
)
# PYGAME
Clock   = Pygame.time.Clock()
Image   = Pygame.image
Vector2 = Pygame.Vector2

#--// PRE-STREAM
Pygame.init()
coreWindow = Pygame.display.set_mode(screenResolution, Pygame.FULLSCREEN)
backgroundGroup = Pygame.sprite.Group()
obstacleGroup   = Pygame.sprite.Group()
playerGroup     = Pygame.sprite.Group()

#--// OBJECT CLASSES
class coreObject(Pygame.sprite.Sprite):
    def __init__(self, Config: dict=None):
        super().__init__()

        if Config:
            self.originalImage = Image.load(Config.Sprite).convert_alpha()
            self.Rectangle     = self.originalImage.get_rect()
            self.Position      = Vector2(
                Config.Position[1],
                Config.Position[2]
            )

    def update(self):
        pass

#--// PLAYER CREATION
# playerSprite = coreObject({ #-- PLAYER OBJECT
#     "Sprite": "Sprites/Player/playerCar.png"
# })
# playerGroup.add(playerSprite) #-- ADD PLAYER TO SPRITE GROUP

#--// RENDERING STREAM 
while Running:
    # UPDATE EVENTS
    for Event in Pygame.event.get():
        if Event.type == Pygame.QUIT:
            Running = False
            break

    # SPRITE UPDATES
    # playerGroup.update()
    
    # FLIP AND DELTA TIME
    Pygame.display.flip()
    deltaTime = Clock.tick(renderSpeed) / 1000

# QUIT APPLICATION
Pygame.quit()
