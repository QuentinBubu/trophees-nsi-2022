from src.Gestion import Gestion
from src.utils.texts import PROLOGUE

def main():
    g = Gestion()
    g.set_nom(input('Bonjour, quel est ton nom? '))
    print(PROLOGUE)

if __name__ == '__main__':
    main()
