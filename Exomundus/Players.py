import pygame

players_image_dict = {}
players_number = 1
players = {}
players_possible_pos = {0:(360, 745),1:(433, 757),2:(542, 762),3:(641, 765),4:(747, 763),5:(853, 765),6:(953, 764),7:(1059, 766),8:(1164, 765),9:(1264, 754),10:(1356, 727),11:(1447, 670),12:(1541, 614),13:(1594, 520),14:(1646, 425),15:(1658, 324),16:(1640, 220),17:(1595, 132),18:(1494, 72),19:(1392, 46),20:(1290, 45),21:(1186, 47),22:(1081, 45),23:(979, 47),24:(876, 44),25:(773, 47),26:(668, 52),27:(558, 63),28:(453, 102),29:(352, 157),30:(261, 224),31:(204, 320),32:(183, 423),33:(184, 531),34:(215, 622),35:(268, 708),36:(360, 745)}
player_pos = [0,25,0,0,0,0]

for i in range(1,players_number+1):
    players["Jogador %i"%(i)] = {}
    players["Jogador %i"%(i)]["Posição"] = 0
    players_image_dict[i] = pygame.image.load('Players/Player%i_image.png'%i) 

def draw_players(display):
    for i in range(1,players_number+1):
        display.blit(players_image_dict[i],players_possible_pos[players["Jogador %i"%i]["Posição"]])






#for i in players.keys():
#    print(players[i])
