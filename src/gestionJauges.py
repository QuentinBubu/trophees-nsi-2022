from src.listeEvenement import ListeEvenement
from justice import Justice
from popularite import Popularite
from legalite import Legalite
from temps import Temps

# à tester avec les variables correspondantes
class GestionJauges:

    liste_evenements = ListeEvenement()

    def __init__(self):
        #recupération de la classe liste_evenement et jauges

        self.popularite = Popularite()   #popularité.get_pop()
        self.legalite = Legalite() #legalite.get_legalite()
        self.temps = Temps()  #temps.get_temps()
        self.justice = Justice()
        
    def jauges(self):
        """
        Cette fonction permet de gérer les jauges popularité, legalité
        et temps avec les informations de la liste_evenement.
        """

        choix = self.liste_evenements.faire_choix()
        self.popularite.add_jus(choix['event'][choix['accepter']]['pop'])
        self.legalite.add_jus(choix['event'][choix['accepter']]['legalite'])
        self.temps.add_jus(choix['event'][choix['accepter']]['temps'])
        self.justice.lien_justice_legalite(self.legalite)
