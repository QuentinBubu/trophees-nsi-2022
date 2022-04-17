from src.gestionJauges import GestionJauges

class Gestion:

    nom = ""
    jauges = GestionJauges()
    run = True

    def set_nom(self, nom:str) -> None:
        self.nom = nom

    def get_nom(self) -> str:
        return self.nom

    def appel_evenement(self, screen) -> bool:
        return self.jauges.jauges(screen)

    def lancement(self, screen) -> None:
        self.run = True
        while self.run:
            retour = self.appel_evenement(screen)
            if not retour:
                self.run = False
