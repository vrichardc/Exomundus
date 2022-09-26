import pygame

from MainMenu import *

pygame.init()

global gameDisplay
screen_size = (1920,1080)
gameDisplay = pygame.display.set_mode(screen_size,pygame.FULLSCREEN)

clock = pygame.time.Clock()
pygame.display.set_caption('Exomundus')


crashed = False
while not crashed:

    Main_Menu(gameDisplay)

    clock.tick(60)


pygame.quit()
quit()
