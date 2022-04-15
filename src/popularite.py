from src.utils.constante import MAIRE, DEPUTE, DEPUTE_REGIONAL, MINISTRE, PRESIDENT, PRESIDENT_DES_NATIONS
from src.jauge import Jauge
from src.utils.affichage import Affichage

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
        else:
            return False
        if v + self.get_pop() < 0 :
            self.popularite = 0
        return True

    def grade(self, listeEvenement):
        """Gestion des grades"""
        pop = self.get_pop()
        if pop >= 20000 and pop < 300000:
            print(listeEvenement.grade) #minimum 20000 de popularité pour atteindre le grade maire.
            listeEvenement.set_grade(MAIRE)
        if pop >= 300000 and pop < 5000000 :
            listeEvenement.set_grade(DEPUTE)
        if pop >= 5000000 and pop < 40000000 :
            listeEvenement.set_grade(DEPUTE_REGIONAL)
        if pop >= 40000000 and pop < 250000000 :
            listeEvenement.set_grade(MINISTRE)
        if pop >= 250000000 and pop < 4000000000 :
            listeEvenement.set_grade(PRESIDENT)
        if pop >= 4000000000 :                                          #arrivé au grace maximal, président des nations, fin du jeu.
            listeEvenement.set_grade(PRESIDENT_DES_NATIONS)
            Affichage.fin_jeu(0)
            return False
