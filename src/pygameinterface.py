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
from pygameSettings import pourcentage

def refresh():
    """Cette partie du programme permet de faire les mise à jour du fond d'écran, des jauges 
    et les interactions avec les boutons "oui" ou "non"

    """
    pygame.init()           #initialisation pygame

    root = tkinter.Tk()                 #Variables pour prendre la taille de l'écran
    larg = root.winfo_screenwidth()
    long = root.winfo_screenheight()

    screen = pygame.display.set_mode((larg ,long), pygame.RESIZABLE)        #ouverture de la fenêtre

    ouvert = True                                                       

    while ouvert:
        mouse = pourcentage(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], screen)               #Donne la position de la souris sur l'écran en pourcentage par rapport à la largeur et hauteur de la fenêtre
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                ouvert = False

            if event.type == pygame.MOUSEBUTTONUP and mouse[0] >= 30*long/100 and mouse[0] <= 37.5*long/100 and mouse[1] >= 82*larg/100 and mouse[1] <= 95*larg/100  :      #Si le bouton oui est cliqué
                return True

            if event.type == pygame.MOUSEBUTTONUP and mouse[0] >= 67*long/100 and mouse[0] <= 87*long/100 and mouse[1] >= 82*larg/100 and mouse[1] <= 95*larg/100  :        #Si le bouton non est cliqué
                return False

        screen.blit(pygame.transform.scale(fond, (larg ,long)), (0, 0))         #Remet la fenêtre aux bonnes dimensions
        pygame.draw.rect(screen , (236, 16, 16), (60 ,140 ,legalite.get_leg()*4 ,20), 0) #Dessin jauge légalite
        pygame.draw.rect(screen , (16, 119, 236), (60 ,220 ,justice.get_jus()*4 ,20), 0) #Dessin jauge justice
        if listeEvenement.get_grade() == CITOYEN :
            pygame.draw.rect(screen , (247, 232, 18), (60 ,300 , popularite.get_pop()/(20000/100)*4 ,20), 0) #Dessin de la jauge qui montre la progression de la popularité pour atteindre le prochain grade
            fond = pygame.image.load('image/imagecitoyen.jpg').convert_alpha()
        if listeEvenement.get_grade() == MAIRE :
            pygame.draw.rect(screen , (247, 232, 18), (60 ,300 , popularite.get_pop()/(300000/100)*4 ,20), 0) #Dessin de la jauge qui montre la progression de la popularité pour atteindre le prochain grade
            fond = pygame.image.load('image/imagemaire.jpg').convert_alpha() 
        if listeEvenement.get_grade() == DEPUTE :
            pygame.draw.rect(screen , (247, 232, 18), (60 ,300 , popularite.get_pop()/(5000000/100)*4 ,20), 0) #Dessin de la jauge qui montre la progression de la popularité pour atteindre le prochain grade
            fond = pygame.image.load('image/imagedepute.jpg').convert_alpha() 
        if listeEvenement.get_grade() == DEPUTE_REGIONAL :
            pygame.draw.rect(screen , (247, 232, 18), (60 ,300 , popularite.get_pop()/(40000000/100)*4 ,20), 0) #Dessin de la jauge qui montre la progression de la popularité pour atteindre le prochain grade
            fond = pygame.image.load('image/imagedepute_regional.jpg').convert_alpha() 
        if listeEvenement.get_grade() == MINISTRE :
            pygame.draw.rect(screen , (247, 232, 18), (60 ,300 , popularite.get_pop()/(250000000/100)*4 ,20), 0) #Dessin de la jauge qui montre la progression de la popularité pour atteindre le prochain grade
            fond = pygame.image.load('image/imagepygameministre.jpg').convert_alpha() 
        if listeEvenement.get_grade() == PRESIDENT :
            pygame.draw.rect(screen , (247, 232, 18), (60 ,300 , popularite.get_pop()/(4000000000/100)*4 ,20), 0) #Dessin de la jauge qui montre la progression de la popularité pour atteindre le prochain grade
            fond = pygame.image.load('image/imagepresident.jpg').convert_alpha() 
        pygame.display.flip()       #Mises à jour d'écran
    pygame.quit()