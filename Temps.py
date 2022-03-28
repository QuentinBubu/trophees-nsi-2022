from datetime import date, timedelta, datetime
import calendar
#from Gestion import Gestion

class Temps:

    LIMITE = 120 # Temps en mois
    DATE_REEL = datetime.today().strftime('%Y-%m-%d')

    actuel = 0

    mois = 0
    annee = 0

    # evenements = {} # {"date": evenement}

    def avancement(self, mois:int):
        self.actuel += mois

        date_ig = self.DATE_REEL + calendar.monthrange(self.DATE_REEL.split('-')[0], self.DATE_REEL.split('-')[1])[1]


        print(date_ig)
        if self.actuel >= self.LIMITE:
            pass
            # Gestion.fin_jeu(1)

    def __repr__(self):
        return f"{self.mois}/{self.annee}"

    def get_temps(self):
        return self.__repr__()

    def get_mois(self):
        return self.mois

    def get_annee(self):
        return self.annee

t = Temps()
t.avancement(1)