import random

class Clubs:
    teams = ["Galatasaray", "Fenerbahçe", "Samsunspor", "Eyüpspor", "Göztepe",
             "Başakşehir", "Beşiktaş", "Kasımpaşa", "Alanyaspor", "Rizespor",
             "Trabzonspor", "Gaziantep FK", "Antalyaspor", "Konyaspor", "Sivasspor",
             "Kayserispor", "Bodrumspor", "Hatayspor", "Adana Demirspor"]

    def __init__(self):
        self.teams = Clubs.teams[:]
        if len(self.teams) % 2 == 1:
            self.teams.append("Bay")

    def set_fixture(self):
        num_weeks = len(self.teams) - 1
        fixture = {}

        teams = self.teams[:]
        random.shuffle(teams)

        for week in range(1, num_weeks + 1):
            matches = []

            for i in range(len(teams) // 2):
                home = teams[i]
                away = teams[-(i + 1)]
                if home != "Bay" and away != "Bay":
                    matches.append(f"{home} - {away}")

            fixture[week] = matches

            # Round-robin
            teams = [teams[0]] + [teams[-1]] + teams[1:-1]

        return fixture

    def print_fixture(self):
        fixture = self.set_fixture()
        for week, matches in fixture.items():
            print(f"Week {week}:")
            for match in matches:
                print(match)
            print("-" * 20)


clubs = Clubs()
clubs.print_fixture()
