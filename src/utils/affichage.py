from src.utils.constante import FIN_GAGNE, FIN_TEMPS, FIN_PRISON, FIN_DICT_VIDE
from src.utils.texts import T_FIN_GAGNE, T_FIN_TEMPS, T_FIN_PRISON, T_FIN_DICT_VIDE

class Affichage:
    @staticmethod
    def fin_jeu(fin:int, screen) -> None:
        if fin == FIN_GAGNE:
            print(T_FIN_GAGNE)
        elif fin == FIN_TEMPS:
            print(T_FIN_TEMPS)
        elif fin == FIN_PRISON:
            print(T_FIN_PRISON)
        elif fin == FIN_DICT_VIDE:
            print(T_FIN_DICT_VIDE)
        else:
            Affichage.erreur('Fin inconnu')