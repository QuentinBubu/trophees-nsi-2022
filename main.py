from time import sleep
from src.screen import Screen
from src.gestion import Gestion
from src.utils.texts import T_FIN_DICT_VIDE, T_PROLOGUE
from src.utils.constante import FIN_DICT_VIDE, GRADE, EVENT, DATE
from pygameSettings import *
from bouton import *
g = Gestion()
ouvert = True
arret = (False)
screen = Screen()
ecran = screen.WAITING

interragibles = [
            Bouton((240, 580), (120, 60), "image/oui.png", "image/oui_c.png", g.retour_true),
            Bouton((890, 580), (120, 60), "image/non.png", "image/non_c.png", g.retour_false)
]
once = True
while ouvert:
    
    if once:
        once = False
        screen.set_fond('image/logo.png')
        pygame.display.flip()
        sleep(0)
        screen.set_fond('image/temp_debut.jpg')
        ecran = screen.PROLOGUE

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ouvert = False
        if event.type == pygame.VIDEORESIZE:
            screen.set_screen(pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE))

        # click de souris
        if event.type == pygame.MOUSEBUTTONDOWN:
            # click gauche :
            if event.button == 1:
                for bouton in interragibles:
                    # Si le bouton est clické, alors sont état est clické
                    bouton.set_clicked(bouton.is_clicked())

        # lacher le clic
        if event.type == pygame.MOUSEBUTTONUP:
            # clic gauche :
            if event.button == 1:
                if ecran == screen.PROLOGUE:
                    ecran = screen.MAIN
                for bouton in interragibles:
                    # Du fait que le bouton est laché, il ne peut pas y avoir de bouton clické
                    if bouton.is_clicked():
                        choix = bouton.click()
                        g.set_event(choix, evenement)
                        g.set_attente_reponse(False)
                    bouton.set_clicked(False)

    if ecran == screen.PROLOGUE:
        afficher_text(T_PROLOGUE, screen, screen.font, screen.PROLOGUE, (0.5, 0.5), True, BLANC)
    elif ecran == screen.MAIN: # en attente de réponse
        if not g.get_attente_reponse(): # Si il n'attend pas de réponses
            screen.remove_on_screen(screen.PROLOGUE)
            screen.remove_on_screen(EVENT)
            screen.remove_on_screen(GRADE)
            screen.remove_on_screen('FIN')
            evenement = g.get_event() # Charger un événement
            g.set_attente_reponse(True) # Le mettre en attente d'un réponse
            if evenement[0] == False: # Si il se passe quelque chose de particulier
                # ouvert = False
                if evenement[1] == FIN_DICT_VIDE:
                    screen.set_fond('image/pop_out.webp')
                    arret = (True, T_FIN_DICT_VIDE)
                    
                #screen.error(evenement[1])
        # On enlève ce qu'il y a à l'écran
        if not arret:
            for i in interragibles: # Ajout des boutons oui/non
                i.actualiser(screen)
                i.set_clicked(False)
            # Et on remplace par les nouvelles infos
            afficher_text(g.grade.capitalize(), screen, screen.font50, GRADE, (0.12, 0.055))
            afficher_text(evenement[1]['titre'], screen, screen.font, EVENT)
            afficher_text(g.jauges.temps.get_date(), screen, screen.font, DATE, (0.12, 0.17))
            g.set_fond(screen) # Mettre le fond au grade correspondant
        else:
            afficher_text(arret[1], screen, screen.font, 'FIN')

    pygame.display.flip()
    screen.clock.tick(60)


pygame.quit()