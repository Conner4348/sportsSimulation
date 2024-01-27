# Here is the main file that simulates the sports matches.

from itertools import combinations
from random import randint

# TEST DATA SET

# Teams
teams = {
    'Argentina': 1,
    'Brazil': 1,
    'Uruguay': 1,
    'Colombia': 1,
    'Ecuador': 1,
    'Peru': 1,
    'Chile': 1,
    'Venezuela': 1,
    'Paraguay': 1,
    'Bolivia': 1
}





class simulate:

    def __init__(self, teams):
        self.teams = teams
        self.teams_list = [key for key in teams.keys()]

    def create_schedule(self):
        matches = list(combinations(self.teams_list, 2))
        #opponents = {key: [] for key in self.teams.keys()}
        self.schedule = [[] for i in range(len(self.teams_list)-1)]


        for match in matches:
            team_one, team_two = match

            for round in self.schedule:
                if len(round) == 0:
                    round.append(match)
                    print(f'{match} appended to round: {self.schedule.index(round)} for being the first match.')
                    break

                teams_in_round = []
                for draw in round:
                    teams_in_round += list(draw)
                if (team_one not in teams_in_round) and (team_two not in teams_in_round):
                    round.append(match) 
                    print(f'{match} appended to round: {self.schedule.index(round)}.')
                    break
                print(f'{match} not appended to any round...')
                        

        #while num_matches < total_matches:
            #for match in matches:
            #for key, val in opponents.items():
                #print(num_matches)
                #for match in matches:
                #    if (match[0] == key) and (match[1] not in val) and (match[0] not in teams_record) and (match[0] not in teams_record):

                #if (match[0] not in teams_record and match[1] not in teams_record):
                    #if (match[1] not in opponents[match[0]]) and (match[0] not in opponents[match[1]]):
                    #self.schedule.append(match)
                    #teams_record.append(match[0])
                    #teams_record.append(match[1])

                        #opponents[match[0]] += match[1]
                        #opponents[match[1]] += match[0]
                        #teams_record.append(match[0])
                        #teams_record.append(match[1])
                    
                        #self.schedule.append(match)
                        #num_matches += 1
                    #continue
                #if len(teams_record) == len(self.teams_list):
                #    teams_record = []

    def print_schedule(self):
        for round in self.schedule:
            print('')
            for match in round:
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
        sorted_rankings = {key: val for key, val in sorted(self.teams.items(), key=lambda item: item[1], reverse=True)}
        for key, val in sorted_rankings.items():
            print(key, val)

            






round = 0
while round < 1:
    test_simulate = simulate(teams)
    test_simulate.create_schedule()
    #test_simulate.print_schedule()
    #test_simulate.simulate_match()
    #test_simulate.print_rankings()
    round += 1

#print('')
#print('Final rankings:')
#test_simulate.print_rankings()