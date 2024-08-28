players = ['charles','martina','micheal','florence','eli']
print(players)
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

print("here are the first three players of my time:")
for player in players[:3]:
    print(player.title())

