from src.gestionJauges import GestionJauges
from src.listeEvenement import ListeEvenement
from src.utils.constante import CITOYEN, MAIRE, DEPUTE, DEPUTE_REGIONAL, MINISTRE, PRESIDENT

class Gestion:

    nom = ""
    liste_evenements = ListeEvenement(CITOYEN)
    jauges = GestionJauges()
    run = True
    grade = CITOYEN
    attente_reponse = False
    
    img_corr = {
        CITOYEN        : 'citoyen',
        MAIRE          : 'maire',
        DEPUTE         : 'depute',
        DEPUTE_REGIONAL: 'depRegion',
        MINISTRE       : 'ministre',
        PRESIDENT      : 'president'
    }

    def set_nom(self, nom:str) -> None:
        self.nom = nom

    def get_nom(self) -> str:
        return self.nom
    
    def set_grade(self, grade):
        self.grade = grade

    def get_grade(self) -> str:
        return self.grade

    def get_event(self) -> None:
        return self.liste_evenements.faire_choix(self.grade)
    
    def set_event(self, choix, event) -> None:
        self.jauges.jauges(choix, event, self)

    def set_attente_reponse(self, reponse:bool):
        self.attente_reponse = reponse

    def get_attente_reponse(self) -> bool:
        return self.attente_reponse

    def set_fond(self, screen):
        screen.set_fond(f"image/{self.img_corr[self.grade]}.jpg")

    def retour_true(self):
        return 'oui'
    def retour_false(self):
        return 'non'