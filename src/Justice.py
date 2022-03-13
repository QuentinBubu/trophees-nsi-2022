from jauge import *

#Justice hérite de Jauge

class Justice(Jauge):

    def __init__(self, justice: float = 0) -> None:
        super().__init__()

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
