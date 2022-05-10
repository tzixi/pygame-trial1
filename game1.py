from cgitb import text
import pygame
from sys import exit

#initializing pygame
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')

#controls framerate
clock = pygame.time.Clock()

test_font = pygame.font.Font('font/Pixeltype.ttf', 50) # font type, font size

sky_surface = pygame.image.load('graphics/Sky.png').convert() # this is the regular surface, the tuple inside is width, height
ground_surface = pygame.image.load('graphics/ground.png').convert() # adds ground surface

text_surface = test_font.render('My Game', False, 'Black') # test, text smoothing, colour
text_rect = text_surface.get_rect(midtop = (400, 50))

snail_surface1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect1 = snail_surface1.get_rect(midbottom = (600, 300))
snail_surface2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()

player_surf = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #opposite to pygame init
            exit() #exits the loop and removes 'video system not initialised'
       
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         player_gravity = -20
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_gravity = -20
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos):
                player_gravity = -20
    
    screen.blit(sky_surface,(0,0)) #surface, position
    screen.blit(ground_surface,(0, 300))
    pygame.draw.rect(screen, '#c0e8ec', text_rect)
    pygame.draw.rect(screen, '#c0e8ec', text_rect, 10)
    screen.blit(text_surface, text_rect)

    # snail
    snail_rect1.left -= 3
    if snail_rect1.left < -100:
        snail_rect1.left = 800
    screen.blit(snail_surface1, snail_rect1)

    # player
    # if player_rect.bottom < 300:
    #     player_gravity += 1
    #     player_rect.bottom += player_gravity
    player_gravity += 1
    player_rect.bottom += player_gravity
    screen.blit(player_surf, player_rect)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print('Jump')

    pygame.display.update() #updates the display
    clock.tick(60) #fps
