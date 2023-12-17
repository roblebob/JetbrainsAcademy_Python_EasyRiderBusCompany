# work with these variables
rivers = set(input().split())
states = set(input().split())
rivers -= states
print(rivers)