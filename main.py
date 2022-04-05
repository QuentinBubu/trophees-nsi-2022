from src.gestion import Gestion
from src.utils.texts import PROLOGUE
from pygameSettings import *

def main():
    g = Gestion()
    ouvert = True
    once = True

    while ouvert: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                ouvert = False
            afficher_text(PROLOGUE)
            pygame.display.flip()
        once = False
    pygame.quit()
    g.set_nom(input('Bonjour, quel est ton nom? '))
    print(PROLOGUE)
    g.lancement()

if __name__ == '__main__':
    main()
