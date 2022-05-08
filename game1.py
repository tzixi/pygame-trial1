import pygame
from sys import exit

#initializing pygame
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #opposite to pygame init
            exit() #exits the loop and removes 'video system not initialised'
    #draw all of our elements
    #update everything
    pygame.display.update() #updates the display



