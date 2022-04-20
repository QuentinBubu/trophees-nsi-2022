from json import load
from random import choice

from src.utils.constante import CITOYEN, FIN_DICT_VIDE, MAIRE, DEPUTE, DEPUTE_REGIONAL, MINISTRE, PRESIDENT, PRESIDENT_DES_NATIONS

class ListeEvenement:

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
        del self.depregion[event[0]]
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
        
    def presidentnation(self):
        if len(self.dict_presidentnation) == 0:
            return False, FIN_DICT_VIDE
        event = choice(list(self.dict_presidentnation.items()))
        del self.dict_presidentnation[event[0]]
        return event

    def faire_choix(self, grade):
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
        elif grade == PRESIDENT_DES_NATIONS:
            event = self.presidentnation()
        else:
            return False, 'Grade inconnu'
        return event
