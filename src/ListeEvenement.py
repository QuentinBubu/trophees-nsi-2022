from json import load
from random import choice

class ListeEvenement:

    dict_maire           = {}
    dict_depute          = {}
    dict_depregion       = {}
    dict_ministre        = {}
    dict_president       = {}
    dict_presidentnation = {}
    
    def __init__(self, grade, event):
        with open('src/utils/events/maire.json')           as f: self.dict_maire           = load(f)
        with open('src/utils/events/depute.json')          as f: self.dict_depute          = load(f)
        with open('src/utils/events/depRegion.json')       as f: self.dict_depregion       = load(f)
        with open('src/utils/events/ministre.json')        as f: self.dict_ministre        = load(f)
        with open('src/utils/events/president.json')       as f: self.dict_president       = load(f)
        with open('src/utils/events/presidentNation.json') as f: self.dict_presidentnation = load(f)

        self.grade=grade
        self.event=event
        
    def maire(self,event):
        event=choice(list(self.dict_maire.items()))
        self.afficher(event)
        
    def depute(self,event):
        event=choice(list(self.dict_depute.items()))
        self.afficher(event)

    def depregion(self,event):
        event=choice(list(self.dict_depregion.items()))
        self.afficher(event)

    def ministre(self,event):
        event=choice(list(self.dict_ministre.items()))
        self.afficher(event)
        
    def president(self,event):
        event=choice(list(self.dict_president.items()))
        self.afficher(event)
        
    def presidentnation(self,event):
        event=choice(list(self.dict_presidentnation.items()))
        self.afficher(event)
        
    def afficher(self,event):
        print (event)
        m=int(input(event[1]["titre"]))
