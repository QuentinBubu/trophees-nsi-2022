from datetime import date as dt

def dateTest(Date):
    assert Date.get_mois() == int(dt.today().strftime('%m'))
    assert Date.get_annee() == int(dt.today().strftime('%Y'))

    assert Date.ajouter_mois(3) == (6, 2022) # mettre la date attendue
    print(Date())
