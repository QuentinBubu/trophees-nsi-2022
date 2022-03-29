from json import load
from random import choice
from src.utils.constante import MAIRE, DEPUTE, DEPUTE_REGIONAL, MINISTRE, PRESIDENT, PRESIDENT_DES_NATIONS
from gestion import Gestion

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

    def citoyen(self):
        event = choice(list(self.dict_citoyen.items()))
        del self.dict_citoyen[event]
        self.afficher(event)

    def maire(self):
        event = choice(list(self.dict_maire.items()))
        del self.dict_maire[event]
        self.afficher(event)
        
    def depute(self):
        event = choice(list(self.dict_depute.items()))
        del self.dict_depute[event]
        self.afficher(event)

    def depregion(self):
        event = choice(list(self.dict_depregion.items()))
        del self.depregion[event]
        self.afficher(event)

    def ministre(self):
        event = choice(list(self.dict_ministre.items()))
        del self.dict_ministre[event]
        self.afficher(event)
        
    def president(self):
        event = choice(list(self.dict_president.items()))
        del self.dict_president[event]
        self.afficher(event)
        
    def presidentnation(self):
        event = choice(list(self.dict_presidentnation.items()))
        del self.dict_presidentnation[event]
        self.afficher(event)

    def faire_choix(self):
        if self.grade == MAIRE:
            self.maire()
        elif self.grade == DEPUTE:
            self.depute()
        elif self.grade == DEPUTE_REGIONAL:
            self.depregion()
        elif self.grade == MINISTRE:
            self.ministre()
        elif self.grade == PRESIDENT:
            self.president()
        elif self.grade == PRESIDENT_DES_NATIONS:
            self.presidentnation()
        else:
            Gestion.erreur("Grade: inconnu")
        
    def afficher(self,event):
        print(event)
        choix = input("Accepter?")
        return {'accepter':choix, 'event':event}
