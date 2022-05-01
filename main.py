"""Fichier principal du jeu
    Il faut run ce fichier pour lancer Head Of States
"""

from time import sleep
from jauges_graphiques import Jauges_graphique
from src.screen import Screen
from src.gestion import Gestion
from src.utils.texts import T_FIN_DICT_VIDE, T_FIN_GAGNE, T_FIN_PRISON, T_FIN_TEMPS, T_PROLOGUE
from src.utils.constante import FIN, FIN_DICT_VIDE, FIN_GAGNE, FIN_PRISON, FIN_TEMPS, GRADE, EVENT, DATE, NOIR, ROUGE, PRESIDENT, CITOYEN
from pygameSettings import *
from src.bouton import *

########################Définition variables globales################################

g = Gestion()
ouvert = True
arret = (False)
screen = Screen()
ecran = screen.WAITING

################Définition des jauges et boutons intéractibles########################
jauge_leg = Jauges_graphique("Legalite",(pourcentage(0.3 ,0.05 ,screen)),(150, 30))
jauge_jus = Jauges_graphique("Risque d'être détécté par la justice", (pourcentage(0.52, 0.05 , screen)),(150, 30))
jauge_pop = Jauges_graphique("Progression de la popularité pour le prochain grade", (pourcentage(0.74, 0.05, screen)),(150, 30))
jauge_leg.draw(screen)
jauge_jus.draw(screen)
jauge_pop.draw(screen)

interragibles = [
    Bouton(pourcentage(0.225, 0.79, screen), (120, 60), "image/oui.png", "image/oui_c.png", g.retour_true),
    Bouton(pourcentage(0.725, 0.8, screen), (120, 60), "image/non.png", "image/non_c.png", g.retour_false),
]

sound = [
    Bouton(pourcentage(0.95, 0.9, screen), (64, 64), "image/mute.png", "image/mute.png", g.play_music),
    Bouton(pourcentage(0.95, 0.9, screen), (64, 64), "image/sound.png", "image/sound.png", g.stop_music)
]

################################################################################

once = True


