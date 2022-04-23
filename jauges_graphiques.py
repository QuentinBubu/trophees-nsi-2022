"""

Des jauges graphiques du type :

    ---------------------
    |######             |
    ---------------------
     Population

"""

import pygame
from src.screen import *
import pygameSettings


class Jauges_graphique:
    def __init__(self, description, pos, size, pourcentage = 0.0, show_pourcentage=True) : 
        """Créée une jauge graphique

        Args:
            description (string): le nom de la jauge (genre pop)
            pos (tuple : int): la position
            size (tuple : int): la taille
            pourcentage (float, optional): le pourcentage de remplissage de la jauge (entre 0 et 1). Defaults to 0.
        """
        self.description = description
        self.pos = pos
        self.size = size
        self.pourcentage = pourcentage
        
        self._show_pourcentage = show_pourcentage

        self.font = pygame.font.SysFont('Candara', 16)
        self.target = pourcentage

#################GETTER ET SETTER#################################

    def set_descritpion(self, n):
        self.description = n

    def set_pos(self, n):
        self.pos = n
    
    def set_size(self, n):
        self.size = n

    def set_pourcentage(self, n):
        self.pourcentage = n

    def set_target(self, n):
        self.target = n

    def set_show_pourcentage(self, n):
        self.set_show_pourcentage = n

    def _get_middle_size(self):
        length = (self.size[0]-4)*self.pourcentage
        return (length, self.size[1]-4)

    def _get_middle_pos(self):
        return (self.pos[0]+2, self.pos[1]+2)

######################################################################

    def remplissage(self, current, max):
        """Remplissage de la jauge (en pourcents)

        Args:
            current (float): pourcentage de remplissage
            max (int): remplissage max
        """
        self.pourcentage = current/max

    def draw(self, screen : Screen):
        """Dessine/Créé la jauge

        Args:
            screen (Screen): fenêtre d'affichage
        """
        plain = pygame.surface.Surface(self._get_middle_size())
        plain.fill("grey")
        
        contour = pygame.surface.Surface(self.size)
        contour.fill("black")

        if self.set_show_pourcentage:
            """Affichage du pourcentage sur l'écran
            """
            text = self.font.render(self.description+" "+str(int(self.pourcentage*100))+"%", False, "black")
        else :
            text = self.font.render(self.description, False, "black")

        screen.screen.blit(contour, self.pos)
        screen.screen.blit(plain, self._get_middle_pos())
        screen.screen.blit(text, (self.pos[0], self.pos[1]+self.size[1]))

    def actualiser(self, screen:Screen):
        """Actualisation de la jauge

        Args:
            screen (Screen): fenêtre d'affichage
        """
        self.pourcentage = round(self.pourcentage, 2) # on ne veux pas de pourcentage avec trop de virgules
        if self.target < self.pourcentage:
            self.pourcentage -= 0.01
        elif self.target > self.pourcentage:
            self.pourcentage += 0.01

        self.draw(screen)