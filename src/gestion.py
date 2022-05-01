import pygame
from random import choice
from src.popularite import Popularite
from src.gestionJauges import GestionJauges
from src.listeEvenement import ListeEvenement
from src.utils.constante import CITOYEN, MAIRE, DEPUTE, DEPUTE_REGIONAL, MINISTRE, PRESIDENT, PRESIDENT_DES_NATIONS

class Gestion:
    """Gestion globale des grades, evenements et jauges

        nom (str) : nom de la classe
        liste_evenements (ListeEvenement) : liste des evenements
        jauges(GestionJauges) : jauges
        grade(str) : grade
        attente_reponse(bool) : attente d'une réponse du joueur (oui ou non)
        fond(bool) : ______________
        img_corr(dict): Prend le fond correspondant au bon grade
    """

    nom = ""
    liste_evenements = ListeEvenement(CITOYEN)
    jauges = GestionJauges()
    grade = CITOYEN
    attente_reponse = False
    fond = False
    
    img_corr = {
        CITOYEN        : 'citoyen',
        MAIRE          : 'maire',
        DEPUTE         : 'depute',
        DEPUTE_REGIONAL: 'depRegion',
        MINISTRE       : 'ministre',
        PRESIDENT      : 'president'
    }
    
    music_list = [
        'MonplaisirS1L24.mp3',
        'The_Bards_Tale.mp3',
        'Monplaisir_-_06_-_Juillet.mp3',
        'Monplaisir_-_01_-_Hlice.mp3',
        'Komiku_-_01_-_Balance.mp3',
        'Brendan_Kinsella_-_01_-_Bach_-_Aria_Variata_BWV_989_Variation_no1.mp3'
    ]
    
    MUSIC_END = pygame.USEREVENT+1

#######################GETTER ET SETTER##############################

    def set_nom(self, nom:str) -> None:
        self.nom = nom

    def get_nom(self) -> str:
        return self.nom
    
    def set_grade(self, grade):
        self.grade = grade

    def get_grade(self) -> str:
        return self.grade

    def get_event(self) -> None:
        return self.liste_evenements.faire_choix(self.grade)
    
    def set_event(self, choix, event):
        return self.jauges.jauges(choix, event, self)

    def set_attente_reponse(self, reponse:bool):
        self.attente_reponse = reponse

    def get_attente_reponse(self) -> bool:
        return self.attente_reponse

    def set_fond(self, screen):
        self.fond = f"image/{self.img_corr[self.grade]}.jpg"
        screen.set_fond(self.fond)

    def get_fond(self):
        return self.fond

###########################################################################

    def retour_true(self):
        return 'oui'
    def retour_false(self):
        return 'non'

    def max_grade(self):
        """Renvoie le nombre d'ahdérants à atteindre pour passer au grade
        suivant pour chaque grade

        return : max (int)

        """
        if self.get_grade() == CITOYEN :
            return 20000
        if self.get_grade() == MAIRE :
            return 300000
        if self.get_grade() == DEPUTE :
            return 5000000
        if self.get_grade() == DEPUTE_REGIONAL :
            return 40000000
        if self.get_grade() == MINISTRE :
            return 250000000
        if self.get_grade() == PRESIDENT :
            return 4000000000
        if self.get_grade() == PRESIDENT_DES_NATIONS :
            return Popularite.get_pop()

    def play_music(self):
        rChoix = choice(self.music_list)
        pygame.mixer.music.set_endevent(self.MUSIC_END)
        pygame.mixer.music.load(__file__[:-14] + '/sound/' + rChoix)
        pygame.mixer.music.play()
        self.music = 1
    
    def stop_music(self):
        pygame.mixer.music.stop()
        self.music = 0
        
    def get_music_status(self) -> bool:
        return self.music