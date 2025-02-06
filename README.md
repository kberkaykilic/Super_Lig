# Super Lig Fixture Generator

This project generates fixtures for the Turkish Super Lig teams, ensuring that each team plays against every other team exactly once. It simulates a round-robin tournament where each match is randomly scheduled, and teams are paired to play home and away matches.

---

## Features

- **Randomized fixtures:** The teams' fixtures are randomized, ensuring a unique schedule every time.
- **Handles "Bay" team:** If the number of teams is odd, the program adds a "Bay" team for the week.
- **Round-robin scheduling:** Each team will face every other team exactly once.
- **Easy to use:** Simple Python script to generate and print fixtures for the entire season.

---

## How it Works

1. The teams are **randomly shuffled**.
2. A **fixture** is generated for each week of the season, with two teams playing against each other.
3. The program ensures that **no team plays against another more than once**, while also ensuring **no teams are left out**.

---
