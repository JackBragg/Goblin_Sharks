import room, item, character

hero_player = character.Player()
main_room = room.Room([hero_player], 10, 10)

game_over = False
while game_over == False:
	print(repr(main_room))
	inkey = input("Next command: ")
	if inkey[0] in ['w', 'W']:
		new_loc = (hero_player.location[0] - 1, hero_player.location[1])
		hero_player.location = new_loc
	elif inkey[0] in ['q', 'Q']:
		game_over = True	






 
