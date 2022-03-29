from src.utils.constante import FIN_GAGNE, FIN_TEMPS, FIN_PRISON
from src.utils.texts import T_FIN_GAGNE, T_FIN_PRISON, T_FIN_TEMPS

class Affichage:
    @staticmethod
    def erreur(erreur:str):
        print(erreur)

    @staticmethod
    def fin_jeu(fin):
        if fin == FIN_GAGNE:
            print(T_FIN_GAGNE)
        elif fin == FIN_TEMPS:
            print(T_FIN_TEMPS)
        elif fin == FIN_PRISON:
            print(T_FIN_PRISON)
        else:
            Affichage.erreur('Fin inconnu')