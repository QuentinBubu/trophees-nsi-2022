from random import randint
from jauge import *
from legalite import *

#Justice hérite de Jauge

class Justice(Jauge):

    def __init__(self, justice: float = 0) -> None:
        super().__init__()
        self.justice = 0

    def set_jus(self, v:int) -> int :
        """setter justice
        Args:
            v (int): pourcentage de jusitce voulue
        Returns:
            int: justice
        """
        self.justice = v
        return self.justice

    def get_jus(self):
        """getter justice"""
        return self.justice

    def add_jus(self, v:int):
        """ ajoute de la justice
        Args:
            v (int): valeur qui va être ajoutée 
        Returns:
            int : justice
        """
        self.justice = self.justice + v
        if self.justice > 100 :             #pour ne pas que la justice soit au dessus de 100%
            self.justice = 100
        if self.justice < 0 :               #et pas en dessous de 0%
            self.justice = 0
        else :
            return self.justice

    def chance_de_detection(self):
        """Fonction qui gère la propabilité d'être detécté par la justice
        NB : si la jauge justice est à 50%, cela ne veut pas dire que vous avez 1 chance / 2 d'être detécté(e), c'est un indiquateur qui plus il est élevé a de chance de vous envoyer en procès et d'aller en prison"""
        just = self.get_jus()
        if just >= 50 :                             #si la jauge de détéction par la justice passe au dessus de 50% :
            if randint((just*0.1),20)== 20 :        #le joueur à selon son pourcentage entre 1 chance sur 20 d'être détécté ou 1 chance sur 4.
                return Gestion.fin_jeu(2)           #fin du jeu
        if just < 50 :
            self.add_jus(-1)

    def lien_justice_legalite(self):
        """Cette fonction fait le lien entre la jauge de justice et de legalité
        plus on est dans l'illégalité, plus on a de chance d'être detécté par la justice et aller en prison"""
        legal = Legalite.get_leg()
        if legal < 50 :             
            self.add_jus(randint(2, legal-48)//4)    #Si le joueur a un pourcentage de légalité inférieur à 50, à chaques tour la jauge "justice" augmente petit à petit
        if legal > 50 :                              #Si le joueur a un pourcentage de légalité supérieur à 50, son pourcentage de chance d'être détécté par la justice est mis à 10
            self.set_jus(10)
