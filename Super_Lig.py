import random

class Clubs:
    teams = ["Galatasaray", "Fenerbahçe", "Samsunspor", "Eyüpspor", "Göztepe",
             "Başakşehir", "Beşiktaş", "Kasımpaşa", "Alanyaspor", "Rizespor",
             "Trabzonspor", "Gaziantep FK", "Antalyaspor", "Konyaspor", "Sivasspor",
             "Kayserispor", "Bodrumspor", "Hatayspor", "Adana Demirspor"]

    def __init__(self):
        self.teams = Clubs.teams

    def set_fixture(self):
        random.shuffle(self.teams)  # Mix teams in the list.

        for i in range(0, len(self.teams), 2):
            if i + 1 < len(self.teams):
                print(self.teams[i], "-", self.teams[i + 1])

clubs = Clubs()
clubs.set_fixture()

