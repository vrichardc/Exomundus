import pygame
from NewGame import *

main_menu_image_dir = 'MainMenu/background_main_menu_image.jfif'
main_menu_image = pygame.image.load(main_menu_image_dir)
main_menu_image_pos = (0,0)

start_button_limits = [(1210, 199),(1783, 449)]
tutorial_button_limits = [(1209, 483),(1782, 737)]
exit_button_limits = [(1209, 778),(1782, 1028)]

menu = True

def Main_Menu(display):
    global menu
    while menu:

        display.blit(main_menu_image,main_menu_image_pos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_position = pygame.mouse.get_pos()

                if mouse_position[0] >= start_button_limits[0][0] and mouse_position[0] <= start_button_limits[1][0] and mouse_position[1] >= start_button_limits[0][1] and mouse_position[1] <= start_button_limits[1][1]:
                    NewGame(display)

                if mouse_position[0] >= tutorial_button_limits[0][0] and mouse_position[0] <= tutorial_button_limits[1][0] and mouse_position[1] >= tutorial_button_limits[0][1] and mouse_position[1] <= tutorial_button_limits[1][1]:
                    pass

                if mouse_position[0] >= exit_button_limits[0][0] and mouse_position[0] <= exit_button_limits[1][0] and mouse_position[1] >= exit_button_limits[0][1] and mouse_position[1] <= exit_button_limits[1][1]:
                    pygame.quit()
                    quit()

        pygame.display.update()
