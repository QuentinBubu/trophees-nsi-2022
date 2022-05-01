from json import load
from random import choice

from src.utils.constante import CITOYEN, FIN_DICT_VIDE, MAIRE, DEPUTE, DEPUTE_REGIONAL, MINISTRE, PRESIDENT

class ListeEvenement:
    """Liste de tous les évènements du jeu

    Arguments : 
    dict_citoyen (dict) : évènements concernant le grade citoyen
    dict_maire (dict) : évènements concernant le grade maire
    dict_depute (dict) : évènements concernant le grade député
    dict_depregion (dict) : évènements concernant le grade député régional
    dict_ministre (dict) : évènements concernant le grade ministre
    dict_president (dict) : évènements concernant le grade president
    """
    dict_citoyen         = {}
    dict_maire           = {}
    dict_depute          = {}
    dict_depregion       = {}
    dict_ministre        = {}
    dict_president       = {}
    
    def __init__(self, grade):                     #Importation des fichiers json pour les dictionnaires des évènements
        with open('src/utils/events/citoyen.json',         encoding='utf-8') as f: self.dict_citoyen         = load(f)
        with open('src/utils/events/maire.json',           encoding='utf-8') as f: self.dict_maire           = load(f)
        with open('src/utils/events/depute.json',          encoding='utf-8') as f: self.dict_depute          = load(f)
        with open('src/utils/events/depRegion.json',       encoding='utf-8') as f: self.dict_depregion       = load(f)
        with open('src/utils/events/ministre.json',        encoding='utf-8') as f: self.dict_ministre        = load(f)
        with open('src/utils/events/president.json',       encoding='utf-8') as f: self.dict_president       = load(f)
        self.grade = grade

##########################GETTER ET SETTER###########################

    def get_grade(self) -> str:
        return self.grade

    def set_grade(self, grade):
        self.grade = grade

#########################################################################


#############################Fonctions renvoyant un évènement relatif à chaque grade###################################### 
    def citoyen(self):
        if len(self.dict_citoyen) == 0:
            return False, FIN_DICT_VIDE
        event = choice(list(self.dict_citoyen.items()))
        del self.dict_citoyen[event[0]]
        return event

    def maire(self):
        if len(self.dict_maire) == 0:
            return False, FIN_DICT_VIDE
        event = choice(list(self.dict_maire.items()))
        del self.dict_maire[event[0]]
        return event
        
    def depute(self):
        if len(self.dict_depute) == 0:
            return False, FIN_DICT_VIDE
        event = choice(list(self.dict_depute.items()))
        del self.dict_depute[event[0]]
        return event

    def depregion(self):
        if len(self.dict_depregion) == 0:
            return False, FIN_DICT_VIDE
        event = choice(list(self.dict_depregion.items()))
        del self.dict_depregion[event[0]]
        return event

    def ministre(self):
        if len(self.dict_ministre) == 0:
            return False, FIN_DICT_VIDE
        event = choice(list(self.dict_ministre.items()))
        del self.dict_ministre[event[0]]
        return event
        
    def president(self):
        if len(self.dict_president) == 0:
            return False, FIN_DICT_VIDE
        event = choice(list(self.dict_president.items()))
        del self.dict_president[event[0]]
        return event

##########################################################################################

    def faire_choix(self, grade):
        """Choisi un évènement pour le bon grade

        Args:
            grade (str): grade

        Returns:
            bool + str: si le grade est inconnu (erreur)
        """
        if grade == CITOYEN:
            event = self.citoyen()
        elif grade == MAIRE:
            event = self.maire()
        elif grade == DEPUTE:
            event = self.depute()
        elif grade == DEPUTE_REGIONAL:
            event = self.depregion()
        elif grade == MINISTRE:
            event = self.ministre()
        elif grade == PRESIDENT:
            event = self.president()
        else:
            return False, 'Grade inconnu'
        return event
