from random import randint
from src.utils.constante import FIN_PRISON

#Justice hérite de Jauge

class Justice:

    def __init__(self, justice: float = 0) -> None:
        """Jauge de la justice

        Args:
            justice (float, optionel): pourcentage de chance d'être détécté comme malhonnête aux yeux de la justice. Par défaut 0.
        """
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

    def get_jus(self) -> int:
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

    def chance_de_detection(self, legal):
        """Fonction qui gère la propabilité d'être detécté par la justice
        NB : si la jauge justice est à 50%, cela ne veut pas dire que vous avez 1 chance / 2 d'être detécté(e), c'est un indiquateur qui plus il est élevé a de chance de vous envoyer en procès et d'aller en prison"""
        just = self.get_jus()
        if just >= 50 :                             #si la jauge de détéction par la justice passe au dessus de 50% :
            if randint(round(just/100, 0)*10, 10)==10 :           #le joueur à selon son pourcentage une chance plus ou moins forte de se faire détécter.
                return True                                   #fin du jeu
        if legal < 50 :
            self.add_jus(-5)

    def lien_justice_legalite(self, legalite:object) -> bool:
        """Cette fonction fait le lien entre la jauge de justice et de legalité
        plus on est dans l'illégalité, plus on a de chance d'être detécté par la justice et aller en prison"""
        legal = legalite.get_leg()
        if self.chance_de_detection(legal) :
            return False
        if legal < 50 :             
            self.add_jus(randint(2, 52-legal))         #Si le joueur a un pourcentage de légalité inférieur à 50, à chaques tour la jauge "justice" augmente petit à petit
        if legal > 50 :                                #Si le joueur a un pourcentage de légalité supérieur à 50, son pourcentage de chance d'être détécté par la justice est mis à 10
            self.set_jus(10)
        return True
