import room, item, character

hero_player = character.Player()
main_room = room.Room([hero_player], 10, 10)
main_room.spawn(hero_player, hero_player.location)

keep_playing = True
while keep_playing:
	print(repr(main_room))
	inkey = input("Next command: ")
	if inkey[0] in ['w', 'W']:
		new_loc = (hero_player.location[0] - 1, hero_player.location[1])
		hero_player.location = new_loc
	elif inkey[0] in ['q', 'Q']:
		keep_playing = False
	main_room.spawn(hero_player, hero_player.location)