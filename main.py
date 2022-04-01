from src.gestion import Gestion
from src.utils.texts import PROLOGUE
from pygameSettings import *


def main():
    g = Gestion()

    screen = pygame.display.set_mode((1280, 720))

    ouvert = True

    while ouvert: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                ouvert = False
            screen.blit(font.render(PROLOGUE, True, (0, 0, 255)), (1000, 1000))
    pygame.quit()
    g.set_nom(input('Bonjour, quel est ton nom? '))
    print(PROLOGUE)
    g.lancement()

if __name__ == '__main__':
    main()
