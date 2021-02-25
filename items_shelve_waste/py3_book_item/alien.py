import sys
import pygame
from settings import Settings #add
from ship import Ship #add

def run_game():
    pygame.init() 
    ai_settings = Settings() #add
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) #xiu 
    pygame.display.set_caption("Alien Invasion") 
    bg_color = (230,230,230) 
    ship = Ship(screen) #add
    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                sys.exit() 
        screen.fill(ai_settings.bg_color) #修
        ship.blitme()
        pygame.display.flip() 

run_game()
