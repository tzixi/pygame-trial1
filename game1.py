from cgitb import text
import pygame
from sys import exit
from random import randint

def display_score():
    current_time = str(int(pygame.time.get_ticks() /1000) - start_time)
    score_surf = test_font.render(current_time, False, 'Black')
    score_rect = score_surf.get_rect(midtop = (600, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface1, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else: return []

def collisions(player, obstacles):
    if obstacles:
        for obstacles_rect in obstacles:
            if player.colliderect(obstacles_rect):
                return False
    return True

#initializing pygame
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
game_active = False
start_time = 0
score = 0

# controls framerate
clock = pygame.time.Clock()

test_font = pygame.font.Font('font/Pixeltype.ttf', 50) # font type, font size

sky_surface = pygame.image.load('graphics/Sky.png').convert() # this is the regular surface, the tuple inside is width, height
ground_surface = pygame.image.load('graphics/ground.png').convert() # adds ground surface

text_surface = test_font.render('My Game', False, 'Black') # text, text smoothing, colour
text_rect = text_surface.get_rect(midtop = (400, 50))

# obstacles
snail_surface1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_surface2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()

fly_surf = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()

obstacle_rect_list = []

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0

# intro screen
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2) # surface, angle, scale
playerstand_rect = player_stand.get_rect(center = (400, 200))

game_name = test_font.render('PIXEL RUNNER', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (400, 80))

restart_surface = test_font.render('PRESS ENTER TO START', False, (111, 196, 169))
restart_rect = restart_surface.get_rect(center = (400, 330))

# timer
obstacle_timer = pygame.USEREVENT + 1 # plus 1 to deconflict
pygame.time.set_timer(obstacle_timer, 900)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #opposite to pygame init
            exit() #exits the loop and removes 'video system not initialised'
        
        if game_active:
            # if event.type == pygame.MOUSEMOTION:
            #     if player_rect.collidepoint(event.pos):
            #         player_gravity = -20
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -20
            
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if player_rect.collidepoint(event.pos):
            #         player_gravity = -20
        
            if event.type == obstacle_timer:
                if randint(0, 2):
                    obstacle_rect_list.append(snail_surface1.get_rect(midbottom = (randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(midbottom = (randint(900, 1100), 200)))

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_active = True
                    player_rect.left = 80
                    start_time = int(pygame.time.get_ticks() /1000)

        
    
    if game_active:    
        screen.blit(sky_surface,(0,0)) #surface, position
        screen.blit(ground_surface,(0, 300))
        pygame.draw.rect(screen, '#c0e8ec', text_rect)
        pygame.draw.rect(screen, '#c0e8ec', text_rect, 10)
        screen.blit(text_surface, text_rect)
        score = display_score()

        # player
        player_gravity += 1
        player_rect.bottom += player_gravity
        if player_rect.bottom >= 300: 
            player_rect.bottom = 300 # simulates collision with the ground
        screen.blit(player_surf, player_rect)

        # player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            player_rect.right += 3
        if keys[pygame.K_LEFT]:
            player_rect.left -= 3

        # obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # collisions
        game_active = collisions(player_rect, obstacle_rect_list)

    # game over screen
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, playerstand_rect)
        score_message = test_font.render(f'Your score: {score}', False, (111, 196, 169))
        score_rect = score_message.get_rect(midtop = (400, 330))
        screen.blit(game_name, game_name_rect)
        
        if score == 0:
            screen.blit(restart_surface, restart_rect)
        else:
            screen.blit(score_message, score_rect)
    
    pygame.display.update() #updates the display
    clock.tick(60) #fps
