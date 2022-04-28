from src.utils.Date import Date

class Temps:
    """Classe pour gérer et afficher le temps, la date

        Arguments : 
        LIMITE (int) : Nombre de mois limite
        actuel (Date) : date actuelle
        date_ig (str) : date dans le jeu
        ajout (int) : __________________
    """
    LIMITE = 120
    actuel = Date.get_date()
    date_ig = "00/00"
    ajout = 0

    def __init__(self) -> None:
        self.add_tps(0)

    def add_tps(self, ajouter:int) -> bool:
        """Ajoute du temps

        Args:
            ajouter (int): valeur à ajouter

        Returns:
            bool: couple mois,année
        """
        self.ajout += ajouter
        self.date_ig = Date.mois_ig_txt(self.ajout)
        return False if not self.verification() else True

    def verification(self) -> bool:
        """Vérifie que le temps qu'on veut ajouter est correct (>0)

        Returns:
            bool: True si ok, False sinon
        """
        if self.ajout >= self.LIMITE:
            return False
        return True

    def get_date(self) -> str:
        """getter date

        Returns:
            str: date
        """
        return self.date_ig

    def __str__(self) -> str:
        return self.date_ig

    def __repr__(self) -> str:
        return self.date_ig
