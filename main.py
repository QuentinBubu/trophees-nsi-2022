from src.screen import Screen
from src.gestion import Gestion
from src.utils.texts import T_PROLOGUE
from pygameSettings import *
from src.utils.constante import CITOYEN

g = Gestion()
ouvert = True
ecran = PROLOGUE
screen = Screen()

while ouvert:    
    screen.set_fond()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ouvert = False
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

    if ecran == MAIN:
        pass
    elif ecran == PROLOGUE:
        afficher_text(T_PROLOGUE, screen, screen.font, (0.5,0.5), True, BLANC)
    elif ecran == CITOYEN:
        afficher_text(CITOYEN, screen, screen.font, (0.1, 0.2), True, BLANC)
    afficher_text(CITOYEN.capitalize(), screen, screen.font50, (0.12, 0.055), True, BLANC)

    pygame.display.flip()
    screen.clock.tick(60)


pygame.quit()
#g.set_nom(input('Bonjour, quel est ton nom? '))
print(PROLOGUE)
g.lancement()
