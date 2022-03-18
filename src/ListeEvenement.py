# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
from random import choice

    

class ListeEvenement:
    dict_maire = {
     "event1":{
            "titre":"patrimoine",
            "oui":{
                    "pop":700,"legalite":50, "temps":1
            },
            "non":{
                    "pop":100,"legalite":50, "temps":1
            }
    },
    "event2":{
            "titre":"papier",
            "oui":{
                    "pop":250,"legalite":50, "temps":1
            },
            "non":{
                    "pop":50,"legalite":50, "temps":1
            }
    },
    "event3":{
            "titre":"salon",
            "oui":{
                    "pop":450,"legalite":50, "temps":1
            },
            "non":{
                    "pop":100,"legalite":50, "temps":1
            }
    },
    "event4":{
            "titre":"poubelle",
            "oui":{
                    "pop":250,"legalite":50, "temps":1
            },
            "non":{
                    "pop":100,"legalite":50, "temps":1
            }
    },
    "event5":{
            "titre":"degradation",
            "oui":{
                    "pop":500,"legalite":50, "temps":1
            },
            "non":{
                    "pop":50,"legalite":50, "temps":1
            }
    },
    "event6":{
            "titre":"argent",
            "oui":{
                    "pop":400,"legalite":50, "temps":1
            },
            "non":{
                    "pop":300,"legalite":50, "temps":1
            }
    },
    "event7":{
            "titre":"election",
            "oui":{
                    "pop":450,"legalite":50, "temps":4
            },
            "non":{
                    "pop":50,"legalite":50, "temps":1
            }
    },
    }
            
            
            
    dict_deputer = {
     "event1":{
            "titre":"loi",
            "oui":{
                    "pop":30000,"legalite":50, "temps":1
            },
            "non":{
                    "pop":4000,"legalite":50, "temps":1
            }
    },
    "event2":{
            "titre":"arret",
            "oui":{
                    "pop":30000,"legalite":50, "temps":1
            },
            "non":{
                    "pop":3000,"legalite":50, "temps":1
            }
    },
    "event3":{
            "titre":"proces",
            "oui":{
                    "pop":3000,"legalite":50, "temps":1
            },
            "non":{
                    "pop":600,"legalite":50, "temps":1
            }
    },
    "event4":{
            "titre":"maltraitance",
            "oui":{
                    "pop":250000,"legalite":50, "temps":1
            },
            "non":{
                    "pop":500,"legalite":50, "temps":1
            }
    },
    "event5":{
            "titre":"ecole",
            "oui":{
                    "pop":7000,"legalite":50, "temps":1
            },
            "non":{
                    "pop":3000,"legalite":50, "temps":1
            }
    },
    "event6":{
            "titre":"budjet",
            "oui":{
                    "pop":4000,"legalite":50, "temps":1
            },
            "non":{
                    "pop":5000,"legalite":50, "temps":1
            }
    },
    "event7":{
            "titre":"parite",
            "oui":{
                    "pop":170000,"legalite":50, "temps":1
            },
            "non":{
                    "pop":600,"legalite":50, "temps":1
            }
    },
    }
            
            
    dict_depregion = {
     "event1":{
            "titre":"confiner",
            "oui":{
                    "pop":350500,"legalite":50, "temps":1
            },
            "non":{
                    "pop":671428,"legalite":50, "temps":1
            }
    },
    "event2":{
            "titre":"plastique",
            "oui":{
                    "pop":350000,"legalite":50, "temps":1
            },
            "non":{
                    "pop":671428,"legalite":50, "temps":1
            }
    },
    "event3":{
            "titre":"musee",
            "oui":{
                    "pop":671428,"legalite":50, "temps":1
            },
            "non":{
                    "pop":450500,"legalite":50, "temps":1
            }
    },
    "event4":{
            "titre":"travail",
            "oui":{
                    "pop":750000,"legalite":50, "temps":1
            },
            "non":{
                    "pop":671428,"legalite":50, "temps":1
            }
    },
    "event5":{
            "titre":"argent",
            "oui":{
                    "pop":671428,"legalite":50, "temps":1
            },
            "non":{
                    "pop":950700,"legalite":50, "temps":1
            }
    },
    "event6":{
            "titre":"animaux",
            "oui":{
                    "pop":4700400,"legalite":50, "temps":4
            },
            "non":{
                    "pop":671408,"legalite":50, "temps":1
            }
    },
    "event7":{
            "titre":"jeune",
            "oui":{
                    "pop":450050,"legalite":50, "temps":1
            },
            "non":{
                    "pop":671428,"legalite":50, "temps":1
            }
    },
    }
            
            
    dict_ministre = {
     "event1":{
            "titre":"egalite",
            "oui":{
                    "pop":17654854,"legalite":50, "temps":4
            },
            "non":{
                    "pop":5000000,"legalite":50, "temps":1
            }
    },
    "event2":{
            "titre":"vacances",
            "oui":{
                    "pop":5000000,"legalite":50, "temps":1
            },
            "non":{
                    "pop":4945945,"legalite":50, "temps":1
            }
    },
    "event3":{
            "titre":"villa",
            "oui":{
                    "pop":5000000,"legalite":50, "temps":1
            },
            "non":{
                    "pop":4845945,"legalite":50, "temps":1
            }
    },
    "event4":{
            "titre":"detenus",
            "oui":{
                    "pop":5000000,"legalite":50, "temps":1
            },
            "non":{
                    "pop":7400500,"legalite":50, "temps":1
            }
    },
    "event5":{
            "titre":"avortement",
            "oui":{
                    "pop":5000000,"legalite":50, "temps":1
            },
            "non":{
                    "pop":15748965,"legalite":50, "temps":1
            }
    },
    "event6":{
            "titre":"victimes",
            "oui":{
                    "pop":13999000,"legalite":50, "temps":1
            },
            "non":{
                    "pop":5000000,"legalite":50, "temps":1
            }
    },
    "event7":{
            "titre":"reforme",
            "oui":{
                    "pop":2645713,"legalite":50, "temps":1
            },
            "non":{
                    "pop":5000000,"legalite":50, "temps":1
            }
    },
    }
    
    
    dict_president = {
     "event1":{
            "titre":"peine",
            "oui":{
                    "pop":300000000,"legalite":50, "temps":1
            },
            "non":{
                    "pop":160475284,"legalite":50, "temps":1
            }
    },
    "event2":{
            "titre":"attaque",
            "oui":{
                    "pop":300000000,"legalite":50, "temps":1
            },
            "non":{
                    "pop":100010200,"legalite":50, "temps":1
            }
    },
    "event3":{
            "titre":"routes",
            "oui":{
                    "pop":30000000,"legalite":50, "temps":1
            },
            "non":{
                    "pop":87676450,"legalite":50, "temps":1
            }
    },
    "event4":{
            "titre":"frontiere",
            "oui":{
                    "pop":30000000,"legalite":50, "temps":1
            },
            "non":{
                    "pop":98550050,"legalite":50, "temps":1
            }
    },
    "event5":{
            "titre":"vaccin",
            "oui":{
                    "pop":158309206,"legalite":50, "temps":4
            },
            "non":{
                    "pop":30000000,"legalite":50, "temps":1
            }
    },
    "event6":{
            "titre":"purge",
            "oui":{
                    "pop":30000000,"legalite":50, "temps":1
            },
            "non":{
                    "pop":76467889,"legalite":50, "temps":1
            }
    },
    "event7":{
            "titre":"retraite",
            "oui":{
                    "pop":30000000,"legalite":50, "temps":1
            },
            "non":{
                    "pop":66467889,"legalite":50, "temps":1
            }
    },
    }
            
    
    dict_presidentnation = {
     "event1":{
            "titre":"marcial",
            "oui":{
                    "pop":3964285714,"legalite":50, "temps":1
            },
            "non":{
                    "pop":98555674,"legalite":50, "temps":1
            }
    },
    "event2":{
            "titre":"invasion",
            "oui":{
                    "pop":2596846754,"legalite":50,"temps":4
            },
            "non":{
                    "pop":3964285714,"legalite":50, "temps":1
            }
    },
    "event3":{
            "titre":"autre",
            "oui":{
                    "pop":3964285714,"legalite":50, "temps":1
            },
            "non":{
                    "pop":44846754,"legalite":50, "temps":1
            }
    },
    "event4":{
            "titre":"virus",
            "oui":{
                    "pop":3964285714,"legalite":50, "temps":1
            },
            "non":{
                    "pop":61942304,"legalite":50, "temps":1
            }
    },
    "event5":{
            "titre":"survivant",
            "oui":{
                    "pop":3964285714,"legalite":50, "temps":1
            },
            "non":{
                    "pop":44850250,"legalite":50,"temps":1
            }
    },
    "event6":{
            "titre":"espace",
            "oui":{
                    "pop":13467864,"legalite":50, "temps":1
            },
            "non":{
                    "pop":3964285714,"legalite":50,"temps":1
            }
    },
    "event7":{
            "titre":"bombe",
            "oui":{
                    "pop":3964285714,"legalite":50, "temps":1
            },
            "non":{
                    "pop":3457864,"legalite":50, "temps":1
            }
    },
    }
    
    def __init__(self,grade,event):
        self.grade=grade
        self.event=event
        
    def maire(self,event):
        event=choice(list(self.dict_maire.items()))
        self.afficher(event)
        
    def deputer(self,event):
        event=choice(list(self.dict_deputer.items()))
        self.afficher(event)
        
    def deputerregion(self,event):
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
l=liste_evenement("maire",0)
l.maire(0)
