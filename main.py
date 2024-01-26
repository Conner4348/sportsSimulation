# Here is the main file that simulates the sports matches.

from itertools import combinations
from random import randint

# TEST DATA SET

# Teams
teams = {
    'Argentina': 1,
    'Brazil': 1,
    #'Uruguay': 0,
    #'Colombia': 0,
    #'Ecuador': 0,
    #'Peru': 0,
    #'Chile': 0,
    #'Venezuela': 0,
    #'Paraguay': 0,
    #'Bolivia': 0
}





class simulate:

    def __init__(self, teams):
        self.teams = teams
        self.teams_list = [key for key in teams.keys()]

    def create_schedule(self):
        self.schedule = combinations(self.teams_list, 2)

    def print_schedule(self):
        for match in self.schedule:
            print(match)
        
    def simulate_match(self):
        for match in self.schedule:
            team_one, team_two = (team for team in match)
            
            team_one_points = self.teams[team_one]
            team_two_points = self.teams[team_two]
            total_points = team_two_points + team_two_points

            team_one_score = 0
            team_two_score = 0

            team_one_random = randint(0, total_points)
            while team_one_random < team_one_points:
                team_one_score += 1
                team_one_points //= 2
                team_one_points += 1
                total_points = team_two_points + team_two_points
                team_one_random = randint(0, total_points)

            team_two_random = randint(0, total_points)
            while team_two_random < team_two_points:
                team_two_score += 1
                team_two_points //= 2
                team_two_points += 1
                total_points = team_two_points + team_two_points
                team_two_random = randint(0, total_points)

            if team_one_score > team_two_score:
                self.teams[team_one] += 2
                if (team_two_score - 1) <= 0:
                    self.teams[team_two] = 1
                else:
                    self.teams[team_two] -= 1
            if team_one_score < team_two_score:
                self.teams[team_two] += 2
                if (team_one_score - 1) <= 0:
                    self.teams[team_one] = 1
                else:
                    self.teams[team_one] -= 1

    def print_rankings(self):
        for key, val in self.teams.items():
            print(key, val)

            






round = 0
while round < 10:
    test_simulate = simulate(teams)
    test_simulate.create_schedule()
    test_simulate.simulate_match()
    test_simulate.print_rankings()
    round += 1

print('')
print('Final rankings:')
test_simulate.print_rankings()