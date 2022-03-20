from datetime import date as dt

class Date:

    MOIS_COURANT = int(dt.today().strftime('%m'))
    ANNEE_COURANT = int(dt.today().strftime('%Y'))

    @staticmethod
    def ajouter_mois(mois:int) -> tuple:
        """ajouter mois, ajoute un mois et retourne la nouvelle date

        Args:
            mois (int): nombre de mois à ajouter

        Returns:
            tuple: date sous la forme (mm, YYYY)
        """        
        return (
            (Date.MOIS_COURANT + mois) % 12, 
            ((Date.MOIS_COURANT + mois) // 12) + Date.ANNEE_COURANT
        )

    @staticmethod
    def mois_ig(mois:int) -> str:
        """mois_ig, calcule le mois dans le jeu puis le retourne sous forme de string

        Args:
            mois (int): nombre de mois à ajouter

        Returns:
            str: date sous la forme mm/YYYY
        """        
        date_ig = Date.ajouter_mois(mois)
        return f"{date_ig[0]}/{date_ig[1]}"

    @staticmethod
    def get_mois() -> int:
        """get mois, retourne le mois courant

        Returns:
            int: mois corant
        """        
        return Date.MOIS_COURANT

    @staticmethod
    def get_annee() -> int:
        """get annee, retourne l'année courante

        Returns:
            int: année courante
        """        
        return Date.ANNEE_COURANT

    @staticmethod
    def get_date() -> str:
        return f"{Date.MOIS_COURANT}/{Date.ANNEE_COURANT}"

    @staticmethod
    def __str__() -> str:
        return f"{Date.MOIS_COURANT}/{Date.ANNEE_COURANT}"

    @staticmethod
    def __repr__() -> str:
        return f"{Date.MOIS_COURANT}/{Date.ANNEE_COURANT}"
