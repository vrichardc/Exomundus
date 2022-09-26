import pygame
from random import randint
from Players import *

pygame.mixer.init()
dice_sound_dir = 'DiceFiles/dice_sound_effect.wav'
dice_sound = pygame.mixer.Sound(dice_sound_dir)
dice_images = {}
dice_image_pos = (1820,770)
dice_limits = [(1821, 770),(1916, 867)]
dice_number = 1
dice_delay = 1900 #ms
previous_player_pos = 0
for i in range(1,7):
    dice_images[i] = pygame.image.load('DiceFiles/image_face_%i.png'%(i))

def move_char(dn):
    global player_pos,previous_player_pos
    previous_player_pos = previous_player_pos + dn
    if previous_player_pos < 36:
        players["Jogador 1"]["Posição"] = previous_player_pos
    else:
        dif = abs(36-previous_player_pos)
        players["Jogador 1"]["Posição"] = dif
        previous_player_pos = dif
def roll_dice():
    global dice_number
    dice_sound.play()
    pygame.time.delay(dice_delay)
    dice_number = randint(1,6)
    move_char(dice_number)

def draw_dice(display):
    display.blit(dice_images[dice_number],dice_image_pos)
    draw_players(display)
    pygame.display.update()
