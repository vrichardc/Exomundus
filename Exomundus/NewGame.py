import pygame
from Server import *
from Dice import *
from PauseMenu import *
board_image_dir = 'MainMenu/Web 1920 – 1.png'
board_image = pygame.image.load(board_image_dir)
board_image_pos = (0,0)


def star_choose():
    star_number = star_sorted_numbers[0]
    return star_number

def goal_choose():
    goal_number = goal_sorted_numbers[0]
    return goal_number
def draw_star_choose(display):
    display.blit(starcard,star_card_pos)

clock = pygame.time.Clock()
newgame = True
starcard = pygame.image.load('CardsFiles/StarCards/star_card_image_1.png')
star_card_pos = (10,900)
def NewGame(display):
    global newgame

    star_number = star_choose()
    goal_number = goal_choose()
    #print(star_number,goal_number)

    while newgame:
        display.blit(board_image,board_image_pos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   pause_menu(display)
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_position = pygame.mouse.get_pos()
                #print(mouse_position)
                if mouse_position[0] >= dice_limits[0][0] and mouse_position[0] <= dice_limits[1][0] and mouse_position[1] >= dice_limits[0][1] and mouse_position[1] <= dice_limits[1][1]:
                    roll_dice()

        draw_dice(display)
        draw_players(display)
        draw_star_choose(display)
        pygame.display.update()
