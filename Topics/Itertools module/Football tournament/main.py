import itertools

# the variable 'teams' is already defined
for match in itertools.combinations(teams, 2):
    print(match)