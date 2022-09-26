import pygame
from Players import *
from Dice import *
from MainMenu import *
from NewGame import *

pause_menu_image_dir = 'PauseMenu/pause_menu_image.png'
pause_menu_image = pygame.image.load(pause_menu_image_dir)
pause_menu_image_position = (600,200)

pause_limits1 = [(865, 251),(1250, 403)]
pause_limits2 = [(867, 432),(1252, 583)]
pause_limits3 = [(865, 603),(1250, 755)]

def pause_menu(display):
    global menu,starcard,star_card_pos
    pausemenu = True

    while pausemenu:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   pausemenu = False
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_position = pygame.mouse.get_pos()

                if mouse_position[0] >= pause_limits1[0][0] and mouse_position[0] <= pause_limits1[1][0] and mouse_position[1] >= pause_limits1[0][1] and mouse_position[1] <= pause_limits1[1][1]:
                    pausemenu = False

                if mouse_position[0] >= pause_limits2[0][0] and mouse_position[0] <= pause_limits2[1][0] and mouse_position[1] >= pause_limits2[0][1] and mouse_position[1] <= pause_limits2[1][1]:
                    #menu = True
                    #Main_Menu(display)
                    pass
                if mouse_position[0] >= pause_limits3[0][0] and mouse_position[0] <= pause_limits3[1][0] and mouse_position[1] >= pause_limits3[0][1] and mouse_position[1] <= pause_limits3[1][1]:
                    pygame.quit()
                    quit()
        display.blit(pause_menu_image,pause_menu_image_position)
        pygame.display.update()