while ouvert:               #Boucle qui garde la fenêtre ouverte

    if once:            #Ecran de chargement
        once = False
        screen.set_fond('image/logo.png')
        pygame.display.flip()
        sleep(2) # temps de faux chargement
        screen.set_fond('image/temp_debut.jpg')
        ecran = screen.PROLOGUE
        g.play_music()
        sound[1].actualiser(screen)
        sound[0].set_pos(pourcentage(0.95, 0.9, screen))
        sound[1].set_pos(pourcentage(0.95, 0.9, screen))

    for event in pygame.event.get():                #Boucle qui va vérifier les actions du joueur (clique, clavier...)
        if event.type == pygame.QUIT:               #le joueur quitte le jeu
            ouvert = False
        if event.type == g.MUSIC_END:
            g.play_music()
        if event.type == pygame.VIDEORESIZE:        #Le joueur redimensionne la fenêtre, donc il faut tout remettre à la bonne taille
            screen.remove_on_screen(screen.PROLOGUE)
            screen.remove_on_screen(EVENT)
            screen.remove_on_screen(GRADE)
            screen.remove_on_screen(FIN)
            screen.set_screen(pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE))
            screen.set_fond()
            interragibles[0].set_pos(pourcentage(0.225, 0.79, screen))
            interragibles[1].set_pos(pourcentage(0.725, 0.8, screen))
            sound[g.music].set_pos(pourcentage(0.95, 0.9, screen))
            jauge_leg.set_pos((pourcentage(0.3 ,0.05 ,screen)))
            jauge_jus.set_pos((pourcentage(0.525, 0.05 , screen)))
            jauge_pop.set_pos((pourcentage(0.75, 0.05, screen)))

        # click de souris
        if event.type == pygame.MOUSEBUTTONDOWN:
    
            # click gauche :
            if event.button == 1:
                for bouton in interragibles and sound:
                    # Si le bouton est clické, alors sont état est clické
                    bouton.set_clicked(bouton.is_clicked())


        # lacher le clic
        if event.type == pygame.MOUSEBUTTONUP:
    
            # clic gauche :
            if event.button == 1:
                if ecran == screen.PROLOGUE:
                    ecran = screen.MAIN
                elif ecran == screen.MAIN:
                    for bouton in interragibles:
                        # Du fait que le bouton est laché, il ne peut pas y avoir de bouton clické
                        if bouton.is_clicked() and not arret:
                            screen.remove_on_screen(EVENT)
                            screen.remove_on_screen(GRADE)
                            choix = bouton.click()
                            evenement = g.set_event(choix, evenement)
                            g.set_attente_reponse(False)
                            if evenement[0] == False: # Si il se passe quelque chose de particulier
                                if evenement[1] == FIN_TEMPS:
                                    screen.set_fond('image/temps_out.jpg')
                                    arret = (True, T_FIN_TEMPS, (0.5, 0.1), BLANC)
                                    bouton.set_clicked(False)
                                elif evenement[1] == FIN_PRISON:
                                    screen.set_fond('image/justice_out.webp')
                                    arret = (True, T_FIN_PRISON, (0.3, 0.2), ROUGE)
                                    bouton.set_clicked(False)
                                elif evenement[1] == FIN_GAGNE:
                                    screen.set_fond('image/fin_gagne.jpg')
                                    arret = (True, T_FIN_GAGNE, (0.3, 0.2), BLANC)
                                    bouton.set_clicked(False)
                    for bouton in sound:
                        if bouton.is_clicked() and not arret:
                            bouton.click()
                            bouton.set_clicked(False)

    if ecran == screen.PROLOGUE:                        #Ecran de prologue
        afficher_text(T_PROLOGUE, screen, screen.font, screen.PROLOGUE, (0.5, 0.5), True, BLANC)

    elif ecran == screen.MAIN: # en attente de réponse

        if not g.get_attente_reponse() and not arret: # Si il n'attend pas de réponses
            screen.remove_on_screen(screen.PROLOGUE)
            evenement = g.get_event() # Charger un événement
            g.set_attente_reponse(True) # Le mettre en attente d'un réponse
            if evenement[0] == False: # Si il se passe quelque chose de particulier
                if evenement[1] == FIN_DICT_VIDE:
                    screen.set_fond('image/pop_out.jpg')
                    arret = (True, T_FIN_DICT_VIDE, (0.5, 0.2), NOIR)

                #screen.error(evenement[1])
        if not arret:
            g.set_fond(screen) # Mettre le fond au grade correspondant
            for i in interragibles: # Ajout des boutons oui/non
                i.actualiser(screen)
                i.set_clicked(False)
            sound[g.music].actualiser(screen)
            sound[g.music].set_clicked(False)
            # Et on remplace par les nouvelles infos
            afficher_text(g.grade.capitalize(), screen, screen.font40, GRADE, (0.12, 0.055))
            if g.get_grade() == PRESIDENT or g.get_grade() == CITOYEN :
                afficher_text(evenement[1]['titre'], screen, screen.font, EVENT, (0.5, 0.5), True, NOIR)
            else :
                afficher_text(evenement[1]['titre'], screen, screen.font, EVENT, (0.5, 0.5), True, BLANC)
            afficher_text(g.jauges.temps.get_date(), screen, screen.font, DATE, (0.12, 0.17))
            jauge_leg.remplissage(g.jauges.legalite.get_leg(),100)
            jauge_jus.remplissage(g.jauges.justice.get_jus(), 100)
            jauge_pop.remplissage(g.jauges.popularite.get_pop(), g.max_grade())
            jauge_leg.actualiser(screen)
            jauge_jus.actualiser(screen) 
            jauge_pop.actualiser(screen) 

        else:
            afficher_text(arret[1], screen, screen.font, FIN, arret[2], True, arret[3])
    pygame.display.flip()
    screen.clock.tick(60)           #Fréquence d'affichage (60FPS)


pygame.quit()