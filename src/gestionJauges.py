from src.justice import Justice
from src.popularite import Popularite
from src.legalite import Legalite
from src.temps import Temps

# à tester avec les variables correspondantes
class GestionJauges:

    def __init__(self) -> None:
        #recupération de la classe liste_evenement et jauges

        self.popularite = Popularite()   #popularité.get_pop()
        self.legalite = Legalite() #legalite.get_legalite()
        self.temps = Temps()  #temps.get_temps()
        self.justice = Justice()
        
    def jauges(self, choix) -> bool:
        """
        Cette fonction permet de gérer les jauges popularité, legalité
        et temps avec les informations de la liste_evenement.
        """
        if choix == False or choix['accepter'] == 'stop':
            return False
        if not self.popularite.add_pop(choix['event'][choix['accepter']]['pop']):
            return False
        if not self.legalite.add_leg(choix['event'][choix['accepter']]['legalite']):
            return False
        if not self.temps.add_tps(choix['event'][choix['accepter']]['temps']):
            return False
        if not self.justice.lien_justice_legalite(self.legalite):
            return False
        self.popularite.grade(self.gestion)
        return True
