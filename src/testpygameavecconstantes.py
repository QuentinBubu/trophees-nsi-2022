# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 11:35:08 2022

@author: leopold.demarco
"""

import pygame 

pygame.init()

screen = pygame.display.set_mode((1300 ,900), pygame.RESIZABLE)

ouvert = True

n = 1

while ouvert: 
    fond = pygame.image.load('image/imagepygame.jpg').convert_alpha()
    screen.blit(fond, (0,0))
    pygame.draw.rect(screen , (236, 16, 16), (560 ,30 ,n ,20), 0) #A la place de 2*30 -> Legalite.get_leg() 
    pygame.draw.rect(screen , (16, 119, 236), (560 ,100 ,n ,20), 0) #A la place de 270 -> Justice.get_jus()    
    pygame.draw.rect(screen , (247, 232, 18), (560 ,170 , 7000/(20000/100) ,20), 0) #A la place de 5000/(20000/100) -> Population.get_pop()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP :
            ouvert = False
        if event.type == pygame.KEYUP :
            n += 1

        if event.type == pygame.MOUSEBUTTONUP and mouse[0] >= 30*long/100 and mouse[0] <= 37.5*long/100 and mouse[1] >= 82*larg/100 and mouse[1] <= 95*larg/100  :
            print("True")

        if event.type == pygame.MOUSEBUTTONUP and mouse[0] >= 67*long/100 and mouse[0] <= 87*long/100 and mouse[1] >= 82*larg/100 and mouse[1] <= 95*larg/100  :
            print("False")
pygame.quit()