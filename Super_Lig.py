import random

class SuperLig:
    teams = ["Galatasaray", "Fenerbahçe", "Samsunspor", "Eyüpspor", "Göztepe",
             "Başakşehir", "Beşiktaş", "Kasımpaşa", "Alanyaspor", "Rizespor",
             "Trabzonspor", "Gaziantep FK", "Antalyaspor", "Konyaspor", "Sivasspor",
             "Kayserispor", "Bodrumspor", "Hatayspor", "Adana Demirspor"]

    def __init__(self):
        self.teams = SuperLig.teams[:]
        if len(self.teams) % 2 == 1:
            self.teams.append("Bay")

        self.points = {team: 0 for team in self.teams if team != "Bay"}

    def simulate_match(self, home, away):
        home_score = random.randint(0, 4)
        away_score = random.randint(0, 4)
        return home_score, away_score

    def update_points(self, home, away, home_score, away_score):
        if home_score > away_score:
            self.points[home] += 3
        elif away_score > home_score:
            self.points[away] += 3
        else:
            self.points[home] += 1
            self.points[away] += 1

    def set_fixture(self):
        num_weeks = (len(self.teams) - 1) * 2
        fixture = {}

        teams = self.teams[:]
        random.shuffle(teams)

        # First Leg
        for week in range(1, len(self.teams)):
            matches = []
            for i in range(len(teams) // 2):
                home = teams[i]
                away = teams[-(i + 1)]

                if home != "Bay" and away != "Bay":
                    home_score, away_score = self.simulate_match(home, away)
                    self.update_points(home, away, home_score, away_score)
                    matches.append(f"{home} {home_score} - {away_score} {away}")

            fixture[week] = matches
            teams = [teams[0]] + [teams[-1]] + teams[1:-1]

        # Revenge Leg
        for week in range(len(self.teams), num_weeks + 1):
            matches = []
            for i in range(len(teams) // 2):
                home = teams[i]
                away = teams[-(i + 1)]

                if home != "Bay" and away != "Bay":
                    away_score, home_score = self.simulate_match(home, away)
                    self.update_points(home, away, home_score, away_score)
                    matches.append(f"{away} {away_score} - {home_score} {home}")

            fixture[week] = matches
            teams = [teams[0]] + [teams[-1]] + teams[1:-1]

        return fixture

    def print_fixture(self):
        fixture = self.set_fixture()
        for week, matches in fixture.items():
            print(f"Week {week}:")
            for match in matches:
                print(match)
            print("-" * 20)

    def print_standings(self):
        sorted_teams = sorted(self.points.items(), key=lambda x: x[1], reverse=True)
        print("\nFinal Standings:")
        print("-" * 30)
        for rank, (team, points) in enumerate(sorted_teams, start=1):
            print(f"{rank}. {team}: {points} points")
        print("-" * 30)

    def print_champion(self):
        champion = sorted(self.points.items(), key=lambda x: x[1], reverse=True)
        top_team, top_points = champion[0]
        print(f"Champion: {top_team} with {top_points} points")


super_lig = SuperLig()
super_lig.print_fixture()
super_lig.print_standings()
super_lig.print_champion()
