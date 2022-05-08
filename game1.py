import pygame
from sys import exit

#initializing pygame
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')

#controls framerate
clock = pygame.time.Clock()

sky_surface = pygame.image.load('graphics/Sky.png') # this is the regular surface, the tuple inside is width, height

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #opposite to pygame init
            exit() #exits the loop and removes 'video system not initialised'
    
    screen.blit(sky_surface,(0,0)) #surface, position
    
    pygame.display.update() #updates the display
    clock.tick(60) #fps
