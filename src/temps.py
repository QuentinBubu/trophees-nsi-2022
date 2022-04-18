from src.utils.Date import Date

class Temps:
    LIMITE = 120
    actuel = Date.get_date()
    date_ig = "00/00"
    ajout = 0

    def __init__(self) -> None:
        self.add_tps(0)

    def add_tps(self, ajouter:int) -> bool:
        self.ajout += ajouter
        self.date_ig = Date.mois_ig_txt(self.ajout)
        return False if not self.verification() else True

    def verification(self) -> bool:
        if self.ajout >= self.LIMITE:
            return False
        return True

    def get_date(self) -> str:
        return self.date_ig

    def __str__(self) -> str:
        return self.date_ig

    def __repr__(self) -> str:
        return self.date_ig
