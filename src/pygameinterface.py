# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 11:11:19 2022

@author: leopold.demarco
"""
from src.utils.constante import CITOYEN, MAIRE, DEPUTE, DEPUTE_REGIONAL, MINISTRE, PRESIDENT
import listeEvenement
import popularite
import legalite
import justice
import pygame 
import tkinter

pygame.init()

root = tkinter.Tk()
larg = root.winfo_screenwidth()
long = root.winfo_screenheight()

screen = pygame.display.set_mode((larg ,long), pygame.RESIZABLE)

ouvert = True

while ouvert: 
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP :
            ouvert = False
    screen.blit(pygame.transform.scale(fond, (larg ,long)), (0, 0))
    pygame.draw.rect(screen , (236, 16, 16), (60 ,140 ,Legalite.get_leg() ,30), 0) #A la place de 2*30 -> Legalite.get_leg() 
    pygame.draw.rect(screen , (16, 119, 236), (60 ,220 ,Justice.get_jus() ,30), 0) #A la place de 270 -> Justice.get_jus()
    if listeEvenement.get_grade() == CITOYEN :
        pygame.draw.rect(screen , (247, 232, 18), (60 ,300 , Popularite.get_pop()/(20000/100) ,30), 0) #A la place de 5000/(20000/100) -> Popularite.get_pop()
        fond = pygame.image.load('image/imagecitoyen.jpg').convert_alpha() 
    if listeEvenement.get_grade() == MAIRE :
        pygame.draw.rect(screen , (247, 232, 18), (60 ,300 , Popularite.get_pop()/(300000/100) ,30), 0) #A la place de 5000/(20000/100) -> Popularite.get_pop()
        fond = pygame.image.load('image/imagemaire.jpg').convert_alpha() 
    if listeEvenement.get_grade() == DEPUTE :
        pygame.draw.rect(screen , (247, 232, 18), (60 ,300 , Popularite.get_pop()/(5000000/100) ,30), 0) #A la place de 5000/(20000/100) -> Popularite.get_pop()
        fond = pygame.image.load('image/imagedepute.jpg').convert_alpha() 
    if listeEvenement.get_grade() == DEPUTE_REGIONAL :
        pygame.draw.rect(screen , (247, 232, 18), (60 ,300 , Popularite.get_pop()/(40000000/100) ,30), 0) #A la place de 5000/(20000/100) -> Popularite.get_pop()
        fond = pygame.image.load('image/imagedepute_regional.jpg').convert_alpha() 
    if listeEvenement.get_grade() == MINISTRE :
        pygame.draw.rect(screen , (247, 232, 18), (60 ,300 , Popularite.get_pop()/(250000000/100) ,30), 0) #A la place de 5000/(20000/100) -> Popularite.get_pop()
        fond = pygame.image.load('image/imagepygameministre.jpg').convert_alpha() 
    if listeEvenement.get_grade() == PRESIDENT :
        pygame.draw.rect(screen , (247, 232, 18), (60 ,300 , Popularite.get_pop()/(4000000000/100) ,30), 0) #A la place de 5000/(20000/100) -> Popularite.get_pop()
        fond = pygame.image.load('image/imagepresident.jpg').convert_alpha() 
    pygame.display.flip()
pygame.quit()