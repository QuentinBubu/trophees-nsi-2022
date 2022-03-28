from src.utils.constante import FIN_GAGNE, FIN_TEMPS, FIN_PRISON
from src.utils.texts import T_FIN_GAGNE, T_FIN_PRISON, T_FIN_TEMPS

class Gestion:

    nom = ""

    @staticmethod
    def fin_jeu(fin):
        if fin == FIN_GAGNE:
            print(T_FIN_GAGNE)
        elif fin == FIN_TEMPS:
            print(T_FIN_TEMPS)
        elif fin == FIN_PRISON:
            print(T_FIN_PRISON)

    def set_nom(self, nom:str) -> None:
        self.nom = nom

    def get_nom(self) -> str:
        return self.nom
