#Legalite qui hérite de Jauge

class Legalite:

    def __init__(self, legalite : float = 100) -> None:
        """Jauge de la Légalité

        Args:
            legalite (float, optionel): Fonctionne en pourcentage, niveau de votre légalité. Par défaut à 100.
        """
        super().__init__()
        self.legalite = 100

    def set_leg(self, v:int) -> int :
        """setter legalité

        Args:
            v (int): légalité voulue

        Returns:
            int: légalité
        """
        self.legalite = v
        return self.legalite

    def get_leg(self) -> int:
        """getter legalite"""
        return self.legalite

    def add_leg(self, v:int):
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
