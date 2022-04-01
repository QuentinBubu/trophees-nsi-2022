from json import load
from random import choice

from urllib3 import Retry
from src.utils.constante import CITOYEN, FIN_DICT_VIDE, MAIRE, DEPUTE, DEPUTE_REGIONAL, MINISTRE, PRESIDENT, PRESIDENT_DES_NATIONS
from src.utils.affichage import Affichage

class ListeEvenement:

    grade = CITOYEN
    dict_citoyen         = {}
    dict_maire           = {}
    dict_depute          = {}
    dict_depregion       = {}
    dict_ministre        = {}
    dict_president       = {}
    dict_presidentnation = {}
    
    def __init__(self, grade):
        with open('src/utils/events/citoyen.json')         as f: self.dict_citoyen         = load(f)
        with open('src/utils/events/maire.json')           as f: self.dict_maire           = load(f)
        with open('src/utils/events/depute.json')          as f: self.dict_depute          = load(f)
        with open('src/utils/events/depRegion.json')       as f: self.dict_depregion       = load(f)
        with open('src/utils/events/ministre.json')        as f: self.dict_ministre        = load(f)
        with open('src/utils/events/president.json')       as f: self.dict_president       = load(f)
        with open('src/utils/events/presidentNation.json') as f: self.dict_presidentnation = load(f)
        self.grade = grade

    def get_grade(self) -> str:
        return self.grade

    def set_grade(self, grade):
        self.grade = grade

    def citoyen(self):
        if len(self.dict_citoyen) == 0:
            Affichage.fin_jeu(FIN_DICT_VIDE)
            return False
        event = choice(list(self.dict_citoyen.items()))
        del self.dict_citoyen[event[0]]
        return self.afficher(event)

    def maire(self):
        if len(self.dict_maire) == 0:
            Affichage.fin_jeu(FIN_DICT_VIDE)
            return False
        event = choice(list(self.dict_maire.items()))
        del self.dict_maire[event[0]]
        return self.afficher(event)
        
    def depute(self):
        if len(self.dict_depute) == 0:
            Affichage.fin_jeu(FIN_DICT_VIDE)
            return False
        event = choice(list(self.dict_depute.items()))
        del self.dict_depute[event[0]]
        return self.afficher(event)

    def depregion(self):
        if len(self.dict_depregion) == 0:
            Affichage.fin_jeu(FIN_DICT_VIDE)
            return False
        event = choice(list(self.dict_depregion.items()))
        del self.depregion[event[0]]
        return self.afficher(event)

    def ministre(self):
        if len(self.dict_ministre) == 0:
            Affichage.fin_jeu(FIN_DICT_VIDE)
            return False
        event = choice(list(self.dict_ministre.items()))
        del self.dict_ministre[event[0]]
        return self.afficher(event)
        
    def president(self):
        if len(self.dict_president) == 0:
            Affichage.fin_jeu(FIN_DICT_VIDE)
            return False
        event = choice(list(self.dict_president.items()))
        del self.dict_president[event[0]]
        return self.afficher(event)
        
    def presidentnation(self):
        if len(self.dict_presidentnation) == 0:
            Affichage.fin_jeu(FIN_DICT_VIDE)
            return False
        event = choice(list(self.dict_presidentnation.items()))
        del self.dict_presidentnation[event[0]]
        return self.afficher(event)

    def faire_choix(self):
        if self.grade == CITOYEN:
            return self.citoyen()
        elif self.grade == MAIRE:
            return self.maire()
        elif self.grade == DEPUTE:
            return self.depute()
        elif self.grade == DEPUTE_REGIONAL:
            return self.depregion()
        elif self.grade == MINISTRE:
            return self.ministre()
        elif self.grade == PRESIDENT:
            return self.president()
        elif self.grade == PRESIDENT_DES_NATIONS:
            return self.presidentnation()
        else:
            Affichage.erreur('Grade inconnu')
        
    def afficher(self,event):
        print(event)
        choix = input("Accepter?")
        return {'accepter':choix, 'event':event[1]}
