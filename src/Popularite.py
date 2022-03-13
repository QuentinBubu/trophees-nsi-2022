from jauge import *

#Popularité hérite de Jauge

class Popularite(Jauge):

    def __init__(self, popularite: int = 10) -> None:
        super().__init__()
        self.popularite = 10 


    def set_pop(self, v:int) -> int :
        """setter popularite

        Args:
            v (int): popularite voulue

        Returns:
            int: popularite
        """
        self.popularite = v
        return self.popularite

    def get_pop(self):
        """getter popularité"""
        return self.popularite

    def add_pop(self, v:int) -> int : 
        """ajoute de la popularite    

        Args:
            v (int): valeur qui va être ajoutée

        Returns:
            int: popularité
        """        
        if type(v) == int :
            self.popularite = self.popularite + v
            return self.popularite
