from src.gestionJauges import GestionJauges

class Gestion:

    nom = ""
    jauges = GestionJauges()
    run = True

    def set_nom(self, nom:str) -> None:
        self.nom = nom

    def get_nom(self) -> str:
        return self.nom

    def lancement(self, screen) -> None:
        return self.jauges.jauges(screen)
