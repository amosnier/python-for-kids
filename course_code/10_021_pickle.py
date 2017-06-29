import pickle
game_data = {
        'player_position' : 'N23 E45',
        'in_pockets' : ['keys', 'pocket knife', 'polished stone'],
        'in_backpack' : ['rope', 'hammer', 'apple'],
        'wealth' : 158.50
}
file = open('data/save.dat', 'wb')
pickle.dump(game_data, file)
file.close()

file = open('data/save.dat', 'rb')
print(pickle.load(file))
print()

file.seek(0)
print(pickle.load(file)['player_position'])
file.close()
print()
