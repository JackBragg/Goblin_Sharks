import room, item, character
from random import randint
hero_player = character.Player()
main_room = room.Room([hero_player], 10, 10)
main_room.spawn(hero_player, hero_player.location)
#spawns the key in a random space
main_room.spawn(item.Item('Key', 'k'), (randint(1,8), randint(1,8)))
#this is a test

keep_playing = True
while keep_playing:
	print(main_room)
	inkey = input("Next command: ")
	cur_loc = hero_player.location
	if inkey[0] in ['w', 'W']:
		new_loc = (hero_player.location[0] - 1, hero_player.location[1])
	elif inkey[0]  in ['a', 'A']:
		new_loc = (hero_player.location[0], hero_player.location[1] - 1)
	elif inkey[0] in ['s', 'S']:
		new_loc = (hero_player.location[0] + 1, hero_player.location[1])
	elif inkey[0] in ['d', 'D']:
		new_loc = (hero_player.location[0], hero_player.location[1] + 1)
	elif inkey[0].lower() == 'k':
		print(hero_player.view_keyring())
	elif inkey[0] in ['q', 'Q']:
		keep_playing = False
	i, j = new_loc
	#coord object
	next_loc = main_room.coord_list[i][j]
	print(next_loc.has.name, next_loc.has)
	if next_loc.has.name == 'Key':
		hero_player.add_key(next_loc.has)
		print('You picked up a Key!')
		main_room.set_blank(new_loc)
	hero_player.location = new_loc
	main_room.spawn(hero_player, hero_player.location)
	main_room.set_blank(cur_loc)