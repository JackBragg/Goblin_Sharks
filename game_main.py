import room, item, character
from random import randint
from Rock_Paper_Scissors import game as RPS


def start_card():
	msg = ''
	msg += '*'*60 + '\n' + '*'*60 + '\n'
	msg += 'Welcome to our game! Move around with \'wasd\' and \'q\' to quit.\nYou will need a key to open the door. Try asking the Boss.'
	msg += '\n' + '*'*60 + '\n' + '*'*60 + '\n'
	print(msg)

def end_card():
	msg = ''
	msg += '*'*60 + '\n' + '*'*60 + '\n'
	msg += '\t\tThank you for playing!\n\t\t\tCaleb\n\t\t\tJack\n\t\t\tScott\n'
	msg += '*'*60 + '\n' + '*'*60 + '\n'
	print(msg)


if __name__ == '__main__':
	start_card()

	hero_player = character.Player()
	main_room = room.Room([hero_player], 10, 10)
	main_room.spawn(hero_player, hero_player.location)
	#this is a test
	boss = character.Boss()
	main_room.spawn(boss, boss.location)
	main_room.add_door()
	new_loc = hero_player.location


	keep_playing = True
	while keep_playing:
		print(f'Health: {hero_player.health}')
		if boss.check(hero_player):
			print(f'Hello {hero_player.name}, you must defeat me in a supreme contest of skill...ROCK PAPER SCISSORS!')
			if RPS():
				main_room.set_blank(boss.location)
				boss.location = (-1,-1)
				boss.set_area()
				print('AHHHHHH you defeted me!!!')
				print(f'as the boss was leaving, they spitefully threw the key back into the room')
				main_room.spawn(item.Item('Key', 'k'), (randint(1,8), randint(1,8)))
			else:
				print('AHAHAHAHAHAHAHA! I WON!\n(you take 10 damage)')
				hero_player.health -= 10
		if main_room.door_check(hero_player):
			print('You opened the door!')

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
		if next_loc.has.name == 'Key':
			hero_player.add_key(next_loc.has)
			print('You picked up a Key!')
			main_room.set_blank(new_loc)
		if new_loc != cur_loc:
			hero_player.location = new_loc
			if main_room.spawn(hero_player, hero_player.location):
				main_room.set_blank(cur_loc)
			else:
				hero_player.location = cur_loc
				print('You can\'t go that way')
		if main_room.exit:
			if hero_player.location == main_room.exit.location:
				keep_playing = False

	end_card()