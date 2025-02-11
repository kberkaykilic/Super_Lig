# Super Lig Fixture Generator

This project generates fixtures for the Turkish Super Lig teams, ensuring that each team plays against every other team exactly once. It simulates a round-robin tournament where each match is randomly scheduled, and teams are paired to play home and away matches. Additionally, the program generates **random match scores** and calculates team points based on match results.

---

## Features

- **Randomized fixtures:** The teams' fixtures are randomized, ensuring a unique schedule every time.
- **Handles "Bay" team:** If the number of teams is odd, the program adds a "Bay" team for the week.
- **Round-robin scheduling:** Each team will face every other team exactly once.
- **Match score simulation:** Generates random match scores (e.g., 2-0, 1-1) for each fixture.
- **Points calculation:** Awards points based on match results (Win: 3 points, Draw: 1 point, Loss: 0 points).
- **Easy to use:** Simple Python script to generate and print fixtures for the entire season.

---

## How it Works

1. The teams are **randomly shuffled**.
2. A **fixture** is generated for each week of the season, with two teams playing against each other.
3. **Match scores are randomly generated**, simulating real game results.
4. **Points are calculated** based on match outcomes and stored in a standings table.
5. The program ensures that **no team plays against another more than once**, while also ensuring **no teams are left out**.

---

This project is **open for further improvements**, such as adding goal statistics, home/away advantages, and detailed season tracking. 🚀
