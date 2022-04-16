"""
Créé par Anton Appel, le 16/04/2022

Une simple classe de boutons
"""

from hashlib import new
import pygame


class Bouton:
    def __init__(self, pos, size, texture_path, texture_path_clicked, func=None):
        """Un bouton interractible

        Args:
            pos (tuple(int)): la position
            size (tuple(int)): la taille du bouton
            texture_path (string): la texture du bouton
            texture_path_clicked (string): la texture du bouton quand il est cliqué
            func (function): la fonction à executer si le bouton est cliqué
        """
        self.pos = pos
        self.size = size
        self.texture = pygame.image.load(texture_path)
        self.texture = pygame.transform.scale(self.texture, self.size) 
        self.texture_clicked = pygame.image.load(texture_path_clicked)
        self.texture_clicked = pygame.transform.scale(self.texture_clicked, self.size)

        self.function = func

        self.clicked = False

    def set_size(self, new_size):
        self.size = new_size

    def set_pos(self, new_pos):
        self.pos = new_pos

    def set_texture(self, new_t):
        self.texture = pygame.image.load(new_t)
        self.texture = pygame.transform.scale(self.texture, self.size) 

    def set_texture_clicked(self, new_tc):
        self.texture_clicked = pygame.image.load(new_tc)
        self.texture_clicked = pygame.transform.scale(self.texture_clicked, self.size)

    def set_clicked(self, state):
        self.clicked = state

    def is_clicked(self):
        m_posX, m_posY = pygame.mouse.get_pos()
        if (self.pos[0] < m_posX < self.pos[0] + self.size[0]) and (self.pos[1] < m_posY < self.pos[1] + self.size[1]):
            return True
        return False

    def click(self):
        if self.function != None:
            self.function()

    def draw(self, window: pygame.surface.Surface):
        if self.clicked:
            window.screen.blit(self.texture_clicked, self.pos)
        else:
            window.screen.blit(self.texture, self.pos)

    def actualiser(self, window: pygame.surface.Surface):
        self.draw(window)