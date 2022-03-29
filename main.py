from src.gestion import Gestion
from src.utils.texts import PROLOGUE

def main():
    g = Gestion()
    g.set_nom(input('Bonjour, quel est ton nom? '))
    print(PROLOGUE)
    g.lancement()

if __name__ == '__main__':
    main()
