from random import randint
from constante import *
from popularite import *
from justice import *
from legalite import *

class Jauge:

    def __init__(self) -> None :
        """fonction init"""

    def lien_justice_legalite(self):
        """Cette fonction fait le lien entre la jauge de justice et de legalité
        plus on est dans l'illégalité, plus on a de chance d'être detécté par la justice et aller en prison"""
        legal = Legalite.get_leg()
        if legal < 50 :             
            Justice.add_jus(randint(2, legal-48)//4)    #Si le joueur a un pourcentage de légalité inférieur à 50, à chaques tour la jauge "justice" augmente petit à petit
        if legal > 50 :                             #Si le joueur a un pourcentage de légalité supérieur à 50, son pourcentage de chance d'être détécté par la justice est mis à 10
            Justice.set_jus(10)

    def chance_de_detection(self):
        """Fonction qui gère la propabilité d'être detécté par la justice
        NB : si la jauge justice est à 50%, cela ne veut pas dire que vous avez 1 chance / 2 d'être detécté(e), c'est un indiquateur qui plus il est élevé a de chance de vous envoyer en procès et d'aller en prison"""
        just = Justice.get_jus()
        if just >= 50 :                             #si la jauge de détéction par la justice passe au dessus de 50% :
            if randint((just*0.1),10)== 10 :        #le joueur à selon son pourcentage entre 1 chance sur 10 d'être détécté ou 1 chance sur 2.
                return Gestion.fin_jeu(2)           #fin du jeu
        if just < 50 :
            Justice.add_jus(-1)

    def grade(self):
        """Gestion des grades"""
        pop = Popularite.get_pop()
        if pop >= 20000 and pop < 300000:                              #minimum 20000 de popularité pour atteindre le grade maire.
            Liste_evenement.set_grade = MAIRE
        if pop >= 300000 and pop < 5000000 :
            Liste_evenement.set_grade = DEPUTE
        if pop >= 5000000 and pop < 40000000 :
            Liste_evenement.set_grade = DEPUTE_REGIONAL
        if pop >= 40000000 and pop < 250000000 :
            Liste_evenement.set_grade = MINISTRE
        if pop >= 250000000 and pop < 4000000000 :
            Liste_evenement.set_grade = PRESIDENT
        if pop >= 4000000000 :                                          #arrivé au grace maximal, président des nations, fin du jeu.
            Liste_evenement.set_grade = PRESIDENT_DES_NATIONS
            return Gestion.fin_jeu(1)
