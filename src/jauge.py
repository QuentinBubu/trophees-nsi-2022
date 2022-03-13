from random import *
from constante import *

class Jauge:

    def __init__(self) -> None :
        """fonction init"""

    def lien_justice_legalite(self):
        """Cette fonction fait le lien entre la jauge de justice et de legalité
        plus on est dans l'illégalité, plus on a de chance d'être detécté par la justice et aller en prison"""
        legal = Legalite.get_leg()
        if legal < 50 :             
            Justice.add_jus(randint(2, legal-48)//4)    #Si le joueur a un pourcentage de légalité inférieur à 50, à chaques tour la jauge "justice" augmente petit à petit
        if legal > 50 :                             #Si le joueur a un pourcentage de légalité supérieur à 50, son pourcentage de chance d'être détécté par la justice est mis à 10
            Justice.set_jus(10)

    def chance_de_detection(self):
        """Fonction qui gère la propabilité d'être detécté par la justice
        NB : si la jauge justice est à 50%, cela ne veut pas dire que vous avez 1 chance / 2 d'être detécté(e), c'est un indiquateur qui plus il est élevé a de chance de vous envoyer en procès et d'aller en prison"""
        just = Justice.get_jus()
        if just >= 50 :                             #si la jauge de détéction par la justice passe au dessus de 50% :
            if randint((just*0.1),10)== 10 :        #le joueur à selon son pourcentage entre 1 chance sur 10 d'être détécté ou 1 chance sur 2.
                return Gestion.fin_jeu(2)           #fin du jeu
        if just < 50 :
            Justice.add_jus(-1)

    def grade(self):
        """Gestion des grades"""
        pop = Popularite.get_pop()
        if pop >= 20000 and pop < 300000:                              #minimum 20000 de popularité pour atteindre le grade maire.
            Liste_evenement.set_grade = MAIRE
        if pop >= 300000 and pop < 5000000 :
            Liste_evenement.set_grade = DEPUTE
        if pop >= 5000000 and pop < 40000000 :
            Liste_evenement.set_grade = DEPUTE_REGIONAL
        if pop >= 40000000 and pop < 250000000 :
            Liste_evenement.set_grade = MINISTRE
        if pop >= 250000000 and pop < 4000000000 :
            Liste_evenement.set_grade = PRESIDENT
        if pop >= 4000000000 :                                          #arrivé au grace maximal, président des nations, fin du jeu.
            Liste_evenement.set_grade = PRESIDENT_DES_NATIONS
            return Gestion.fin_jeu(1)


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

#Legalite qui hérite de Jauge

class Legalite(Jauge):

    def __init__(self, legalite : float = 100) -> None:
        super().__init__()

    def set_leg(self, v:int) -> int :
        """setter legalité

        Args:
            v (int): légalité voulue

        Returns:
            int: légalité
        """
        self.legalite = v
        return self.legalite

    def get_leg(self):
        """getter legalite"""
        return self.legalite

    def add_leg(self, v):
        """ajoute de la légalité

        Args:
            v (int): valeur ajoutée

        Returns:
            int : legalité
        """
        self.legalite = self.legalite + v
        if self.legalite > 100 :             #pour ne pas que la legalite soit au dessus de 100%        
            self.legalite = 100
        if self.legalite < 0 :               #et pas en dessous de 0%
            self.legalite = 0
        else :
            return self.legalite