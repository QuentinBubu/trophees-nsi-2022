from src.ListeEvenement import ListeEvenement
# à tester avec les variables correspondantes
class GestionJauges:

    liste_evenements = ListeEvenement("grade ??") # Mais honnetement, mieux vaut faire des attributs propres a l'objet que à la classe

    def __init__(self, jauges, event): # t'aurais pas oublié les arguments pop, legalite, temps ?
        #recupération de la classe liste_evenement et jauges
        
        self.event = event   #liste_evenement.get_event()
        self.pop = "pop"   #popularité.get_pop()
        self.legalite = "legalite" #legalite.get_legalite()
        self.temps = "temps"  #temps.get_temps()

    def jauges(self, event, pop, legalite, justice):
        """
        Cette fonction permet de gérer les jauges popularité, legalité
        et temps avec les informations de la liste_evenement.
        """
    
        self.event["event"]["oui"]["pop"].append(get_pop())
        self.event["event"]["oui"]["legalite"].append(get_leg())
        self.event["event"]["oui"]["temps"].append(get_temps())
        
        self.event["event"]["non"]["pop"].append(get_pop())
        self.event["event"]["non"]["legalite"].append(get_leg())
        self.event["event"]["non"]["temps"].append(get_temps())
        
