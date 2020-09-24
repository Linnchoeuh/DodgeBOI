import os
try:
    import pygame
except:
    print("Erreur pygame n'est pas installé.")
    print("Installation automatique...")
    print("Mise à jour de pip...")
    os.system("python -m pip install --upgrade pip")
    print("Installation de pygame...")
    os.system("pip install pygame")
    print("Pip à été mis à jour et pygame a été installé.\nSi le programme ne se lance toujours pas, faite manuellement les installations\nPour installer voici la marche à suivre:\nPremièrement faites 'windows+r', tapez 'cmd' et appuyer sur entré.\n Nous allons d'abbord vérifier que pip est à jour, entrez la commande si dessous dans l'invite de commande que vous avez ouvert:\npython -m pip install --upgrade pip\nAttendez la fin de l'instalation et entrez ensuite cette commande pour installer pygame:\npip install pygame\n Une fois l'installation terminé vous devriez pouvoir lancer correctement ce programme\n Appuyez sur entrée pour continuer.")
    import pygame

import pygame
from pygame.locals import *
import time
import language
import random
import ctypes
import sys
import threading
from multiprocessing.pool import ThreadPool


red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
magenta = (255, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
white = (255,255,255)
light_gray = (225, 225, 225)
gray = (150,150,150)
dark_gray = (75, 75, 75)
black = (0, 0, 0)

print("->Lecture de custom_setting.txt...")
try:
    with open("custom_setting.txt", "r") as s:
        res = []
        valid_framerate_list = [30, 60, 120, 240, 360, 480]

        custom_setting_list = s.readlines()
        print(custom_setting_list)

        res_checked = 0
        res.append(int(custom_setting_list[0]))
        res.append(int(custom_setting_list[1]))
        
        print(f"Résolution horizontale chargé! [{res[0]}]")
        print(f"Résolution verticale chargé! [{res[1]}]")
        
        text_aliasing = custom_setting_list[2]
        text_aliasing = int(text_aliasing)
        text_aliasing = bool(text_aliasing)
        print(f"Aliasing du texte chargé! [{text_aliasing}]")
        
        fullscreen = custom_setting_list[3]
        fullscreen = int(fullscreen)
        print(f"Paramètre de plein écran chargé! [{fullscreen}]")

        show_fps = custom_setting_list[4]
        show_fps = int(show_fps)
        show_fps = bool(show_fps)
        
        fps_checked = 0
        fps = custom_setting_list[5]
        fps = int(fps)
        for i in range(len(valid_framerate_list)):
            if fps == valid_framerate_list[i]:
                fps_checked = 1
        if fps_checked == 0:
            print("FrameRate invalide, fps mis à 30.")
            fps = 30
            
        print(f"FrameRate limite chargé! [{fps}]")
        
        langue = language.language_detect()
        if langue == -1:
            raise ValueError("Langue invalide")
        print(f"Langue détecté! [{language.language_detect()}]")

        score_data = []
        try:
            with open("score.txt", "r") as sc:
                try:
                    for i in range(10):
                        highscore = sc.readline()
                        highscore = int(highscore)
                        score_data.append(highscore)
                except:
                    bui = 1
            score_data.sort()
            print("score.txt chargé!")
        except:
            with open("score.txt", "w") as s:
                s.close()
            print("Création de score.txt")
        print("->Lecture terminée.")
except:
    print("->custom_setting.txt est introuvable ou illisible,\n->recréation d'un fichier avec les paramètres par défaut...")
    res = [1280, 720]
    text_aliasing = False
    fullscreen = 0
    langue = 0
    show_fps = False
    fps = 30
    with open("custom_setting.txt", "w") as s:
        s.write("1280\n")
        s.write("720\n")
        s.write("0\n")
        s.write("0\n")
        s.write("0\n")
        s.write("30\n")
        s.write("english")
    print("->Recréation de custom_setting.txt terminé.")
print("->Lancement de Pygame...")

pygame.init()
# pygame.font.init()

pygame.display.set_caption("DodgeBOI") #renommer l'intitulé de la fenêtre

def update_fps(): # Génération des fonctions
    window_surface.blit(fps_text.render(str(round(clock.get_fps(), 2)), text_aliasing, red), res_pos(5,5))

def res_pos(spacex = 0, spacey = 0):
    return round((spacex/1920) * res[0]) , round((spacey/1080) * res[1])

def res_posx(space = 0):
    return round((space/1920) * res[0])

def res_posy(space = 0):
    return round((space/1080) * res[1])

def res_adaptation(height):
    return round(height * res[1]/1080)


def collision_square(res, text):
    icon_rect = icon.get_rect(topleft=(res[0],res[1]))
    window_surface.blit(icon, (res[0],res[1]))
    window_surface.blit(text, (res[0]+res_posx(20),+res[1]+res_posy(25)))
    if icon_rect.collidepoint(x,y) == 1:
        window_surface.blit(corner1, (res[0]-res_posx(18),res[1]-res_posy(18)))
        window_surface.blit(corner2, (res[0]+res_posx(268),res[1]-res_posy(18)))
        window_surface.blit(corner3, (res[0]+res_posx(268),res[1]+res_posy(68)))
        window_surface.blit(corner4, (res[0]-res_posx(18),res[1]+res_posy(68)))
        if pressed[0] and mouse_click_left == False:
            return True
    return False

def collision_back(px,py):
    back_rect = back.get_rect(topleft=res_pos(px,py))
    window_surface.blit(back, res_pos(px,py))
    if back_rect.collidepoint(x,y) == 1:
        window_surface.blit(back_light, res_pos(px,py))
        if pressed[0] and mouse_click_left == False:
            return True
    return False

def controller_square_icon(x,y,weight,height):
    window_surface.blit(corner1, res_pos(x,y))
    window_surface.blit(corner2, res_pos(weight,y))
    window_surface.blit(corner3, res_pos(weight,height))
    window_surface.blit(corner4, res_pos(x,height))
    

def stick1_negligerh():
    if input_controller[1] > 0.1:
        return 1
    elif input_controller[1] < -0.1:
        return 0
    else:
        return -1

def stick1_negligerv():
    if input_controller[2] < -0.1:
        return 0
    elif input_controller[2] > 0.1:
        return 1
    else:
        return -1

def d_pad_negligerv():
    if input_controller[0] == (0,1) or input_controller[0] == (1,1) or input_controller[0] == (-1,1):
        return 0
    elif input_controller[0] == (0,-1) or input_controller[0] == (1,-1) or input_controller[0] == (-1,-1):
        return 1
    else:
        return -1

def d_pad_negligerh():
    if input_controller[0] == (1,0) or input_controller[0] == (1,1) or input_controller[0] == (1,-1):
        return 1
    elif input_controller[0] == (-1,0) or input_controller[0] == (-1,1) or input_controller[0] == (-1,-1):
        return 0
    else:
        return -1

dict_axis = {0 : 0.0, 1 : 0.0, 2 : 0.0, 3 : 0.0, 4 : 0.0}
dict_button = {0 : False, 1 : False, 2 : False, 3 : False, 4 : False, 5 : False, 6 : False, 7 : False, 8 : False, 9 : False}
dict_hat = {0: (0, 0)}
dict_key = {}
def controller_outpout():
    dict_button[0] = bool(pygame.joystick.Joystick(0).get_button(0)) #A
    dict_button[1] = bool(pygame.joystick.Joystick(0).get_button(1)) #B
    dict_button[2] = bool(pygame.joystick.Joystick(0).get_button(2)) #Y
    dict_button[3] = bool(pygame.joystick.Joystick(0).get_button(3)) #X
    dict_button[4] = bool(pygame.joystick.Joystick(0).get_button(4)) #L
    dict_button[5] = bool(pygame.joystick.Joystick(0).get_button(5)) #R
    dict_button[6] = bool(pygame.joystick.Joystick(0).get_button(6)) #-
    dict_button[7] = bool(pygame.joystick.Joystick(0).get_button(7)) #+
    dict_button[8] = bool(pygame.joystick.Joystick(0).get_button(8)) #StickL
    dict_button[9] = bool(pygame.joystick.Joystick(0).get_button(9)) #StickR

    dict_axis[0] = round(pygame.joystick.Joystick(0).get_axis(0), 1) #StickLVertical
    dict_axis[1] = round(pygame.joystick.Joystick(0).get_axis(1), 1) #StickLHorizontal
    dict_axis[2] = round(pygame.joystick.Joystick(0).get_axis(2), 1) #ZL/ZR
    dict_axis[3] = round(pygame.joystick.Joystick(0).get_axis(3), 1) #StickRVertical
    dict_axis[4] = round(pygame.joystick.Joystick(0).get_axis(4), 1) #StickRHorizontal
    
    if event.type == JOYHATMOTION:
        dict_hat[0] = mon_joystick1.get_hat(0)

    stick1_mov = False
    if event.type == JOYAXISMOTION:
        if event.axis == 1 and event.value > 0.1 or event.axis == 1 and event.value < -0.1 or event.axis == 0 and event.value > 0.1 or event.axis == 0 and event.value < -0.1:
            stick1_mov = True

    stick2_mov = False
    if event.type == JOYAXISMOTION:
        if event.axis == 3 and event.value > 0.1 or event.axis == 3 and event.value < -0.1 or event.axis == 4 and event.value > 0.1 or event.axis == 4 and event.value < -0.1:
            stick2_mov = True
    
    # print(dict_axis)
    # print(dict_button)
    # print(dict_hat)
    input_list = [dict_hat[0], dict_axis[0], dict_axis[1], dict_axis[3], dict_axis[4], dict_button[1], dict_button[0], dict_button[2], dict_button[3], dict_button[4], dict_button[5], dict_button[6], dict_button[7], dict_button[8], dict_button[9], dict_axis[2]]
    # print(input_list)
    return input_list


def loading_rect(percent = 0):
    window_surface.fill(black)
    text_percent = text_50a.render(f"{percent}%", text_aliasing, white)
    window_surface.blit(loading_text, res_pos(810,400))
    window_surface.blit(text_percent, res_pos(900,470))
    pygame.draw.rect(window_surface, white, pygame.Rect(res_posx(725),res_posy(550),percent*res_posx(4),30))
    pygame.display.flip()
    return 1

def tutorial_text(text = "", input_info = 0):
    text = text_40a.render(text, text_aliasing, white)
    window_surface.blit(text, res_pos(50,900))

def tutorial_text2(text = "", input_info = 0):
    text = text_40a.render(text, text_aliasing, white)
    window_surface.blit(text, res_pos(50,950))


print("Chargement des textures")

# Autres ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def generateur(waiting1, last1, color_last1, block_collide1a, block_collide2a, block_collide3a, block_collidealla):
    if PAUSE < 1:
        if waiting1 <= 0 or div_wait == True: #générateur 
            random_number = random.randint(0,13)
            if random_number == 0 and last1 != 1 and div_wait == False:
                for i in range(len(block_id)):
                    if block_id[i] == 0:
                        block_id.insert(i , 1)
                        del block_id[i+1]
                        last1 = 1
                        break
            elif random_number == 1 and last1 != 2 and div_wait == False:
                for i in range(len(block_id)):
                    if block_id[i] == 0:
                        block_id.insert(i , 2)
                        del block_id[i+1]
                        last1 = 2
                        break
            elif random_number == 2 and last1 != 3 and div_wait == False:
                for i in range(len(block_id)):
                    if block_id[i] == 0:
                        block_id.insert(i , 3)
                        del block_id[i+1]
                        last1 = 3
                        break
            elif random_number == 4 and last1 != 4 and div_wait == False:
                for i in range(len(block_id)):
                    if block_id[i] == 0:
                        block_id.insert(i , 4)
                        del block_id[i+1]
                        last1 = 4
                        break
            elif random_number == 5 and last1 != 5 and div_wait == False:
                for i in range(len(block_id)):
                    if block_id[i] == 0:
                        block_id.insert(i , 5)
                        del block_id[i+1]
                        last1 = 5
                        break
            elif random_number == 6 and last1 != 6 and div_wait == False or last1 == 7 and div_wait == False:
                for i in range(len(block_id)):
                    if block_id[i] == 0:
                        block_id.insert(i , 6)
                        del block_id[i+1]
                        last1 = 6
                        break
            elif random_number == 7 and last1 != 7 and color_last1 != 1 and div_wait == False:
                for i in range(len(block_id)):
                    if block_id[i] == 0:
                        block_id.insert(i , 7)
                        del block_id[i+1]
                        last1 = 7
                        color_last1 = 1
                        break
            elif random_number == 8 and last1 != 7 and color_last1 != 2 and div_wait == False:
                for i in range(len(block_id)):
                    if block_id[i] == 0:
                        block_id.insert(i , 8)
                        del block_id[i+1]
                        last1 = 7
                        color_last1 = 2
                        break
            elif random_number == 9 and last1 != 7 and color_last1 != 3 and div_wait == False:
                for i in range(len(block_id)):
                    if block_id[i] == 0:
                        block_id.insert(i , 9)
                        del block_id[i+1]
                        last1 = 7
                        color_last1 = 3
                        break
            elif  last1 != 8 or div_wait == True:
                random_number = random.randint(0,2)
                random_number2 = random.randint(0,2)
                if random_number == 0:
                    if random_number2 == 0:
                        for i in range(len(block_id)):
                            if block_id[i] == 0:
                                block_id.insert(i , 10)
                                del block_id[i+1]
                                break
                    elif random_number2 == 1:
                        for i in range(len(block_id)):
                            if block_id[i] == 0:
                                block_id.insert(i , 11)
                                del block_id[i+1]
                                break
                    else:
                        for i in range(len(block_id)):
                            if block_id[i] == 0:
                                block_id.insert(i , 12)
                                del block_id[i+1]
                                break
                elif random_number == 1:
                    if random_number2 == 0:
                        for i in range(len(block_id)):
                            if block_id[i] == 0:
                                block_id.insert(i , 13)
                                del block_id[i+1]
                                break
                    elif random_number2 == 1:
                        for i in range(len(block_id)):
                            if block_id[i] == 0:
                                block_id.insert(i , 14)
                                del block_id[i+1]
                                break
                    else:
                        for i in range(len(block_id)):
                            if block_id[i] == 0:
                                block_id.insert(i , 15)
                                del block_id[i+1]
                                break
                else:
                    if random_number2 == 0:
                        for i in range(len(block_id)):
                            if block_id[i] == 0:
                                block_id.insert(i , 16)
                                del block_id[i+1]
                                break
                    elif random_number2 == 1:
                        for i in range(len(block_id)):
                            if block_id[i] == 0:
                                block_id.insert(i , 17)
                                del block_id[i+1]
                                break
                    else:
                        for i in range(len(block_id)):
                            if block_id[i] == 0:
                                block_id.insert(i , 18)
                                del block_id[i+1]
                                break
                last = 8
            elif color_last == 1:
                if random.randint(0,1) == 0:
                    for i in range(len(block_id)):
                        if block_id[i] == 0:
                            block_id.insert(i , 8)
                            del block_id[i+1]
                            last1 = 7
                            color_last1 = 2
                            break
                else:
                    for i in range(len(block_id)):
                        if block_id[i] == 0:
                            block_id.insert(i , 9)
                            del block_id[i+1]
                            last1 = 7
                            color_last1 = 3
                            break
            elif color_last == 2:
                if random.randint(0,1) == 0:
                    for i in range(len(block_id)):
                        if block_id[i] == 0:
                            block_id.insert(i , 7)
                            del block_id[i+1]
                            last1 = 7
                            color_last1 = 1
                            break
                else:
                    for i in range(len(block_id)):
                        if block_id[i] == 0:
                            block_id.insert(i , 9)
                            del block_id[i+1]
                            last1 = 7
                            color_last1 = 3
                            break
            elif color_last == 3:
                if random.randint(0,1) == 0:
                    for i in range(len(block_id)):
                        if block_id[i] == 0:
                            block_id.insert(i , 8)
                            del block_id[i+1]
                            last1 = 7
                            color_last1 = 2
                            break
                else:
                    for i in range(len(block_id)):
                        if block_id[i] == 0:
                            block_id.insert(i , 7)
                            del block_id[i+1]
                            last1 = 7
                            color_last1 = 1
                            break
            waiting1 = (26*sfr)/speed
        waiting1 -= fps*dt

        for i in range(len(block_id)): # Déplaceur de bloc
            if block_id[i] > 0:
                a = block_mov.get(f"block{i}")
                a += -1000 * dt * speed
                block_mov[f"block{i}"] = a
                if a < -301:
                    block_id.insert(i , 0)
                    del block_id[i+1]
                    block_mov[f"block{i}"] = 1920
    block_collide1a = 0
    block_collide2a = 0
    block_collide3a = 0
    block_collidealla = "none"
    for i in range(len(block_id)): #l'afficheur de block
        if block_id[i] > 0:
            if block_id[i] < 4:
                if block_id[i] == 1:
                    window_surface.blit(block, res_pos(block_mov.get(f"block{i}"),30)) #One block up id:1
                    if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                        block_collide1a = 1
                elif block_id[i] == 2:
                    window_surface.blit(block, res_pos(block_mov.get(f"block{i}"),390)) #One block middle id:2
                    if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                        block_collide2a = 1
                elif block_id[i] == 3:
                    window_surface.blit(block, res_pos(block_mov.get(f"block{i}"),750)) #One block bottom id:3
                    if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                        block_collide3a = 1
            elif block_id[i] > 3 and block_id[i] < 7:    
                if block_id[i] == 4:
                    window_surface.blit(block, res_pos(block_mov.get(f"block{i}"),30)) #Two blocks up bottom id:4
                    window_surface.blit(block, res_pos(block_mov.get(f"block{i}"),750))
                    if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                        block_collide1a = 1
                        block_collide3a = 1
                elif block_id[i] == 5:
                    window_surface.blit(block, res_pos(block_mov.get(f"block{i}"),30)) #Two blocks up middle id:5
                    window_surface.blit(block, res_pos(block_mov.get(f"block{i}"),390))
                    if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                        block_collide1a = 1
                        block_collide2a = 1
                elif block_id[i] == 6:
                    window_surface.blit(block, res_pos(block_mov.get(f"block{i}"),390)) #Two blocks middle bottom id:6
                    window_surface.blit(block, res_pos(block_mov.get(f"block{i}"),750))
                    if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                        block_collide2a = 1
                        block_collide3a = 1
            elif block_id[i] > 6 and block_id[i] < 10:
                if block_id[i] == 7:
                    window_surface.blit(big_block_red, res_pos(block_mov.get(f"block{i}"),30)) #big_block_red
                    if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                        block_collidealla = "red"
                elif block_id[i] == 8:
                    window_surface.blit(big_block_blue, res_pos(block_mov.get(f"block{i}"),30))
                    if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                        block_collidealla = "blue"
                elif block_id[i] == 9:
                    window_surface.blit(big_block_yellow, res_pos(block_mov.get(f"block{i}"),30))
                    if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                        block_collidealla = "yellow"
            elif block_id[i] > 9 and block_id[i] < 13:
                window_surface.blit(block, res_pos(block_mov.get(f"block{i}"),390))
                window_surface.blit(block, res_pos(block_mov.get(f"block{i}"),750))
                if block_id[i] == 10:
                    window_surface.blit(demi_block, res_pos(block_mov.get(f"block{i}"),30))
                    if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                        block_collide1a = 2
                        block_collide2a = 1
                        block_collide3a = 1
                elif block_id[i] == 11:
                    window_surface.blit(demi_block, res_pos(block_mov.get(f"block{i}"),180))
                    if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                        block_collide1a = 3
                        block_collide2a = 1
                        block_collide3a = 1
                elif block_id[i] == 12:
                    window_surface.blit(break_block, res_pos(block_mov.get(f"block{i}"),30))
                    if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                        block_collide1a = 4
                        block_collide2a = 1
                        block_collide3a = 1
                        if position_of_player == 3:
                            block_id.insert(i, 6)
                            del block_id[i+1]
            elif block_id[i] > 12 and block_id[i] < 16:
                window_surface.blit(block, res_pos(block_mov.get(f"block{i}"),30))
                window_surface.blit(block, res_pos(block_mov.get(f"block{i}"),750))
                if block_id[i] == 13:
                    window_surface.blit(demi_block, res_pos(block_mov.get(f"block{i}"),390))
                    if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                        block_collide1a = 1
                        block_collide2a = 2
                        block_collide3a = 1
                elif block_id[i] == 14:
                    window_surface.blit(demi_block, res_pos(block_mov.get(f"block{i}"),540))
                    if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                        block_collide1a = 1
                        block_collide2a = 3
                        block_collide3a = 1
                elif block_id[i] == 15:
                    window_surface.blit(break_block, res_pos(block_mov.get(f"block{i}"),390))
                    if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                        block_collide1a = 1
                        block_collide2a = 4
                        block_collide3a = 1
                        if position_of_player == 3:
                            block_id.insert(i, 4)
                            del block_id[i+1]
            elif block_id[i] > 15:
                window_surface.blit(block, res_pos(block_mov.get(f"block{i}"),30))
                window_surface.blit(block, res_pos(block_mov.get(f"block{i}"),390))
                if block_id[i] == 16:
                    window_surface.blit(demi_block, res_pos(block_mov.get(f"block{i}"),750))
                    if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                        block_collide1a = 1
                        block_collide2a = 1
                        block_collide3a = 2
                elif block_id[i] == 17:
                    window_surface.blit(demi_block, res_pos(block_mov.get(f"block{i}"),900))
                    if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                        block_collide1a = 1
                        block_collide2a = 1
                        block_collide3a = 3
                elif block_id[i] == 18:
                    window_surface.blit(break_block, res_pos(block_mov.get(f"block{i}"),750))
                    if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                        block_collide1a = 1
                        block_collide2a = 1
                        block_collide3a = 4
                        if position_of_player == 3:
                            block_id.insert(i, 5)
                            del block_id[i+1]
    return [waiting1, last1, color_last1, block_collide1a, block_collide2a, block_collide3a, block_collidealla]

# Variables ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

clock = pygame.time.Clock()
sfr = fps / 30

launched = True #pour maintenir la fenêtre ouverte
loaded = True
click = False
menu = 0
frame = 1
player_pos = 1
player_pos_y = round((515/1080) * res[1])
press = 0
PAUSE = 0
score_counter = 0
score = 0

rng = random.Random()
waiting = 90 * sfr
last = 0
game_design = 1
color = "red"
color_last = 1
menu_loaded = -1
controller_on = 1
mon_joystick1 = 0
mon_joystick2 = 0
menu0_joystick_select = 0
menu1_joystick_select = 0
menu2_joystick_select = 0
menu3_joystick_select = 0
no_input = True
nokey_input = True
position_of_player = 0
div_wait = False
event_waiting = False
keyboard_input = {27: False, 13: False, 119: False, 115: False, 113: False, 101: False, 257: False, 258: False, 259: False, 107: False, 108: False, 59: False, 32: False}
                # 27: esc   ,13:return, 119 : z ,   115: s    , 113: a    , 101: e    , 257: 1    , 258: 2    , 259: 3    , 107: k    , 108: l    , 59: m    , 32: space
firstload = False
pool = ThreadPool(processes = 1)
input_controller = [(0, 0), 0, 0, 0, 0, False, False, False, False, False, False, False, False, False, False, 0]

while launched: #Pour fermer la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        event_waiting = True

    if loaded == True:
        if fullscreen == 1:
            if res[1] == 1080:
                ctypes.windll.user32.SetProcessDPIAware()
            try:
                window_surface = pygame.display.set_mode(res, pygame.FULLSCREEN)
            except:
                try:
                    print(f"Erreur, la résolution fourni n'est pas supporté par votre appareil. Résolution mise en {tres[0]}x{tres[1]}.")
                    custom_setting_list = [str(tres[0]), str(tres[1]), str(int(text_aliasing)), str(fullscreen), str(int(show_fps)), str(fps), custom_setting_list[6]]
                    with open("custom_setting.txt", "w") as s:
                        for i in range(len(custom_setting_list)-1):
                            s.write(f"{custom_setting_list[i]}\n")
                        s.write(custom_setting_list[6])
                    res = tres
                except:
                    print("Erreur, la résolution fourni n'est pas supporté par votre appareil. Résolution mise en 1280x720.")
                    custom_setting_list = [str(1280), str(720), str(int(text_aliasing)), str(fullscreen), str(int(show_fps)), str(fps), custom_setting_list[6]]
                    with open("custom_setting.txt", "w") as s:
                        for i in range(len(custom_setting_list)-1):
                            s.write(f"{custom_setting_list[i]}\n")
                        s.write(custom_setting_list[6])
                    res = [1280,720]
                window_surface = pygame.display.set_mode(res, pygame.FULLSCREEN)
                
        else:
            window_surface = pygame.display.set_mode(res) #définir les propriétés de la fenêtre
        
        window_surface.fill(black) #Rend la fenêtre noir a tout les démarrage
        
        try:
            fps_text = pygame.font.Font(os.path.join("fonts", "VCR_OSD_MONO_1.ttf"), round(res_adaptation(22))) # Autres

            text_40a = pygame.font.Font(os.path.join("fonts", "arialbd.ttf"), round(res_adaptation(40))) # Menu principal
            quit_text_load = pygame.font.Font(os.path.join("fonts", "arialbd.ttf"), round(res_adaptation(180)))
            text_50a = pygame.font.Font(os.path.join("fonts", "arialbd.ttf"), round(res_adaptation(50)))

            text_25a = pygame.font.Font(os.path.join("fonts", "arialbd.ttf"), round(res_adaptation(25))) # Jeu
            text_200a = pygame.font.Font(os.path.join("fonts", "arialbd.ttf"), round(res_adaptation(200)))

            text_20a = pygame.font.Font(os.path.join("fonts", "arialbd.ttf"), round(res_adaptation(20))) # Détails sur certaine variable + score

            text_140a = pygame.font.Font(os.path.join("fonts", "arialbd.ttf"), round(res_adaptation(140)))

            text_90a = pygame.font.Font(os.path.join("fonts", "arialbd.ttf"), round(res_adaptation(90)))
        except:
            print("Erreur, fichier(s) de police manquant, réinstallez le programme, si le problème persiste réinstallez pygame voir python.")
            input()

        # Render textes ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        loading_text = text_50a.render(language.loading_text(langue), text_aliasing, white)
        load = loading_rect()
        
        setting_text = text_40a.render(language.setting_icon(langue), text_aliasing, white) #Menu Principal
        play_text = text_40a.render(language.play_icon(langue), text_aliasing, white)
        load += loading_rect(load)
        score_text = text_40a.render(language.score_icon(langue), text_aliasing, white)
        quit_text = quit_text_load.render(language.quit(langue), text_aliasing, white)
        quit_text_min = text_40a.render(language.the_quit(langue), text_aliasing, white)
        load += loading_rect(load)
        yes_text = text_50a.render(language.yes(langue), text_aliasing, white)
        no_text = text_50a.render(language.no(langue), text_aliasing, white)
        load += loading_rect(load)
        text_tuto = text_40a.render(language.tutorial(langue), text_aliasing, white)

        text_main_menu = text_25a.render(language.back_to_menu(langue), text_aliasing, white) # En jeu
        text_resume = text_40a.render(language.unpause(langue), text_aliasing, white)
        load += loading_rect(load)
        text_pause = text_200a.render(language.pause(langue), text_aliasing, white)

        text_retry = text_50a.render(language.retry(langue), text_aliasing, white)
        load += loading_rect(load)
        text_lose = text_140a.render(language.lose(langue), text_aliasing, white)

        setting_text_in_setting = text_200a.render(language.setting_icon(langue), text_aliasing, white) # Paramètres
        load += loading_rect(load)
        text_language = text_50a.render(language.Language(langue), text_aliasing, white)
        text_show_fps = text_50a.render(language.show_fps(langue), text_aliasing, white)
        load += loading_rect(load)
        text_setting_aliasing = text_50a.render(language.text_aliasing(langue), text_aliasing, white)
        text_res = text_50a.render(language.resolution_modify(langue), text_aliasing, white)
        load += loading_rect(load)
        text_fullscreen = text_50a.render(language.fullscreen(langue), text_aliasing, white)
        text_framerate = text_50a.render(language.framerate(langue), text_aliasing, white)
        load += loading_rect(load)
        text_apply = text_40a.render(language.apply(langue), text_aliasing, white)
        text_cdisconnect = text_25a.render(language.disconnect_controller(langue), text_aliasing, red)
        text_cconnect = text_25a.render(language.connect_controller(langue), text_aliasing, white)
        text_searching_controller = text_140a.render(language.searching_controller(langue), text_aliasing, white)

        text_highscore = text_200a.render(language.highscore(langue), text_aliasing, white) # Stats
        load += loading_rect(load)

        controller_detected = text_140a.render(language.controller_detected(langue), text_aliasing, white)
        use_controller = text_90a.render(language.use_controller(langue), text_aliasing, white)
        move_text = text_90a.render(language.moving_mouse(langue), text_aliasing, white)
        tuto_help_text = text_25a.render(language.tuto_help(langue), text_aliasing, white)
        text_finish = text_90a.render(language.text_finish(langue), text_aliasing, white)

        try:
            # Menu principal ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            
            load += loading_rect(load)
            bg = pygame.image.load(f"textures/ui/menu_background.png").convert()
            bg = pygame.transform.smoothscale(bg, res_pos(1920,1080))
            load += loading_rect(load)
            croix = pygame.image.load(f"textures/ui/croix.png").convert_alpha()
            croix = pygame.transform.smoothscale(croix, res_pos(30,30))
            back = pygame.image.load(f"textures/ui/back.png").convert_alpha()
            back = pygame.transform.smoothscale(back, res_pos(60,60))
            load += loading_rect(load)
            croix_light = pygame.image.load(f"textures/ui/croix_light.png").convert_alpha()
            croix_light = pygame.transform.smoothscale(croix_light, res_pos(30,30))
            back_light = pygame.image.load(f"textures/ui/back_light.png").convert_alpha()
            back_light = pygame.transform.smoothscale(back_light, res_pos(60,60))
            load += loading_rect(load)
            icon = pygame.image.load(f"textures/ui/icon_select.png").convert_alpha()
            icon = pygame.transform.scale(icon, res_pos(300,100))
            load += loading_rect(load)
            no_button = pygame.image.load(f"textures/ui/no_button.png").convert_alpha()
            no_button = pygame.transform.scale(no_button, res_pos(179,100))
            load += loading_rect(load)
            yes_button = pygame.image.load(f"textures/ui/yes_button.png").convert_alpha()
            yes_button = pygame.transform.scale(yes_button, res_pos(179,100))
            load += loading_rect(load)
            rect_quit = pygame.image.load(f"textures/ui/rect_quit.png").convert_alpha()
            rect_quit = pygame.transform.scale(rect_quit, res_pos(1000,400))

            # Jeu ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            load += loading_rect(load)
            runner1r = pygame.image.load(f"textures/game/runner1red.png").convert_alpha() # Runner
            runner1r = pygame.transform.scale(runner1r, res_pos(90,90))
            load += loading_rect(load)
            runner2r = pygame.image.load(f"textures/game/runner2red.png").convert_alpha()
            runner2r = pygame.transform.scale(runner2r, res_pos(90,90))
            load += loading_rect(load)
            runner3r = pygame.image.load(f"textures/game/runner3red.png").convert_alpha()
            runner3r = pygame.transform.scale(runner3r, res_pos(90,90))
            load += loading_rect(load)
            runner4r = pygame.image.load(f"textures/game/runner4red.png").convert_alpha()
            runner4r = pygame.transform.scale(runner4r, res_pos(90,90))
            
            load += loading_rect(load)
            runner1b = pygame.image.load(f"textures/game/runner1blue.png").convert_alpha()
            runner1b = pygame.transform.scale(runner1b, res_pos(90,90))
            load += loading_rect(load)
            runner2b = pygame.image.load(f"textures/game/runner2blue.png").convert_alpha()
            runner2b = pygame.transform.scale(runner2b, res_pos(90,90))
            load += loading_rect(load)
            runner3b = pygame.image.load(f"textures/game/runner3blue.png").convert_alpha()
            runner3b = pygame.transform.scale(runner3b, res_pos(90,90))
            load += loading_rect(load)
            runner4b = pygame.image.load(f"textures/game/runner4blue.png").convert_alpha()
            runner4b = pygame.transform.scale(runner4b, res_pos(90,90))
            
            load += loading_rect(load)
            runner1y = pygame.image.load(f"textures/game/runner1yellow.png").convert_alpha()
            runner1y = pygame.transform.scale(runner1y, res_pos(90,90))
            load += loading_rect(load)
            runner2y = pygame.image.load(f"textures/game/runner2yellow.png").convert_alpha()
            runner2y = pygame.transform.scale(runner2y, res_pos(90,90))
            load += loading_rect(load)
            runner3y = pygame.image.load(f"textures/game/runner3yellow.png").convert_alpha()
            runner3y = pygame.transform.scale(runner3y, res_pos(90,90))
            load += loading_rect(load)
            runner4y = pygame.image.load(f"textures/game/runner4yellow.png").convert_alpha()
            runner4y = pygame.transform.scale(runner4y, res_pos(90,90))
            
            load += loading_rect(load)
            runnerfallred = pygame.image.load(f"textures/game/runnerfallred.png").convert_alpha()
            runnerfallred = pygame.transform.scale(runnerfallred, res_pos(90,90))
            load += loading_rect(load)
            runnerfallblue = pygame.image.load(f"textures/game/runnerfallblue.png").convert_alpha()
            runnerfallblue = pygame.transform.scale(runnerfallblue, res_pos(90,90))
            load += loading_rect(load)
            runnerfallyellow = pygame.image.load(f"textures/game/runnerfallyellow.png").convert_alpha()
            runnerfallyellow = pygame.transform.scale(runnerfallyellow, res_pos(90,90))
            
            load += loading_rect(load)
            runnergroundred = pygame.image.load(f"textures/game/runnergroundred.png").convert_alpha()
            runnergroundred = pygame.transform.scale(runnergroundred, res_pos(90,90))
            load += loading_rect(load)
            runnergroundblue = pygame.image.load(f"textures/game/runnergroundblue.png").convert_alpha()
            runnergroundblue = pygame.transform.scale(runnergroundblue, res_pos(90,90))
            load += loading_rect(load)
            runnergroundyellow = pygame.image.load(f"textures/game/runnergroundyellow.png").convert_alpha()
            runnergroundyellow = pygame.transform.scale(runnergroundyellow, res_pos(90,90))

            load += loading_rect(load)
            slide1r = pygame.image.load(f"textures/game/slide1red.png").convert_alpha()
            slide1r = pygame.transform.scale(slide1r, res_pos(102,90))
            load += loading_rect(load)
            slide2r = pygame.image.load(f"textures/game/slide2red.png").convert_alpha()
            slide2r = pygame.transform.scale(slide2r, res_pos(102,90))
            load += loading_rect(load)
            slide3r = pygame.image.load(f"textures/game/slide3red.png").convert_alpha()
            slide3r = pygame.transform.scale(slide3r, res_pos(102,90))
            load += loading_rect(load)
            slide4r = pygame.image.load(f"textures/game/slide4red.png").convert_alpha()
            slide4r = pygame.transform.scale(slide4r, res_pos(102,90))

            load += loading_rect(load)
            slide1b = pygame.image.load(f"textures/game/slide1blue.png").convert_alpha()
            slide1b = pygame.transform.scale(slide1b, res_pos(102,90))
            load += loading_rect(load)
            slide2b = pygame.image.load(f"textures/game/slide2blue.png").convert_alpha()
            slide2b = pygame.transform.scale(slide2b, res_pos(102,90))
            load += loading_rect(load)
            slide3b = pygame.image.load(f"textures/game/slide3blue.png").convert_alpha()
            slide3b = pygame.transform.scale(slide3b, res_pos(102,90))
            load += loading_rect(load)
            slide4b = pygame.image.load(f"textures/game/slide4blue.png").convert_alpha()
            slide4b = pygame.transform.scale(slide4b, res_pos(102,90))

            load += loading_rect(load)
            slide1y = pygame.image.load(f"textures/game/slide1yellow.png").convert_alpha()
            slide1y = pygame.transform.scale(slide1y, res_pos(102,90))
            load += loading_rect(load)
            slide2y = pygame.image.load(f"textures/game/slide2yellow.png").convert_alpha()
            slide2y = pygame.transform.scale(slide2y, res_pos(102,90))
            load += loading_rect(load)
            slide3y = pygame.image.load(f"textures/game/slide3yellow.png").convert_alpha()
            slide3y = pygame.transform.scale(slide3y, res_pos(102,90))
            load += loading_rect(load)
            slide4y = pygame.image.load(f"textures/game/slide4yellow.png").convert_alpha()
            slide4y = pygame.transform.scale(slide4y, res_pos(102,90))
            load += loading_rect(load)
            jump1r = pygame.image.load(f"textures/game/jump1red.png").convert_alpha()
            jump1r = pygame.transform.scale(jump1r, res_pos(90,90))
            load += loading_rect(load)
            jump2r = pygame.image.load(f"textures/game/jump2red.png").convert_alpha()
            jump2r = pygame.transform.scale(jump2r, res_pos(90,90))
            load += loading_rect(load)
            jump3r = pygame.image.load(f"textures/game/jump3red.png").convert_alpha()
            jump3r = pygame.transform.scale(jump3r, res_pos(90,90))
            load += loading_rect(load)
            jump4r = pygame.image.load(f"textures/game/jump4red.png").convert_alpha()
            jump4r = pygame.transform.scale(jump4r, res_pos(90,90))

            load += loading_rect(load)
            jump1b = pygame.image.load(f"textures/game/jump1blue.png").convert_alpha()
            jump1b = pygame.transform.scale(jump1b, res_pos(90,90))
            load += loading_rect(load)
            jump2b = pygame.image.load(f"textures/game/jump2blue.png").convert_alpha()
            jump2b = pygame.transform.scale(jump2b, res_pos(90,90))
            load += loading_rect(load)
            jump3b = pygame.image.load(f"textures/game/jump3blue.png").convert_alpha()
            jump3b = pygame.transform.scale(jump3b, res_pos(90,90))
            load += loading_rect(load)
            jump4b = pygame.image.load(f"textures/game/jump4blue.png").convert_alpha()
            jump4b = pygame.transform.scale(jump4b, res_pos(90,90))

            load += loading_rect(load)
            jump1y = pygame.image.load(f"textures/game/jump1yellow.png").convert_alpha()
            jump1y = pygame.transform.scale(jump1y, res_pos(90,90))
            load += loading_rect(load)
            jump2y = pygame.image.load(f"textures/game/jump2yellow.png").convert_alpha()
            jump2y = pygame.transform.scale(jump2y, res_pos(90,90))
            load += loading_rect(load)
            jump3y = pygame.image.load(f"textures/game/jump3yellow.png").convert_alpha()
            jump3y = pygame.transform.scale(jump3y, res_pos(90,90))
            load += loading_rect(load)
            jump4y = pygame.image.load(f"textures/game/jump4yellow.png").convert_alpha()
            jump4y = pygame.transform.scale(jump4y, res_pos(90,90))
            
            load += loading_rect(load)
            kick1r = pygame.image.load(f"textures/game/kick1red.png").convert_alpha()
            kick1r = pygame.transform.scale(kick1r, res_pos(90,90))
            load += loading_rect(load)
            kick2r = pygame.image.load(f"textures/game/kick2red.png").convert_alpha()
            kick2r = pygame.transform.scale(kick2r, res_pos(90,90))
            load += loading_rect(load)
            kick3r = pygame.image.load(f"textures/game/kick3red.png").convert_alpha()
            kick3r = pygame.transform.scale(kick3r, res_pos(90,90))
            load += loading_rect(load)
            kick4r = pygame.image.load(f"textures/game/kick4red.png").convert_alpha()
            kick4r = pygame.transform.scale(kick4r, res_pos(90,90))
            
            load += loading_rect(load)
            kick1b = pygame.image.load(f"textures/game/kick1blue.png").convert_alpha()
            kick1b = pygame.transform.scale(kick1b, res_pos(90,90))
            load += loading_rect(load)
            kick2b = pygame.image.load(f"textures/game/kick2blue.png").convert_alpha()
            kick2b = pygame.transform.scale(kick2b, res_pos(90,90))
            load += loading_rect(load)
            kick3b = pygame.image.load(f"textures/game/kick3blue.png").convert_alpha()
            kick3b = pygame.transform.scale(kick3b, res_pos(90,90))
            load += loading_rect(load)
            kick4b = pygame.image.load(f"textures/game/kick4blue.png").convert_alpha()
            kick4b = pygame.transform.scale(kick4b, res_pos(90,90))
            
            load += loading_rect(load)
            kick1y = pygame.image.load(f"textures/game/kick1yellow.png").convert_alpha()
            kick1y = pygame.transform.scale(kick1y, res_pos(90,90))
            load += loading_rect(load)
            kick2y = pygame.image.load(f"textures/game/kick2yellow.png").convert_alpha()
            kick2y = pygame.transform.scale(kick2y, res_pos(90,90))
            load += loading_rect(load)
            kick3y = pygame.image.load(f"textures/game/kick3yellow.png").convert_alpha()
            kick3y = pygame.transform.scale(kick3y, res_pos(90,90))
            load += loading_rect(load)
            kick4y = pygame.image.load(f"textures/game/kick4yellow.png").convert_alpha()
            kick4y = pygame.transform.scale(kick4y, res_pos(90,90))
            
            load += loading_rect(load)
            big_block_red = pygame.image.load(f"textures/game/big_blockred.png").convert_alpha() # Obstacles
            big_block_red = pygame.transform.scale(big_block_red, res_pos(300,1020))
            load += loading_rect(load)
            big_block_blue = pygame.image.load(f"textures/game/big_blockblue.png").convert_alpha()
            big_block_blue = pygame.transform.scale(big_block_blue, res_pos(300,1020))
            load += loading_rect(load)
            big_block_yellow = pygame.image.load(f"textures/game/big_blockyellow.png").convert_alpha()
            big_block_yellow = pygame.transform.scale(big_block_yellow, res_pos(300,1020))
            
            load += loading_rect(load)
            block = pygame.image.load(f"textures/game/basic_block.png").convert_alpha()
            block = pygame.transform.scale(block, res_pos(300,300))
            load += loading_rect(load)
            demi_block = pygame.image.load(f"textures/game/demi_block.png").convert_alpha()
            demi_block = pygame.transform.scale(demi_block, res_pos(300,150))
            load += loading_rect(load)
            break_block = pygame.image.load(f"textures/game/breakable_block.png").convert_alpha()
            break_block = pygame.transform.scale(break_block, res_pos(300,300))
            load += loading_rect(load)
            pause_square = pygame.image.load(f"textures/game/pause_square.png").convert_alpha() # Pause/Echec
            pause_square = pygame.transform.scale(pause_square, res_pos(1280,720))
            load += loading_rect(load)
            stat = pygame.image.load(f"textures/ui/stat.png").convert_alpha()
            stat = pygame.transform.scale(stat, res_pos(100,100))
            load += loading_rect(load)
            rect_form = pygame.Rect(res_posx(5), res_posy(5), res_adaptation(100), res_adaptation(22))

            # Paramètres ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            load += loading_rect(load)
            language_icon_eng = pygame.image.load(f"textures/ui/eng.png").convert_alpha()
            language_icon_eng = pygame.transform.scale(language_icon_eng, res_pos(50,50))
            load += loading_rect(load)
            language_icon_fr = pygame.image.load(f"textures/ui/fr.png").convert_alpha()
            language_icon_fr = pygame.transform.scale(language_icon_fr, res_pos(50,50))
            load += loading_rect(load)
            valid = pygame.image.load(f"textures/ui/valid_button.png").convert_alpha()
            valid = pygame.transform.scale(valid, res_pos(72,40))
            load += loading_rect(load)
            invalid = pygame.image.load(f"textures/ui/invalid_button.png").convert_alpha()
            invalid = pygame.transform.scale(invalid, res_pos(72,40))
            load += loading_rect(load)
            left_arrow = pygame.image.load(f"textures/ui/left_arrow.png").convert_alpha()
            left_arrow = pygame.transform.smoothscale(left_arrow, res_pos(35,40))
            load += loading_rect(load)
            right_arrow = pygame.image.load(f"textures/ui/right_arrow.png").convert_alpha()
            right_arrow = pygame.transform.smoothscale(right_arrow, res_pos(35,40))
            load += loading_rect(load)
            res_block = pygame.image.load(f"textures/ui/res_block.png").convert_alpha()
            res_block = pygame.transform.scale(res_block, res_pos(279,70))
            load += loading_rect(load)
            res_block_next = pygame.image.load(f"textures/ui/res_block_next.png").convert_alpha()
            res_block_next = pygame.transform.scale(res_block_next, res_pos(279,70))

            # Stats ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


            # Controller

            load += loading_rect(load)
            controller_square = pygame.image.load(f"textures/ui/controller_square.png").convert_alpha()
            controller_square = pygame.transform.smoothscale(controller_square, res_pos(1860,1000))
            load += loading_rect(load)
            switch_controller = pygame.image.load(f"textures/ui/switch_controller.png").convert_alpha()
            switch_controller = pygame.transform.smoothscale(switch_controller, res_pos(200,200))
            load += loading_rect(load)
            joy_cons = pygame.image.load(f"textures/ui/joy_cons.png").convert_alpha()
            joy_cons = pygame.transform.smoothscale(joy_cons, res_pos(200,200))
            load += loading_rect(load)
            xbox_one_controller = pygame.image.load(f"textures/ui/xbox_one_controller.png").convert_alpha()
            xbox_one_controller = pygame.transform.smoothscale(xbox_one_controller, res_pos(200,200))
            load += loading_rect(load)
            ps4_controller = pygame.image.load(f"textures/ui/ps4_controller.png").convert_alpha()
            ps4_controller = pygame.transform.smoothscale(ps4_controller, res_pos(200,200))
            load += loading_rect(load)
            joy_conl = pygame.image.load(f"textures/ui/joy_conl.png").convert_alpha()
            joy_conl = pygame.transform.smoothscale(joy_conl, res_pos(200,100))
            load += loading_rect(load)
            joy_conr = pygame.image.load(f"textures/ui/joy_conr.png").convert_alpha()
            joy_conr = pygame.transform.smoothscale(joy_conr, res_pos(200,100))
            load += loading_rect(load)
            corner1 = pygame.image.load(f"textures/ui/corner1.png").convert_alpha()
            corner1 = pygame.transform.scale(corner1, res_pos(50,50))
            load += loading_rect(load)
            corner2 = pygame.image.load(f"textures/ui/corner2.png").convert_alpha()
            corner2 = pygame.transform.scale(corner2, res_pos(50,50))
            load += loading_rect(load)
            corner3 = pygame.image.load(f"textures/ui/corner3.png").convert_alpha()
            corner3 = pygame.transform.scale(corner3, res_pos(50,50))
            load += loading_rect(load)
            corner4 = pygame.image.load(f"textures/ui/corner4.png").convert_alpha()
            corner4 = pygame.transform.scale(corner4, res_pos(50,50))
            load += loading_rect(load)
            if event_waiting == False:
                window_surface.blit(move_text, res_pos(525,650))
                pygame.display.flip()
            if firstload == False:
                print("Bienvenue sur DodgeBOI 1.2!")
                firstload = True
        except:
                print("Erreur, textures(s) manquante(s), réinstallez le programme, si le problème persiste réinstallez pygame voir python.")
                input("Appuyez sur entré pour fermer le programme.")
            
        loaded = False

    if event_waiting == True:
        pressing = pygame.key.get_pressed()
        
        #Esc
        if pressing[pygame.K_ESCAPE]:
            keyboard_input[27] = True
        else:
            keyboard_input[27] = False
        
        #Return
        if pressing[pygame.K_RETURN]:
            keyboard_input[13] = True
        else:
            keyboard_input[13] = False
        
        #Z
        if pressing[pygame.K_w]:
            keyboard_input[119] = True
        else:
            keyboard_input[119] = False
        
        #S
        if pressing[pygame.K_s]:
            keyboard_input[115] = True
        else:
            keyboard_input[115] = False
        
        #A
        if pressing[pygame.K_q]:
            keyboard_input[113] = True
        else:
            keyboard_input[113] = False
        
        #E
        if pressing[pygame.K_e]:
            keyboard_input[101] = True
        else:
            keyboard_input[101] = False

        #1
        if pressing[pygame.K_KP1]:
            keyboard_input[257] = True
        else:
            keyboard_input[257] = False

        #2
        if pressing[pygame.K_KP2]:
            keyboard_input[258] = True
        else:
            keyboard_input[258] = False

        #3
        if pressing[pygame.K_KP3]:
            keyboard_input[259] = True
        else:
            keyboard_input[259] = False

        #K
        if pressing[pygame.K_k]:
            keyboard_input[107] = True
        else:
            keyboard_input[107] = False  

        #L
        if pressing[pygame.K_l]:
            keyboard_input[108] = True
        else:
            keyboard_input[108] = False  

        #M
        if pressing[pygame.K_SEMICOLON]:
            keyboard_input[59] = True
        else:
            keyboard_input[59] = False  

        #Space
        if pressing[pygame.K_SPACE]:
            keyboard_input[32] = True
        else:
            keyboard_input[32] = False
    
        
        x, y = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()
        

        if menu == 0: # MENU PRINCIPAL --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- MENU PRINCIPAL
            if menu_loaded != 0:
                no_button_rect = no_button.get_rect(topleft=res_pos(1200,600))
                yes_button_rect = yes_button.get_rect(topleft=res_pos(550,600))
                menu_loaded = 0
            
            window_surface.blit(bg, (0, 0))
            
            if controller_on > 2 and controller_on != 10000 and menu0_joystick_select <= 4:
                controller_square_icon(792,407+(125*menu0_joystick_select),1078,493+(125*menu0_joystick_select))
                if d_pad_negligerv() == 1 and no_input == True or stick1_negligerv() == 1 and no_input == True:
                    menu0_joystick_select += 1
                    if menu0_joystick_select > 4:
                        menu0_joystick_select = 0
                elif d_pad_negligerv() == 0 and no_input == True or stick1_negligerv() == 0 and no_input == True:
                    menu0_joystick_select -= 1
                    if menu0_joystick_select < 0:
                        menu0_joystick_select = 4
            
            if collision_square(res_pos(810,425), play_text) == True and controller_on != 2 or menu0_joystick_select == 0 and input_controller[6] and no_input == True:
                if click == False:
                    menu = 1
                    no_input = False
            elif collision_square(res_pos(810,550), setting_text) == True and controller_on != 2 or menu0_joystick_select == 1 and input_controller[6] and no_input == True:
                if click == False:
                    menu = 2
            elif collision_square(res_pos(810,675), score_text) == True and controller_on != 2 or menu0_joystick_select == 2 and input_controller[6] and no_input == True:
                if click == False:    
                    menu = 3
            elif collision_square(res_pos(810,800), text_tuto) == True and controller_on != 2 or menu0_joystick_select == 3 and input_controller[6] and no_input == True:
                if click == False:        
                    menu = 5 
                    no_input = False
            elif collision_square(res_pos(810,925), quit_text_min) == True and controller_on != 2 or click == True or controller_on > 2 and input_controller[12] or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and nokey_input == True or menu0_joystick_select == 4 and input_controller[6] and no_input == True:
                if click == False:
                    no_input = False
                    nokey_input = False
                    menu0_joystick_select = 5


                window_surface.blit(rect_quit, res_pos(460,340))
                window_surface.blit(yes_button, res_pos(550,600))
                window_surface.blit(no_button, res_pos(1200,600))
                window_surface.blit(yes_text, res_pos(590,615))
                window_surface.blit(no_text, res_pos(1230,615))
                window_surface.blit(quit_text, res_pos(560,335))

                if controller_on > 2 and controller_on != 10000:
                    if menu0_joystick_select == 5:
                        controller_square_icon(1180,580,1349,670)
                        if d_pad_negligerh() == 0 and no_input == True or d_pad_negligerh() == 1 and no_input == True or stick1_negligerh() == 1 and no_input == True or stick1_negligerh() == 0 and no_input == True:
                            menu0_joystick_select = 6
                    elif menu0_joystick_select == 6:
                        controller_square_icon(530,580,699,670)
                        if d_pad_negligerh() == 1 and no_input == True or d_pad_negligerh() == 0 and no_input == True or stick1_negligerh() == 0 and no_input == True or stick1_negligerh() == 1 and no_input == True:
                            menu0_joystick_select = 5
                
                click = True
                
                if pressed[0] and yes_button_rect.collidepoint(x,y) == 1 and mouse_click_left == False or event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and nokey_input == True or menu0_joystick_select == 6 and input_controller[6] and no_input == True:
                    launched = False
                elif pressed[0] and no_button_rect.collidepoint(x,y) == 1 and mouse_click_left == False or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and nokey_input == True or menu0_joystick_select == 5 and input_controller[6] and no_input == True:
                    click = False
                    menu0_joystick_select = 4
                    no_input = False

            if pressed[0] == 1 and controller_on != 2:
                mouse_click_left = True
            else:
                mouse_click_left = False

        if menu == 1: # EN JEU --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- EN JEU

            if menu_loaded != 1 and PAUSE != 2:
                    sfr = fps / 30
                    menu1_joystick_select = 0
                    block_collide1 = False
                    block_collide2 = False
                    block_collide3 = False
                    block_collideall = "none"
                    block_mov = {"block0" : 1920 , "block1" : 1920 ,"block2" : 1920 ,"block3" : 1920 ,"block4" : 1920 ,"block5" : 1920 ,"block6" : 1920 ,"block7" : 1920 ,"block8" : 1920 ,"block9" : 1920 ,"block10" : 1920 ,"block11" : 1920}
                    block_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    color_last = 1
                    color = "red"
                    PAUSE = 0
                    score_counter = 0
                    score = 0
                    frame = 1
                    player_pos = 1
                    player_pos_y = round((515/1080) * res[1])
                    press = 0
                    waiting = 20 * sfr * ((1/fps)/dt)
                    last = 0
                    speed = 1
                    fallx = res_posx(-2)*sfr
                    fally = res_posy(1)*sfr
                    did = False
                    joy_press = 0
                    jumping = 0
                    pause_input = False
                    kick = 0

                    stat_rect = stat.get_rect(topleft=res_pos(900,700))

                    menu_loaded = 1
            async_result = pool.apply_async(generateur, (waiting, last, color_last, block_collide1, block_collide2, block_collide3, block_collideall))
            window_surface.fill(black)
            if PAUSE < 1:
                if keyboard_input[113] == True or input_controller[9] == True:
                    position_of_player = 1
                elif keyboard_input[101] == True or input_controller[10] == True:
                    if jumping < 20*sfr+1:
                        position_of_player = 2
                        jumping += 1
                    elif jumping > 20*sfr:
                        position_of_player = 0
                        jumping = 21*sfr
                    else:
                        position_of_player = 0
                        jumping = 0
                elif keyboard_input[32] == True or input_controller[7] == True:
                    if kick < 5*sfr+1:
                        position_of_player = 3
                        kick += 1
                    elif kick > 5*sfr:
                        position_of_player = 0
                        kick = 12*sfr
                    else:
                        position_of_player = 0
                        kick = 0
                else:
                    position_of_player = 0
                    jumping = 0
                    kick = 0

                if keyboard_input[115] == True and position_of_player == 0: #Déplacment vers le bas
                    if player_pos == 2 and press == 0 and block_collide2 == 0:
                        player_pos_y = round((515/1080) * res[1])
                        press = 1
                        player_pos = 1
                    elif player_pos == 1 and press == 0 and block_collide3 == 0:
                        player_pos_y = round((875/1080) * res[1])
                        press = 1
                        player_pos = 0
                elif keyboard_input[119] == True and position_of_player == 0: #Déplacment vers le haut
                    if player_pos == 0 and press == 0 and block_collide2 == 0:
                        player_pos_y = round((515/1080) * res[1])
                        press = 1
                        player_pos = 1
                    elif player_pos == 1 and press == 0 and block_collide1 == 0:
                        player_pos_y = round((155/1080) * res[1])
                        press = 1
                        player_pos = 2

                if keyboard_input[115] == False and keyboard_input[119] == False: #Oblige le joueur à relever la touche pour rebouger
                    press = 0
                if controller_on > 2 and controller_on != 10000:
                    if d_pad_negligerv() == 1 and axis_press == 0 and position_of_player == 0: #Déplacment vers le bas
                        if player_pos == 2 and block_collide2 == 0:
                            player_pos_y = round((515/1080) * res[1])
                            player_pos = 1
                        elif player_pos == 1 and block_collide3 == 0:
                            player_pos_y = round((875/1080) * res[1])
                            player_pos = 0
                        axis_press = 1
                    elif d_pad_negligerv() == 0 and axis_press == 0 and position_of_player == 0: #Déplacment vers le haut
                        if player_pos == 0 and block_collide2 == 0:
                            player_pos_y = round((515/1080) * res[1])
                            player_pos = 1
                        elif player_pos == 1 and block_collide1 == 0:
                            player_pos_y = round((155/1080) * res[1])
                            player_pos = 2
                        axis_press = 1

                    if stick1_negligerv() == 1 and joy_press == 0 and position_of_player == 0: #Déplacment vers le bas
                        if player_pos == 2 and block_collide2 == 0:
                            player_pos_y = round((515/1080) * res[1])
                            player_pos = 1
                        elif player_pos == 1 and block_collide3 == 0:
                            player_pos_y = round((875/1080) * res[1])
                            player_pos = 0
                        joy_press = 1
                    elif stick1_negligerv() == 0 and joy_press == 0 and position_of_player == 0: #Déplacment vers le haut
                        if player_pos == 0 and block_collide2 == 0:
                            player_pos_y = round((515/1080) * res[1])
                            player_pos = 1
                        elif player_pos == 1 and block_collide1 == 0:
                            player_pos_y = round((155/1080) * res[1])
                            player_pos = 2
                        joy_press = 1

                if d_pad_negligerv() == -1:
                    axis_press = 0

                if stick1_negligerv() == -1:
                    joy_press = 0

                if no_input == True or input_controller[9] or input_controller[10]:
                    if keyboard_input[257] == True or keyboard_input[107] == True or input_controller[8]: # Change la couleur du bandana
                        color = "red"
                    elif keyboard_input[258] == True or keyboard_input[108] == True or input_controller[6]:
                        color = "blue"
                    elif keyboard_input[259] == True or keyboard_input[59] == True or input_controller[5]:
                        color = "yellow"

            waiting, last, color_last, block_collide1, block_collide2, block_collide3, block_collideall = async_result.get()
            text_score = text_50a.render(f"Score : {score}", text_aliasing, white)
            window_surface.blit(text_score, res_pos(5,5)) #affichage de plusieur éléments
            text_waiting = text_20a.render(f"waiting = {waiting}", text_aliasing, white)
            text_block_id = text_20a.render(f"block_id = {block_id}", text_aliasing, white)
            text_color = text_20a.render(f"color  = {color}", text_aliasing, white)
            text_sfr = text_20a.render(f"sfr  = {sfr}", text_aliasing, white)
            window_surface.blit(text_waiting, res_pos(1750,5))
            window_surface.blit(text_block_id, res_pos(1500,30))
            text_speed = text_20a.render(f"speed  = {speed}", text_aliasing, white)
            window_surface.blit(text_speed, res_pos(1750,55))
            window_surface.blit(text_color, res_pos(1800,80))
            window_surface.blit(text_sfr ,res_pos(1800,105))
            text_collider1 = text_20a.render(f"block_collide1  = {block_collide1}", text_aliasing, white)
            window_surface.blit(text_collider1 ,res_pos(1650,130))
            text_collider2 = text_20a.render(f"block_collide2  = {block_collide2}", text_aliasing, white)
            window_surface.blit(text_collider2 ,res_pos(1650,155))
            text_collider3 = text_20a.render(f"block_collide3  = {block_collide3}", text_aliasing, white)
            window_surface.blit(text_collider3 ,res_pos(1650,180))
            text_colliderall = text_20a.render(f"block_collideall  = {block_collideall}", text_aliasing, white)
            window_surface.blit(text_colliderall ,res_pos(1650,205))

            if PAUSE < 2:
                if (2*sfr)+1 > frame > 0: #Animation du personnage quand il court
                    if color == "red":
                        if position_of_player == 1:
                            window_surface.blit(slide1r, [res_posx(200), player_pos_y])
                        elif position_of_player == 3:
                            window_surface.blit(kick1r, [res_posx(200), player_pos_y+res_posy(-35)])
                        elif position_of_player == 2:
                            window_surface.blit(jump1r, [res_posx(200), player_pos_y+res_posy(-55)])
                        elif position_of_player == 0:
                            window_surface.blit(runner1r, [res_posx(200), player_pos_y])
                    elif color == "blue":
                        if position_of_player == 1:
                            window_surface.blit(slide1b, [res_posx(200), player_pos_y])
                        elif position_of_player == 3:
                            window_surface.blit(kick1b, [res_posx(200), player_pos_y+res_posy(-35)])
                        elif position_of_player == 2:
                            window_surface.blit(jump1b, [res_posx(200), player_pos_y+res_posy(-55)])
                        elif position_of_player == 0:
                            window_surface.blit(runner1b, [res_posx(200), player_pos_y])
                    elif color == "yellow":
                        if position_of_player == 1:
                            window_surface.blit(slide1y, [res_posx(200), player_pos_y])
                        elif position_of_player == 3:
                            window_surface.blit(kick1y, [res_posx(200), player_pos_y+res_posy(-35)])
                        elif position_of_player == 2:
                            window_surface.blit(jump1y, [res_posx(200), player_pos_y+res_posy(-55)])
                        elif position_of_player == 0:
                            window_surface.blit(runner1y, [res_posx(200), player_pos_y])
                if (4*sfr)+1 > frame > (2*sfr):
                    if color == "red":
                        if position_of_player == 1:
                            window_surface.blit(slide2r, [res_posx(200), player_pos_y])
                        elif position_of_player == 3:
                            window_surface.blit(kick2r, [res_posx(200), player_pos_y+res_posy(-35)])
                        elif position_of_player == 2:
                            window_surface.blit(jump2r, [res_posx(200), player_pos_y+res_posy(-55)])
                        elif position_of_player == 0:
                            window_surface.blit(runner2r, [res_posx(200), player_pos_y])
                    elif color == "blue":
                        if position_of_player == 1:
                            window_surface.blit(slide2b, [res_posx(200), player_pos_y])
                        elif position_of_player == 3:
                            window_surface.blit(kick2b, [res_posx(200), player_pos_y+res_posy(-35)])
                        elif position_of_player == 2:
                            window_surface.blit(jump2b, [res_posx(200), player_pos_y+res_posy(-55)])
                        elif position_of_player == 0:
                            window_surface.blit(runner2b, [res_posx(200), player_pos_y])
                    elif color == "yellow":
                        if position_of_player == 1:
                            window_surface.blit(slide2y, [res_posx(200), player_pos_y])
                        elif position_of_player == 3:
                            window_surface.blit(kick2y, [res_posx(200), player_pos_y+res_posy(-35)])
                        elif position_of_player == 2:
                            window_surface.blit(jump2y, [res_posx(200), player_pos_y+res_posy(-55)])
                        elif position_of_player == 0:
                            window_surface.blit(runner2y, [res_posx(200), player_pos_y])
                if (6*sfr)+1 > frame > (4*sfr):
                    if color == "red":
                        if position_of_player == 1:
                            window_surface.blit(slide3r, [res_posx(200), player_pos_y])
                        elif position_of_player == 3:
                            window_surface.blit(kick3r, [res_posx(200), player_pos_y+res_posy(-35)])
                        elif position_of_player == 2:
                            window_surface.blit(jump3r, [res_posx(200), player_pos_y+res_posy(-55)])
                        elif position_of_player == 0:
                            window_surface.blit(runner3r, [res_posx(200), player_pos_y])
                    elif color == "blue":
                        if position_of_player == 1:
                            window_surface.blit(slide3b, [res_posx(200), player_pos_y])
                        elif position_of_player == 3:
                            window_surface.blit(kick3b, [res_posx(200), player_pos_y+res_posy(-35)])
                        elif position_of_player == 2:
                            window_surface.blit(jump3b, [res_posx(200), player_pos_y+res_posy(-55)])
                        elif position_of_player == 0:
                            window_surface.blit(runner3b, [res_posx(200), player_pos_y])
                    elif color == "yellow":
                        if position_of_player == 1:
                            window_surface.blit(slide3y, [res_posx(200), player_pos_y])
                        elif position_of_player == 3:
                            window_surface.blit(kick3y, [res_posx(200), player_pos_y+res_posy(-35)])
                        elif position_of_player == 2:
                            window_surface.blit(jump3y, [res_posx(200), player_pos_y+res_posy(-55)])
                        elif position_of_player == 0:
                            window_surface.blit(runner3y, [res_posx(200), player_pos_y])
                if (8*sfr)+1 > frame > (6*sfr):
                    if color == "red":
                        if position_of_player == 1:
                            window_surface.blit(slide4r, [res_posx(200), player_pos_y])
                        elif position_of_player == 3:
                            window_surface.blit(kick4r, [res_posx(200), player_pos_y+res_posy(-35)])
                        elif position_of_player == 2:
                            window_surface.blit(jump4r, [res_posx(200), player_pos_y+res_posy(-55)])
                        elif position_of_player == 0:
                            window_surface.blit(runner4r, [res_posx(200), player_pos_y])
                    elif color == "blue":
                        if position_of_player == 1:
                            window_surface.blit(slide4b, [res_posx(200), player_pos_y])
                        elif position_of_player == 3:
                            window_surface.blit(kick4b, [res_posx(200), player_pos_y+res_posy(-35)])
                        elif position_of_player == 2:
                            window_surface.blit(jump4b, [res_posx(200), player_pos_y+res_posy(-55)])
                        elif position_of_player == 0:
                            window_surface.blit(runner4b, [res_posx(200), player_pos_y])
                    elif color == "yellow":
                        if position_of_player == 1:
                            window_surface.blit(slide4y, [res_posx(200), player_pos_y])
                        elif position_of_player == 3:
                            window_surface.blit(kick4y, [res_posx(200), player_pos_y+res_posy(-35)])
                        elif position_of_player == 2:
                            window_surface.blit(jump4y, [res_posx(200), player_pos_y+res_posy(-55)])
                        elif position_of_player == 0:
                            window_surface.blit(runner4y, [res_posx(200), player_pos_y])
                if PAUSE < 1:
                    frame += 1
                if frame == (8*sfr)+1:
                    frame = 1

            if PAUSE < 1:
                if speed <= 2.5:
                    speed = score * 0.005 + 1

                if score_counter < (30*sfr): #Compteur de score
                    score_counter += 1
                else:
                    score_counter = 0
                    score += 1

                if block_collide1 == 1 and player_pos == 2 or block_collide2 == 1 and player_pos == 1 or block_collide3 == 1 and player_pos == 0 or block_collideall != "none" and block_collideall != color or block_collide1 == 2 and player_pos == 2 and position_of_player != 1 or block_collide2 == 2 and player_pos == 1 and position_of_player != 1 or block_collide3 == 2 and player_pos == 0 and position_of_player != 1 or block_collide1 == 3 and player_pos == 2 and position_of_player != 2 or block_collide2 == 3 and player_pos == 1 and position_of_player != 2 or block_collide3 == 3 and player_pos == 0 and position_of_player != 2 or block_collide1 == 4 and player_pos == 2 and position_of_player != 3 or block_collide2 == 4 and player_pos == 1 and position_of_player != 3 or block_collide3 == 4 and player_pos == 0 and position_of_player != 3:
                    PAUSE = 2
                    menu1_joystick_select = 2

                if keyboard_input[27] == True or input_controller[12] == True and no_input == True or input_controller[12] and pause_input == True: #Activer la pause
                    PAUSE = 1
                    menu1_joystick_select = 0
                    no_input = False
                    pause_input = False
            if PAUSE == 1: # PAUSE --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- PAUSE
                window_surface.blit(pause_square, res_pos(320,180))
                window_surface.blit(text_pause, res_pos(650,300))
                pygame.draw.rect(window_surface, black, rect_form)

                if controller_on == 3 and controller_on != 0:
                    if menu1_joystick_select == 0:
                            controller_square_icon(1080,680,1370,770)
                            if d_pad_negligerh() == 0 and no_input == True or d_pad_negligerh() == 1 and no_input == True or stick1_negligerh() == 1 and no_input == True or stick1_negligerh() == 0 and no_input == True:
                                menu1_joystick_select = 1
                    elif menu1_joystick_select == 1:
                        controller_square_icon(480,680,770,770)
                        if d_pad_negligerh() == 1 and no_input == True or d_pad_negligerh() == 0 and no_input == True or stick1_negligerh() == 1 and no_input == True or stick1_negligerh() == 0 and no_input == True:
                            menu1_joystick_select = 0
                if collision_square(res_pos(500,700), text_main_menu) or input_controller[6] and no_input == True and menu1_joystick_select == 1:
                    menu = 0
                    PAUSE = 0
                if collision_square(res_pos(1100,700), text_resume) or input_controller[6] and no_input == True and menu1_joystick_select == 0 or input_controller[12] and no_input == True or input_controller[12] == True and pause_input == True:
                    PAUSE = 0
                    pause_input = False


            if PAUSE == 2: # PERDU --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- PERDU
                if color == "red":
                    runnerfall = runnerfallred
                    runnerground = runnergroundred
                elif color == "blue":
                    runnerfall = runnerfallblue
                    runnerground = runnergroundblue
                elif color == "yellow":
                    runnerfall = runnerfallyellow
                    runnerground = runnergroundyellow

                if fallx > res_posx(-60):
                    fallx += res_posx(-8)
                    fally += res_posy(-2)
                    window_surface.blit(runnerfall, (res_posx(200)+fallx,player_pos_y+fally))
                else:
                    window_surface.blit(runnerground, (res_posx(200)+fallx,player_pos_y+fally))
                    pygame.draw.rect(window_surface, black, rect_form)

                    window_surface.blit(pause_square, res_pos(320,180))
                    window_surface.blit(text_lose, res_pos(400,250))

                    text_score = text_90a.render(f"Score : {score}", text_aliasing, white)
                    window_surface.blit(text_score, res_pos(700,500))


                    window_surface.blit(stat, res_pos(900,700))
                    stat_collide = stat_rect.collidepoint(x,y)

                    if controller_on > 2 and controller_on != 10000:
                        if menu1_joystick_select == 2:
                            controller_square_icon(1080,680,1370,770)
                            if d_pad_negligerh() == 1 and no_input == True or stick1_negligerh() == 1 and no_input == True:
                                menu1_joystick_select = 4
                            elif d_pad_negligerh() == 0 and no_input == True or stick1_negligerh() == 0 and no_input == True:
                                menu1_joystick_select = 3
                        elif menu1_joystick_select == 3:
                            controller_square_icon(880,680,970,770)
                            if d_pad_negligerh() == 1 and no_input == True or stick1_negligerh() == 1 and no_input == True:
                                menu1_joystick_select = 2
                            elif d_pad_negligerh() == 0 and no_input == True or stick1_negligerh() == 0 and no_input == True:
                                menu1_joystick_select = 4
                        elif menu1_joystick_select == 4:
                            controller_square_icon(480,680,770,770)
                            if d_pad_negligerh() == 1 and no_input == True or stick1_negligerh() == 1 and no_input == True:
                                menu1_joystick_select = 3
                            elif d_pad_negligerh() == 0 and no_input == True or stick1_negligerh() == 0 and no_input == True:
                                menu1_joystick_select = 2

                    if did == False:
                        if len(score_data) == 10:
                            score_data.append(score)
                            score_data.sort(reverse = True)
                            del score_data[len(score_data)-1]
                        else:
                            score_data.append(score)
                        with open("score.txt", "w") as s:
                            for i in range(len(score_data)):
                                s.write(f"{score_data[i]}\n")
                        did = True
                    if collision_square(res_pos(500,700), text_main_menu) or input_controller[6] and no_input == True and menu1_joystick_select == 4:
                        menu = 0
                        PAUSE = 0
                        did = False
                    if collision_square(res_pos(1100,700), text_retry) or input_controller[6] and no_input == True and menu1_joystick_select == 2:
                        PAUSE = 0
                        menu_loaded = 0
                        did = False
                    if pressed[0] and stat_collide == 1 or input_controller[12] and no_input == True or input_controller[6] and no_input == True and menu1_joystick_select == 3:
                        menu = 4

            if pressed[0] == 1:
                mouse_click_left = True
            else:
                mouse_click_left = False

            if input_controller[12] == False:
                pause_input = True
            else:
                pause_input = False

        if menu == 2: # PARAMETRES --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- PARAMETRES
            window_surface.fill(black)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                menu = 0
            
            if menu_loaded != 2:
                menu2_joystick_select = 0

                croix_rect = croix.get_rect(topleft=res_pos(1875,15))

                language_icon_rect = language_icon_eng.get_rect(topleft=res_pos(350,260))
                if langue == 0: # Langue
                    temp_langue = 0
                elif langue == 1:
                    temp_langue = 1

                aliasing_rect = valid.get_rect(topleft=res_pos(700,410))
                if text_aliasing == True: # Activer/Désactiver l'aliasing du texte
                    temp_text_aliasing = True
                elif text_aliasing == False:
                    temp_text_aliasing = False

                res_block_rect = res_block.get_rect(topleft=res_pos(875,468)) # Choisir la résolution
                stay = False
                temp_res = res
                res_select = 0

                fullscreen_rect = valid.get_rect(topleft=res_pos(575,560))
                if fullscreen == 1:  # Activer/Désactiver le plein écran
                    temp_fullscreen = 1
                elif fullscreen == 0:
                    temp_fullscreen = 0


                show_fps_rect = valid.get_rect(topleft=res_pos(450,335))
                less_framerate = left_arrow.get_rect(topleft=res_pos(460,637))
                more_framerate = right_arrow.get_rect(topleft=res_pos(610,637))
                temp_fps = fps #Modifier framerate
                if fps == 30:
                    framerate_id = 0
                elif fps == 60:
                    framerate_id = 1
                elif fps == 120:
                    framerate_id = 2
                elif fps == 240:
                    framerate_id = 3
                elif fps == 360:
                    framerate_id = 4
                elif fps == 480:
                    framerate_id = 5

                rtyp = False # Gérer manettes
                controller_res_select = 0

                menu_loaded = 2

            window_surface.blit(setting_text_in_setting, res_pos(320,-30))
            window_surface.blit(text_language, res_pos(40,250))
            window_surface.blit(text_show_fps, res_pos(40,325))
            window_surface.blit(text_setting_aliasing, res_pos(40,400))
            window_surface.blit(text_res, res_pos(40,475))   
            window_surface.blit(text_fullscreen, res_pos(40,550))
            window_surface.blit(text_framerate, res_pos(40,625))
            framerate = text_50a.render(str(temp_fps), text_aliasing, white)
            window_surface.blit(framerate, res_pos(510,630))
            
            if collision_back(1840,20) == True or no_input == True and input_controller[5] and stay == False:
                menu = 0

            #Modifier la résolution
            window_surface.blit(res_block, res_pos(875,468))
            resolution = text_50a.render(f"{temp_res[0]}x{temp_res[1]}", text_aliasing, white)
            window_surface.blit(resolution, res_pos(887,475))
            if pressed[0] and res_block_rect.collidepoint(x,y) == 1 and mouse_click_left == False or stay == True or menu2_joystick_select == 3 and no_input == True and input_controller[6]:
                if stay == False:
                    mouse_click_left = True
                    stay = True
                    no_input = False
                    other_res = [[3840,2160], [2560,1440], [1920,1080], [1600,900], [1366,768], [1280,720], [800,450]]
                    valid_res = []
                    for i in range(len(other_res)):
                        if other_res[i] != res:
                            valid_res.append(other_res[i])
                            if controller_on > 2 and controller_on != 10000:
                                controller_res_select = 0
                if controller_on > 2 and controller_on != 10000:
                    pygame.draw.circle(window_surface, white, res_pos(850, 505+(controller_res_select*60)),res_posx(10))
                    if d_pad_negligerv() == 1 and no_input == True or stick1_negligerv() == 1 and no_input == True:
                        controller_res_select += 1
                        if controller_res_select > len(valid_res):
                            controller_res_select = 0
                    elif d_pad_negligerv() == 0 and no_input == True or stick1_negligerv() == 0 and no_input == True:
                        controller_res_select -= 1
                        if controller_res_select < 0:
                            controller_res_select = len(valid_res)
                
                for i in range(len(valid_res)):
                    res_block_next_rect = res_block.get_rect(topleft=res_pos(875,528+(i*60)))
                    window_surface.blit(res_block_next, res_pos(875,528+(i*60)))
                    showing_res = valid_res[i]
                    other_res_text = text_50a.render(f"{showing_res[0]}x{showing_res[1]}", text_aliasing, white)
                    window_surface.blit(other_res_text, res_pos(895,528+(i*60)+7))
                    if pressed[0] and mouse_click_left == False or no_input == True and input_controller[5] or input_controller[6] and no_input == True:
                        stay = False
                        if res_block_next_rect.collidepoint(x,y) == 1 or controller_res_select == i+1 and input_controller[6] and no_input == True:
                            temp_res = valid_res[i]
                            if temp_fullscreen == 1:
                                tres = res

            

            if temp_langue == 0: # Langue
                window_surface.blit(language_icon_eng, res_pos(350,260))
            elif temp_langue == 1:
                window_surface.blit(language_icon_fr, res_pos(350,260))
            language_icon_collide = language_icon_rect.collidepoint(x,y)

            if pressed[0] and language_icon_collide == 1 and mouse_click_left == False  or menu2_joystick_select == 0 and no_input == True and input_controller[6]:
                if temp_langue == 0:
                    temp_langue = 1
                elif temp_langue == 1:
                    temp_langue = 0

            if temp_langue == 0:
                langue_update = "english"
            elif temp_langue == 1:
                langue_update = "french"


            if show_fps == True: # Afficher les fps
                window_surface.blit(valid, res_pos(450,335))
            elif show_fps == False:
                window_surface.blit(invalid, res_pos(450,335))
            show_fps_collide = show_fps_rect.collidepoint(x,y)

            if pressed[0] and show_fps_collide == 1 and mouse_click_left == False or menu2_joystick_select == 1 and no_input == True and input_controller[6]:
                if show_fps == True:
                    show_fps = False
                elif show_fps == False:
                    show_fps = True
                custom_setting_list = [str(res[0]), str(res[1]), str(int(text_aliasing)), str(fullscreen), str(int(show_fps)), str(fps), langue_update]
                with open("custom_setting.txt", "w") as s:
                    for i in range(len(custom_setting_list)-1):
                        s.write(f"{custom_setting_list[i]}\n")
                    s.write(langue_update)


            if temp_text_aliasing == True: # Activer/Désactiver l'aliasing du texte
                window_surface.blit(valid, res_pos(700,410))
            elif temp_text_aliasing == False:
                window_surface.blit(invalid, res_pos(700,410))
            aliasing_collide = aliasing_rect.collidepoint(x,y)

            if pressed[0] and aliasing_collide == 1 and mouse_click_left == False or menu2_joystick_select == 2 and no_input == True and input_controller[6]:
                if temp_text_aliasing == True:
                    temp_text_aliasing = False
                elif temp_text_aliasing == False:
                    temp_text_aliasing = True


            if temp_fullscreen == 1: # Activer/Désactiver le plein écran
                window_surface.blit(valid, res_pos(575,560))
            elif temp_fullscreen == 0:
                window_surface.blit(invalid, res_pos(575,560))
            fullscreen_collide = fullscreen_rect.collidepoint(x,y)

            if pressed[0] and fullscreen_collide == 1 and mouse_click_left == False or menu2_joystick_select == 4 and no_input == True and input_controller[6]:
                if temp_fullscreen == 1:
                    temp_fullscreen = 0
                elif temp_fullscreen == 0:
                    temp_fullscreen = 1

            less_framerate_collide = 0 # Modifier la framelimit
            more_framerate_collide = 0
            if temp_fps != 30:
                window_surface.blit(left_arrow, res_pos(460,637))
                less_framerate_collide = less_framerate.collidepoint(x,y)
                if pressed[0] and less_framerate_collide == 1 and mouse_click_left == False or menu2_joystick_select == 5 and no_input == True and d_pad_negligerh() == 0 or stick1_negligerh() == 0 and no_input == True and menu2_joystick_select == 5:
                    framerate_id += -1
            if temp_fps != 480:
                window_surface.blit(right_arrow, res_pos(610,637))
                more_framerate_collide = more_framerate.collidepoint(x,y)
                if pressed[0] and more_framerate_collide == 1 and mouse_click_left == False or menu2_joystick_select == 5 and no_input == True and d_pad_negligerh() == 1 or stick1_negligerh() == 1 and no_input == True and menu2_joystick_select == 5:
                    framerate_id += 1
            temp_fps = valid_framerate_list[framerate_id]
            
            # Gérer manettes -----------------------------------------------------------------

            if controller_on != 0: #Déconnecter manettes    
                if collision_square(res_pos(20,950), text_cdisconnect)  and mouse_click_left == False or menu2_joystick_select == 7 and no_input == True and input_controller[6] or rtyp == True:
                    if input_controller[6] == True:
                        rtyp = True
                    else:
                        controller_on = 0
                        mon_joystick1.quit()
                        pygame.joystick.quit()
                        rtyp = False
            else: # Connecter manettes
                if collision_square(res_pos(20,950), text_cconnect) and mouse_click_left == False:
                    controller_on = -1

            # Appliquer les modifs -----------------------------------------------------------------

            if controller_on == 3 and controller_on != 0 and stay == False:
                point_pos = [275,355,430,502,580,655]
                if menu2_joystick_select >= 0 and menu2_joystick_select <= 5:
                    pygame.draw.circle(window_surface, white, res_pos(20, point_pos[menu2_joystick_select]),res_posx(10))
                    if d_pad_negligerv() == 1 and no_input == True or stick1_negligerv() == 1 and no_input == True:
                        menu2_joystick_select += 1
                    elif d_pad_negligerv() == 0 and no_input == True or stick1_negligerv() == 0 and no_input == True:
                        menu2_joystick_select -= 1
                        if menu2_joystick_select < 0:
                            menu2_joystick_select = 6
                elif menu2_joystick_select == 6:
                    controller_square_icon(1580,930,1870,1020)
                    if d_pad_negligerv() == 1 and no_input == True or stick1_negligerv() == 1 and no_input == True:
                        menu2_joystick_select = 0
                    elif d_pad_negligerv() == 0 and no_input == True or stick1_negligerv() == 0 and no_input == True:
                        menu2_joystick_select = 5
                    if d_pad_negligerh() == 1 and no_input == True or stick1_negligerh() == 1 and no_input == True:
                        menu2_joystick_select = 7
                    elif d_pad_negligerh() == 0 and no_input == True or stick1_negligerh() == 0 and no_input == True:
                        menu2_joystick_select = 7
                elif menu2_joystick_select == 7:
                    controller_square_icon(0,930,290,1020)
                    if d_pad_negligerv() == 1 and no_input == True or stick1_negligerv() == 1 and no_input == True:
                        menu2_joystick_select = 0
                    elif d_pad_negligerv() == 0 and no_input == True or stick1_negligerv() == 0 and no_input == True:
                        menu2_joystick_select = 5
                    if d_pad_negligerh() == 1 and no_input == True or stick1_negligerh() == 1 and no_input == True:
                        menu2_joystick_select = 6
                    elif d_pad_negligerh() == 0 and no_input == True or stick1_negligerh() == 0 and no_input == True:
                        menu2_joystick_select = 6

            if collision_square(res_pos(1600,950), text_apply) and mouse_click_left == False or menu2_joystick_select == 6 and no_input == True and input_controller[6]:

                langue = temp_langue
                text_aliasing = temp_text_aliasing
                fullscreen = temp_fullscreen
                fps = valid_framerate_list[framerate_id]
                res = temp_res

                custom_setting_list = [str(res[0]), str(res[1]), str(int(text_aliasing)), str(fullscreen), str(int(show_fps)), str(fps), langue_update]
                with open("custom_setting.txt", "w") as s:
                    for i in range(len(custom_setting_list)-1):
                        s.write(f"{custom_setting_list[i]}\n")
                    s.write(langue_update)
                loaded = True
                menu_loaded = -1

            if pressed[0] == 1:
                mouse_click_left = True
            else:
                mouse_click_left = False

        if menu == 3 or menu == 4: # STATS --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- STATS

            if menu_loaded != 3:
                menu3_joystick_select = 0
                score_data.sort(reverse = True)
                menu_loaded = 3

            window_surface.fill(black)
            window_surface.blit(text_highscore, res_pos(500,0))
            for i in range(len(score_data)):
                window_surface.blit(text_90a.render(f"Score {i+1} : {score_data[i]}", text_aliasing, green), res_pos(550,215+i*83))

            if collision_back(1840,20) == True or no_input == True and input_controller[5]:
                if menu == 3 or input_controller[5] and menu == 3:
                    menu = 0
                elif menu == 4 or input_controller[5] and menu == 4:
                    PAUSE = 2
                    menu = 1

            if pressed[0] == 1:
                mouse_click_left = True
            else:
                mouse_click_left = False

        if menu == 5: # TUTORIEL --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- TUTORIEL
            window_surface.fill(black)
            if menu_loaded != 1 and PAUSE != 2:
                    sfr = fps / 30
                    menu1_joystick_select = 0
                    block_collide1 = False
                    block_collide2 = False
                    block_collide3 = False
                    block_collideall = "none"
                    block_mov = {"block0" : 1920 , "block1" : 1920 ,"block2" : 1920 ,"block3" : 1920 ,"block4" : 1920 ,"block5" : 1920 ,"block6" : 1920 ,"block7" : 1920 ,"block8" : 1920 ,"block9" : 1920 ,"block10" : 1920 ,"block11" : 1920}
                    block_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    color_last = 1
                    color = "red"
                    PAUSE = 0
                    score_counter = 0
                    score = 0
                    frame = 1
                    player_pos = 1
                    player_pos_y = round((515/1080) * res[1])
                    press = 0
                    waiting = 90 * sfr * ((1/fps)/dt)
                    last = 0
                    speed = 1
                    fallx = res_posx(-2)*sfr
                    fally = res_posy(1)*sfr
                    did = False
                    joy_press = 0
                    jumping = 0
                    pause_input = False
                    kick = 0
                    trying = -100
                    state = 0
                    explain_text = 0
                    last_trying = 0

                    menu_loaded = 1


            window_surface.fill(black)
            if PAUSE < 1:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q or input_controller[9] == True:
                    position_of_player = 1
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_e or input_controller[10] == True:
                    if jumping < 20*sfr+1:
                        position_of_player = 2
                        jumping += 1
                    elif jumping > 20*sfr:
                        position_of_player = 0
                        jumping = 21*sfr
                    else:
                        position_of_player = 0
                        jumping = 0
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE or input_controller[7] == True:
                    if kick < 5*sfr+1:
                        position_of_player = 3
                        kick += 1
                    elif kick > 5*sfr:
                        position_of_player = 0
                        kick = 12*sfr
                    else:
                        position_of_player = 0
                        kick = 0
                else:
                    position_of_player = 0
                    jumping = 0
                    kick = 0

                if event.type == pygame.KEYDOWN and event.key == pygame.K_s and position_of_player == 0: #Déplacment vers le bas
                    if player_pos == 2 and press == 0 and block_collide2 == 0:
                        player_pos_y = round((515/1080) * res[1])
                        press = 1
                        player_pos = 1
                    elif player_pos == 1 and press == 0 and block_collide3 == 0:
                        player_pos_y = round((875/1080) * res[1])
                        press = 1
                        player_pos = 0
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_w and position_of_player == 0: #Déplacment vers le haut
                    if player_pos == 0 and press == 0 and block_collide2 == 0:
                        player_pos_y = round((515/1080) * res[1])
                        press = 1
                        player_pos = 1
                    elif player_pos == 1 and press == 0 and block_collide1 == 0:
                        player_pos_y = round((155/1080) * res[1])
                        press = 1
                        player_pos = 2

                if event.type == pygame.KEYUP: #Oblige le joueur à relever la touche pour rebouger
                    press = 0

                if controller_on > 2 and controller_on != 10000:
                    if d_pad_negligerv() == 1 and axis_press == 0 and position_of_player == 0: #Déplacment vers le bas
                        if player_pos == 2 and block_collide2 == 0:
                            player_pos_y = round((515/1080) * res[1])
                            player_pos = 1
                        elif player_pos == 1 and block_collide3 == 0:
                            player_pos_y = round((875/1080) * res[1])
                            player_pos = 0
                        axis_press = 1
                    elif d_pad_negligerv() == 0 and axis_press == 0 and position_of_player == 0: #Déplacment vers le haut
                        if player_pos == 0 and block_collide2 == 0:
                            player_pos_y = round((515/1080) * res[1])
                            player_pos = 1
                        elif player_pos == 1 and block_collide1 == 0:
                            player_pos_y = round((155/1080) * res[1])
                            player_pos = 2
                        axis_press = 1

                    if stick1_negligerv() == 1 and joy_press == 0 and position_of_player == 0: #Déplacment vers le bas
                        if player_pos == 2 and block_collide2 == 0:
                            player_pos_y = round((515/1080) * res[1])
                            player_pos = 1
                        elif player_pos == 1 and block_collide3 == 0:
                            player_pos_y = round((875/1080) * res[1])
                            player_pos = 0
                        joy_press = 1
                    elif stick1_negligerv() == 0 and joy_press == 0 and position_of_player == 0: #Déplacment vers le haut
                        if player_pos == 0 and block_collide2 == 0:
                            player_pos_y = round((515/1080) * res[1])
                            player_pos = 1
                        elif player_pos == 1 and block_collide1 == 0:
                            player_pos_y = round((155/1080) * res[1])
                            player_pos = 2
                        joy_press = 1

                if d_pad_negligerv() == -1:
                    axis_press = 0

                if stick1_negligerv() == -1:
                    joy_press = 0

                if no_input == True or input_controller[9] or input_controller[10]:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_KP1 or event.type == pygame.KEYDOWN and event.key == pygame.K_k or input_controller[8] and trying > -1: # Change la couleur du bandana
                        color = "red"
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_KP2 or event.type == pygame.KEYDOWN and event.key == pygame.K_l or input_controller[6] and trying > -1:
                        color = "blue"
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_KP3 or event.type == pygame.KEYDOWN and event.key == pygame.K_SEMICOLON or input_controller[5] and trying > -1:
                        color = "yellow"

                
                if waiting <= 0 or div_wait == True: #générateur 
                    if trying == 0:
                        if state == 0:
                            for i in range(len(block_id)):
                                if block_id[i] == 0:
                                    block_id.insert(i , 1)
                                    del block_id[i+1]
                                    last = 1
                                    state = 1
                                    break
                        elif state == 1:
                            for i in range(len(block_id)):
                                if block_id[i] == 0:
                                    block_id.insert(i , 2)
                                    del block_id[i+1]
                                    last = 2
                                    state = 2
                                    break
                        elif state == 2:
                            for i in range(len(block_id)):
                                if block_id[i] == 0:
                                    block_id.insert(i , 3)
                                    del block_id[i+1]
                                    last = 3
                                    trying = 5
                                    state = 0
                                    break
                    elif trying == 1:
                        if state == 0:
                            for i in range(len(block_id)):
                                if block_id[i] == 0:
                                    block_id.insert(i , 7)
                                    del block_id[i+1]
                                    last = 7
                                    color_last = 1
                                    state = 1
                                    break
                        elif state == 1:
                            for i in range(len(block_id)):
                                if block_id[i] == 0:
                                    block_id.insert(i , 8)
                                    del block_id[i+1]
                                    last = 7
                                    color_last = 2
                                    state = 2
                                    break
                        elif state == 2:
                            for i in range(len(block_id)):
                                if block_id[i] == 0:
                                    block_id.insert(i , 9)
                                    del block_id[i+1]
                                    last = 7
                                    color_last = 3
                                    trying = 5
                                    state = 0
                                    break
                    elif trying == 2:
                        if state == 0:
                            for i in range(len(block_id)):
                                if block_id[i] == 0:
                                    block_id.insert(i , 10)
                                    del block_id[i+1]
                                    last = 7
                                    color_last = 1
                                    state = 1
                                    break
                        elif state == 1:
                            for i in range(len(block_id)):
                                if block_id[i] == 0:
                                    block_id.insert(i , 13)
                                    del block_id[i+1]
                                    last = 7
                                    color_last = 2
                                    state = 2
                                    break
                        elif state == 2:
                            for i in range(len(block_id)):
                                if block_id[i] == 0:
                                    block_id.insert(i , 16)
                                    del block_id[i+1]
                                    last = 7
                                    color_last = 3
                                    state = 0
                                    trying = 5
                                    break
                    elif trying == 3:
                        if state == 0:
                            for i in range(len(block_id)):
                                if block_id[i] == 0:
                                    block_id.insert(i , 11)
                                    del block_id[i+1]
                                    last = 7
                                    color_last = 1
                                    state = 1
                                    break
                        elif state == 1:
                            for i in range(len(block_id)):
                                if block_id[i] == 0:
                                    block_id.insert(i , 14)
                                    del block_id[i+1]
                                    last = 7
                                    color_last = 2
                                    state = 2
                                    break
                        elif state == 2:
                            for i in range(len(block_id)):
                                if block_id[i] == 0:
                                    block_id.insert(i , 17)
                                    del block_id[i+1]
                                    last = 7
                                    color_last = 3
                                    state = 0
                                    trying = 5
                                    break
                    elif trying == 4:
                        if state == 0:
                            for i in range(len(block_id)):
                                if block_id[i] == 0:
                                    block_id.insert(i , 12)
                                    del block_id[i+1]
                                    last = 7
                                    color_last = 1
                                    state = 1
                                    break
                        elif state == 1:
                            for i in range(len(block_id)):
                                if block_id[i] == 0:
                                    block_id.insert(i , 15)
                                    del block_id[i+1]
                                    last = 7
                                    color_last = 2
                                    state = 2
                                    break
                        elif state == 2:
                            for i in range(len(block_id)):
                                if block_id[i] == 0:
                                    block_id.insert(i , 18)
                                    del block_id[i+1]
                                    last = 7
                                    color_last = 3
                                    state = 0
                                    trying = 5
                                    break
                    else:
                        trying += 1

                    waiting = (26*sfr)/speed

                if trying > -1:
                    waiting -= fps*dt
                else:
                    waiting = (26*sfr)/speed

                for i in range(len(block_id)): # Déplaceur de bloc
                    if block_id[i] > 0:
                        a = block_mov.get(f"block{i}")
                        a += -1000 * dt * speed
                        block_mov[f"block{i}"] = a
                        if a < -301:
                            block_id.insert(i , 0)
                            del block_id[i+1]
                            block_mov[f"block{i}"] = 1920

                block_collide1 = 0
                block_collide2 = 0
                block_collide3 = 0
                block_collideall = "none"
            for i in range(len(block_id)): #l'afficheur de block
                if block_id[i] > 0:
                    if block_id[i] < 7:
                        if block_id[i] == 1:
                            window_surface.blit(block, res_pos(block_mov.get(f"block{i}"),30))
                            if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                                block_collide1 = 1
                        elif block_id[i] == 2:
                            window_surface.blit(block, res_pos(block_mov.get(f"block{i}"),390))
                            if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                                block_collide2 = 1
                        elif block_id[i] == 3:
                            window_surface.blit(block, res_pos(block_mov.get(f"block{i}"),750))
                            if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                                block_collide3 = 1
                        elif block_id[i] == 4:
                            window_surface.blit(block, res_pos(block_mov.get(f"block{i}"),30))
                            window_surface.blit(block, res_pos(block_mov.get(f"block{i}"),750))
                            if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                                block_collide1 = 1
                                block_collide3 = 1
                        elif block_id[i] == 5:
                            window_surface.blit(block, res_pos(block_mov.get(f"block{i}"),30))
                            window_surface.blit(block, res_pos(block_mov.get(f"block{i}"),390))
                            if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                                block_collide1 = 1
                                block_collide2 = 1
                        elif block_id[i] == 6:
                            window_surface.blit(block, res_pos(block_mov.get(f"block{i}"),390))
                            window_surface.blit(block, res_pos(block_mov.get(f"block{i}"),750))
                            if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                                block_collide2 = 1
                                block_collide3 = 1
                    if block_id[i] > 6 and block_id[i] < 10:
                        if block_id[i] == 7:
                            window_surface.blit(big_block_red, res_pos(block_mov.get(f"block{i}"),30))
                            if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                                block_collideall = "red"
                        elif block_id[i] == 8:
                            window_surface.blit(big_block_blue, res_pos(block_mov.get(f"block{i}"),30))
                            if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                                block_collideall = "blue"
                        elif block_id[i] == 9:
                            window_surface.blit(big_block_yellow, res_pos(block_mov.get(f"block{i}"),30))
                            if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                                block_collideall = "yellow"
                    if block_id[i] > 9 and block_id[i] < 13:
                        window_surface.blit(block, res_pos(block_mov.get(f"block{i}"),390))
                        window_surface.blit(block, res_pos(block_mov.get(f"block{i}"),750))
                        if block_id[i] == 10:
                            window_surface.blit(demi_block, res_pos(block_mov.get(f"block{i}"),30))
                            if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                                block_collide1 = 2
                                block_collide2 = 1
                                block_collide3 = 1
                        elif block_id[i] == 11:
                            window_surface.blit(demi_block, res_pos(block_mov.get(f"block{i}"),180))
                            if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                                block_collide1 = 3
                                block_collide2 = 1
                                block_collide3 = 1
                        elif block_id[i] == 12:
                            window_surface.blit(break_block, res_pos(block_mov.get(f"block{i}"),30))
                            if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                                block_collide1 = 4
                                block_collide2 = 1
                                block_collide3 = 1
                                if position_of_player == 3:
                                    block_id.insert(i, 6)
                                    del block_id[i+1]
                    if block_id[i] > 12 and block_id[i] < 16:
                        window_surface.blit(block, res_pos(block_mov.get(f"block{i}"),30))
                        window_surface.blit(block, res_pos(block_mov.get(f"block{i}"),750))
                        if block_id[i] == 13:
                            window_surface.blit(demi_block, res_pos(block_mov.get(f"block{i}"),390))
                            if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                                block_collide1 = 1
                                block_collide2 = 2
                                block_collide3 = 1
                        elif block_id[i] == 14:
                            window_surface.blit(demi_block, res_pos(block_mov.get(f"block{i}"),540))
                            if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                                block_collide1 = 1
                                block_collide2 = 3
                                block_collide3 = 1
                        elif block_id[i] == 15:
                            window_surface.blit(break_block, res_pos(block_mov.get(f"block{i}"),390))
                            if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                                block_collide1 = 1
                                block_collide2 = 4
                                block_collide3 = 1
                                if position_of_player == 3:
                                    block_id.insert(i, 4)
                                    del block_id[i+1]
                    if block_id[i] > 15:
                        window_surface.blit(block, res_pos(block_mov.get(f"block{i}"),30))
                        window_surface.blit(block, res_pos(block_mov.get(f"block{i}"),390))
                        if block_id[i] == 16:
                            window_surface.blit(demi_block, res_pos(block_mov.get(f"block{i}"),750))
                            if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                                block_collide1 = 1
                                block_collide2 = 1
                                block_collide3 = 2
                        elif block_id[i] == 17:
                            window_surface.blit(demi_block, res_pos(block_mov.get(f"block{i}"),900))
                            if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                                block_collide1 = 1
                                block_collide2 = 1
                                block_collide3 = 3
                        elif block_id[i] == 18:
                            window_surface.blit(break_block, res_pos(block_mov.get(f"block{i}"),750))
                            if res_posx(10) <= block_mov.get(f"block{i}") and block_mov.get(f"block{i}") <= (res_posx(200)+ (65*(1920/res[0]))):
                                block_collide1 = 1
                                block_collide2 = 1
                                block_collide3 = 4
                                if position_of_player == 3:
                                    block_id.insert(i, 5)
                                    del block_id[i+1]

            if PAUSE < 2:
                if (2*sfr)+1 > frame > 0: #Animation du personnage quand il court
                    if color == "red":
                        if position_of_player == 1:
                            window_surface.blit(slide1r, [res_posx(200), player_pos_y])
                        elif position_of_player == 3:
                            window_surface.blit(kick1r, [res_posx(200), player_pos_y+res_posy(-35)])
                        elif position_of_player == 2:
                            window_surface.blit(jump1r, [res_posx(200), player_pos_y+res_posy(-55)])
                        elif position_of_player == 0:
                            window_surface.blit(runner1r, [res_posx(200), player_pos_y])
                    elif color == "blue":
                        if position_of_player == 1:
                            window_surface.blit(slide1b, [res_posx(200), player_pos_y])
                        elif position_of_player == 3:
                            window_surface.blit(kick1b, [res_posx(200), player_pos_y+res_posy(-35)])
                        elif position_of_player == 2:
                            window_surface.blit(jump1b, [res_posx(200), player_pos_y+res_posy(-55)])
                        elif position_of_player == 0:
                            window_surface.blit(runner1b, [res_posx(200), player_pos_y])
                    elif color == "yellow":
                        if position_of_player == 1:
                            window_surface.blit(slide1y, [res_posx(200), player_pos_y])
                        elif position_of_player == 3:
                            window_surface.blit(kick1y, [res_posx(200), player_pos_y+res_posy(-35)])
                        elif position_of_player == 2:
                            window_surface.blit(jump1y, [res_posx(200), player_pos_y+res_posy(-55)])
                        elif position_of_player == 0:
                            window_surface.blit(runner1y, [res_posx(200), player_pos_y])
                if (4*sfr)+1 > frame > (2*sfr):
                    if color == "red":
                        if position_of_player == 1:
                            window_surface.blit(slide2r, [res_posx(200), player_pos_y])
                        elif position_of_player == 3:
                            window_surface.blit(kick2r, [res_posx(200), player_pos_y+res_posy(-35)])
                        elif position_of_player == 2:
                            window_surface.blit(jump2r, [res_posx(200), player_pos_y+res_posy(-55)])
                        elif position_of_player == 0:
                            window_surface.blit(runner2r, [res_posx(200), player_pos_y])
                    elif color == "blue":
                        if position_of_player == 1:
                            window_surface.blit(slide2b, [res_posx(200), player_pos_y])
                        elif position_of_player == 3:
                            window_surface.blit(kick2b, [res_posx(200), player_pos_y+res_posy(-35)])
                        elif position_of_player == 2:
                            window_surface.blit(jump2b, [res_posx(200), player_pos_y+res_posy(-55)])
                        elif position_of_player == 0:
                            window_surface.blit(runner2b, [res_posx(200), player_pos_y])
                    elif color == "yellow":
                        if position_of_player == 1:
                            window_surface.blit(slide2y, [res_posx(200), player_pos_y])
                        elif position_of_player == 3:
                            window_surface.blit(kick2y, [res_posx(200), player_pos_y+res_posy(-35)])
                        elif position_of_player == 2:
                            window_surface.blit(jump2y, [res_posx(200), player_pos_y+res_posy(-55)])
                        elif position_of_player == 0:
                            window_surface.blit(runner2y, [res_posx(200), player_pos_y])
                if (6*sfr)+1 > frame > (4*sfr):
                    if color == "red":
                        if position_of_player == 1:
                            window_surface.blit(slide3r, [res_posx(200), player_pos_y])
                        elif position_of_player == 3:
                            window_surface.blit(kick3r, [res_posx(200), player_pos_y+res_posy(-35)])
                        elif position_of_player == 2:
                            window_surface.blit(jump3r, [res_posx(200), player_pos_y+res_posy(-55)])
                        elif position_of_player == 0:
                            window_surface.blit(runner3r, [res_posx(200), player_pos_y])
                    elif color == "blue":
                        if position_of_player == 1:
                            window_surface.blit(slide3b, [res_posx(200), player_pos_y])
                        elif position_of_player == 3:
                            window_surface.blit(kick3b, [res_posx(200), player_pos_y+res_posy(-35)])
                        elif position_of_player == 2:
                            window_surface.blit(jump3b, [res_posx(200), player_pos_y+res_posy(-55)])
                        elif position_of_player == 0:
                            window_surface.blit(runner3b, [res_posx(200), player_pos_y])
                    elif color == "yellow":
                        if position_of_player == 1:
                            window_surface.blit(slide3y, [res_posx(200), player_pos_y])
                        elif position_of_player == 3:
                            window_surface.blit(kick3y, [res_posx(200), player_pos_y+res_posy(-35)])
                        elif position_of_player == 2:
                            window_surface.blit(jump3y, [res_posx(200), player_pos_y+res_posy(-55)])
                        elif position_of_player == 0:
                            window_surface.blit(runner3y, [res_posx(200), player_pos_y])
                if (8*sfr)+1 > frame > (6*sfr):
                    if color == "red":
                        if position_of_player == 1:
                            window_surface.blit(slide4r, [res_posx(200), player_pos_y])
                        elif position_of_player == 3:
                            window_surface.blit(kick4r, [res_posx(200), player_pos_y+res_posy(-35)])
                        elif position_of_player == 2:
                            window_surface.blit(jump4r, [res_posx(200), player_pos_y+res_posy(-55)])
                        elif position_of_player == 0:
                            window_surface.blit(runner4r, [res_posx(200), player_pos_y])
                    elif color == "blue":
                        if position_of_player == 1:
                            window_surface.blit(slide4b, [res_posx(200), player_pos_y])
                        elif position_of_player == 3:
                            window_surface.blit(kick4b, [res_posx(200), player_pos_y+res_posy(-35)])
                        elif position_of_player == 2:
                            window_surface.blit(jump4b, [res_posx(200), player_pos_y+res_posy(-55)])
                        elif position_of_player == 0:
                            window_surface.blit(runner4b, [res_posx(200), player_pos_y])
                    elif color == "yellow":
                        if position_of_player == 1:
                            window_surface.blit(slide4y, [res_posx(200), player_pos_y])
                        elif position_of_player == 3:
                            window_surface.blit(kick4y, [res_posx(200), player_pos_y+res_posy(-35)])
                        elif position_of_player == 2:
                            window_surface.blit(jump4y, [res_posx(200), player_pos_y+res_posy(-55)])
                        elif position_of_player == 0:
                            window_surface.blit(runner4y, [res_posx(200), player_pos_y])
                if PAUSE < 1:
                    frame += 1
                if frame == (8*sfr)+1:
                    frame = 1


            if PAUSE < 1:

                if block_collide1 == 1 and player_pos == 2 or block_collide2 == 1 and player_pos == 1 or block_collide3 == 1 and player_pos == 0 or block_collideall != "none" and block_collideall != color or block_collide1 == 2 and player_pos == 2 and position_of_player != 1 or block_collide2 == 2 and player_pos == 1 and position_of_player != 1 or block_collide3 == 2 and player_pos == 0 and position_of_player != 1 or block_collide1 == 3 and player_pos == 2 and position_of_player != 2 or block_collide2 == 3 and player_pos == 1 and position_of_player != 2 or block_collide3 == 3 and player_pos == 0 and position_of_player != 2 or block_collide1 == 4 and player_pos == 2 and position_of_player != 3 or block_collide2 == 4 and player_pos == 1 and position_of_player != 3 or block_collide3 == 4 and player_pos == 0 and position_of_player != 3:
                    state = 0
                    block_mov = {"block0" : 1920 , "block1" : 1920 ,"block2" : 1920 ,"block3" : 1920 ,"block4" : 1920 ,"block5" : 1920 ,"block6" : 1920 ,"block7" : 1920 ,"block8" : 1920 ,"block9" : 1920 ,"block10" : 1920 ,"block11" : 1920}
                    block_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    waiting = (26*sfr)
                    block_collide1 = False
                    block_collide2 = False
                    block_collide3 = False
                    block_collideall = "none"
                    trying = last_trying

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or input_controller[12] == True and no_input == True or input_controller[12] and pause_input == True: #Activer la pause
                    PAUSE = 1
                    menu1_joystick_select = 0
                    no_input = False
                    pause_input = False

                if trying == 8:
                    if explain_text == 0:
                        PAUSE = 2
                        menu1_joystick_select = 2
                    else:
                        trying = -1
                
                if trying < 0:
                    window_surface.blit(tuto_help_text, res_pos(1300,1030))
                    if trying == -100:
                        if explain_text == 0:
                            tutorial_text(language.tuto_rep1(langue))
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and nokey_input == True or input_controller[6] == True and no_input == True or pressed[0] and mouse_click_left == False:
                                explain_text = 1
                        elif explain_text == 1:
                            tutorial_text(language.tuto_rep2(langue))
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and nokey_input == True or input_controller[6] == True and no_input == True or pressed[0] and mouse_click_left == False:
                                explain_text = 2
                        elif explain_text == 2:
                            tutorial_text(language.tuto_rep3(langue))
                            if controller_on != 10000:
                                tutorial_text2(language.tuto_rep3b(langue))
                            else:
                                tutorial_text2(language.tuto_rep3c(langue))
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and nokey_input == True or input_controller[6] == True and no_input == True or pressed[0] and mouse_click_left == False:
                                explain_text = 10
                                trying = 0
                                last_trying = 0
                    elif explain_text == 10 or explain_text == 11:
                        if explain_text == 10:
                            tutorial_text(language.tuto_rep4(langue))
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and nokey_input == True or input_controller[6] == True and no_input == True or pressed[0] and mouse_click_left == False:
                                explain_text = 11
                        elif explain_text == 11:
                            tutorial_text(language.tuto_rep5(langue))
                            if controller_on != 10000:
                                tutorial_text2(language.tuto_rep5b(langue))
                            else:
                                tutorial_text2(language.tuto_rep5c(langue))
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and nokey_input == True or input_controller[6] == True and no_input == True or pressed[0] and mouse_click_left == False:
                                explain_text = 20
                                trying = 1
                                last_trying = 1
                    elif explain_text == 20 or explain_text == 21:
                        if explain_text == 20:
                            tutorial_text(language.tuto_rep6(langue))
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and nokey_input == True or input_controller[6] == True and no_input == True or pressed[0] and mouse_click_left == False:
                                explain_text = 21
                        elif explain_text == 21:
                            tutorial_text(language.tuto_rep7(langue))
                            if controller_on != 10000:
                                tutorial_text2(language.tuto_rep7b(langue))
                            else:
                                tutorial_text2(language.tuto_rep7c(langue))
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and nokey_input == True or input_controller[6] == True and no_input == True or pressed[0] and mouse_click_left == False:
                                explain_text = 30
                                trying = 2
                                last_trying = 2
                    elif explain_text == 30 or explain_text == 31:
                        if explain_text == 30:
                            tutorial_text(language.tuto_rep8(langue))
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and nokey_input == True or input_controller[6] == True and no_input == True or pressed[0] and mouse_click_left == False:
                                explain_text = 31
                        elif explain_text == 31:
                            tutorial_text(language.tuto_rep9(langue))
                            if controller_on != 10000:
                                tutorial_text2(language.tuto_rep9b(langue))
                            else:
                                tutorial_text2(language.tuto_rep9c(langue))
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and nokey_input == True or input_controller[6] == True and no_input == True or pressed[0] and mouse_click_left == False:
                                explain_text = 40
                                trying = 3
                                last_trying = 3
                    elif explain_text == 40 or explain_text == 41:
                        if explain_text == 40:
                            tutorial_text(language.tuto_rep10(langue))
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and nokey_input == True or input_controller[6] == True and no_input == True or pressed[0] and mouse_click_left == False:
                                explain_text = 41
                        elif explain_text == 41:
                            tutorial_text(language.tuto_rep11(langue))
                            if controller_on != 10000:
                                tutorial_text2(language.tuto_rep11b(langue))
                            else:
                                tutorial_text2(language.tuto_rep11c(langue))
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and nokey_input == True or input_controller[6] == True and no_input == True or pressed[0] and mouse_click_left == False:
                                explain_text = 0
                                trying = 4
                                last_trying = 4
            
            
            if PAUSE == 1: # PAUSE --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- PAUSE
                window_surface.blit(pause_square, res_pos(320,180))
                pygame.draw.rect(window_surface, black, rect_form)

                if controller_on > 2 and controller_on != 10000:
                    if menu1_joystick_select == 0:
                            controller_square_icon(1080,680,1370,770)
                            if d_pad_negligerh() == 0 and no_input == True or d_pad_negligerh() == 1 and no_input == True or stick1_negligerh() == 1 and no_input == True or stick1_negligerh() == 0 and no_input == True:
                                menu1_joystick_select = 1
                    elif menu1_joystick_select == 1:
                        controller_square_icon(480,680,770,770)
                        if d_pad_negligerh() == 1 and no_input == True or d_pad_negligerh() == 0 and no_input == True or stick1_negligerh() == 1 and no_input == True or stick1_negligerh() == 0 and no_input == True:
                            menu1_joystick_select = 0

                if collision_square(res_pos(500,700), text_main_menu) or input_controller[6] and no_input == True and menu1_joystick_select == 1:
                    menu = 0
                    PAUSE = 0
                elif collision_square(res_pos(1100,700), text_resume) or input_controller[6] and no_input == True and menu1_joystick_select == 0 or input_controller[12] and no_input == True or input_controller[12] == True and pause_input == True:
                    PAUSE = 0
                    pause_input = False


            if PAUSE == 2: # FIN DE TUTO --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- FIN DE TUTO
                pygame.draw.rect(window_surface, black, rect_form)

                window_surface.blit(pause_square, res_pos(320,180))
                window_surface.blit(text_finish, res_pos(400,250))

                if controller_on > 2 and controller_on != 10000:
                    if menu1_joystick_select == 2:
                        controller_square_icon(1080,680,1370,770)
                        if d_pad_negligerh() == 1 and no_input == True or stick1_negligerh() == 1 and no_input == True:
                            menu1_joystick_select = 4
                        elif d_pad_negligerh() == 0 and no_input == True or stick1_negligerh() == 0 and no_input == True:
                            menu1_joystick_select = 4
                    elif menu1_joystick_select == 4:
                        controller_square_icon(480,680,770,770)
                        if d_pad_negligerh() == 1 and no_input == True or stick1_negligerh() == 1 and no_input == True:
                            menu1_joystick_select = 2
                        elif d_pad_negligerh() == 0 and no_input == True or stick1_negligerh() == 0 and no_input == True:
                            menu1_joystick_select = 2
                
                if collision_square(res_pos(500,700), text_main_menu) or input_controller[6] and no_input == True and menu1_joystick_select == 4:
                    menu = 0
                    PAUSE = 0
                    did = False
                elif collision_square(res_pos(1100,700), play_text) or input_controller[6] and no_input == True and menu1_joystick_select == 2:
                    PAUSE = 0
                    menu = 1
                    menu_loaded = 0
                    did = False

            if pressed[0] == 1:
                mouse_click_left = True
            else:
                mouse_click_left = False

            if input_controller[12] == False:
                pause_input = True
            else:
                pause_input = False
        
        if input_controller == [(0, 0), 0, 0, 0, 0, False, False, False, False, False, False, False, False, False, False, 0]:
            no_input = True
        else:
            no_input = False

        if controller_on != 0: # CONTROLLER --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- CONTROLLER
            if controller_on == 1 or controller_on == -1:
                pygame.joystick.init()
                if pygame.joystick.get_count() > 0:
                    mon_joystick1 = pygame.joystick.Joystick(0)
                    mon_joystick1.init()
                if controller_on == 1:
                    controller_on = 2
                elif controller_on == -1:
                    controller_on = -2
                else:
                    controller_on = 0
                input_controller = [(0, 0), 0, 0, 0, 0, False, False, False, False, False, False, False, False, False, False, 0]
            elif controller_on == 3:
                input_controller = controller_outpout()
            elif controller_on == 2:
                window_surface.blit(controller_square, res_pos(40,40))
                window_surface.blit(croix, res_pos(1810,100))
                croix_rect_controller = croix.get_rect(topleft=res_pos(1810,100))
                if croix_rect_controller.collidepoint(x,y) == 1:
                    window_surface.blit(croix_light, res_pos(1810,100))
                    if pressed[0]:
                        controller_on = 0
                else:
                    window_surface.blit(croix, res_pos(1810,100))
                    controller_on = 2
                window_surface.blit(controller_detected, res_pos(350,70))
                window_surface.blit(use_controller, res_pos(550,350))
                menu0_joystick_select = 0
                menu1_joystick_select = 0
                menu2_joystick_select = 0
                menu3_joystick_select = 0
                no_button_rect = no_button.get_rect(topleft=res_pos(1200,600))
                yes_button_rect = yes_button.get_rect(topleft=res_pos(550,600))
                window_surface.blit(yes_button, res_pos(550,600))
                window_surface.blit(no_button, res_pos(1200,600))
                window_surface.blit(yes_text, res_pos(590,615))
                window_surface.blit(no_text, res_pos(1230,615))
                if pressed[0] and yes_button_rect.collidepoint(x,y) == 1 and mouse_click_left == False:
                    controller_on = 3
                    mouse_click_left = True
                elif pressed[0] and no_button_rect.collidepoint(x,y) == 1 and mouse_click_left == False:
                    controller_on = 0
                    mouse_click_left = True
            elif controller_on == -2:
                pygame.joystick.quit()
                pygame.joystick.init()
                if pygame.joystick.get_count() > 0:
                    mon_joystick1 = pygame.joystick.Joystick(0)
                    mon_joystick1.init()
                    controller_on = 3
                    input_controller = [(0, 0), 0, 0, 0, 0, False, False, False, False, False, False, False, False, False, False, 0]
                else:
                    window_surface.blit(controller_square, res_pos(40,40))
                    window_surface.blit(croix, res_pos(1810,100))
                    croix_rect_controller = croix.get_rect(topleft=res_pos(1810,100))
                    window_surface.blit(text_searching_controller, res_pos(250,450))
                    if croix_rect_controller.collidepoint(x,y) == 1:
                        window_surface.blit(croix_light, res_pos(1810,100))
                        if pressed[0]:
                            controller_on = 0

        if show_fps == True:
            update_fps()
        
        if event.type == pygame.KEYUP:
            nokey_input = True
        elif event.type == pygame.KEYDOWN:
            nokey_input = False

        pygame.display.flip()
        dt = clock.tick(fps)/1000