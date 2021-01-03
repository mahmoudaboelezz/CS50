# Simulate a sports tournament

import csv
import sys
import random
import math

# Number of simluations to run
N = 1000


def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    with open("2018m.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            team = row[0]
            rating = int(row[1])
            teams.append({"team": team, "rating": rating})

    counts = {}
    for team in teams:
        counts[team["team"]] = 0

    for tournament in range(N):
        winner = simulate_tournament(teams)
        for team in teams:
            if team["team"] == winner:
                counts[team["team"]] += 1

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    original_teams = teams.copy()

    while len(teams) != 1:
        teams = simulate_round(teams)
    winner = teams[0]["team"]
    teams = original_teams
    return winner


if __name__ == "__main__":
    main()
