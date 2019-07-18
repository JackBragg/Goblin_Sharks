import random

def play(player_One_Choice):

    l_RPS = ['Rock', 'Paper', 'Scissors']
    pc = player_One_Choice
    cc = random.choice(l_RPS)
    l_Rock = ['Scissors', 'Paper']
    l_Paper = ['Rock', 'Scissors']
    l_Scissors = ['Paper', 'Rock']
    scenarios = {'Rock':l_Rock, 'Paper':l_Paper, 'Scissors':l_Scissors}

    if pc == cc:
        return tie(pc, cc)
    elif cc == scenarios[pc][0]:
        return player_Win(pc, cc)
    elif cc == scenarios[pc][1]:
        return computer_Win(pc, cc)


def tie(pc, cc):
    print(f'You chose {pc} the computer chose {cc} Its a tie!')
    return True

def player_Win(pc, cc):
    print(f'You chose {pc} the computer chose {cc} you win!')
    return True

def computer_Win(pc, cc):
    print(f'You chose {pc} the computer chose {cc} you loose!')
    return False


def controls(pOC):
    if pOC == 1:
        return 'Rock'
    elif pOC == 2:
        return 'Paper'
    elif pOC == 3:
        return 'Scissors'
    elif pOC == 4:
        return controls(random.randint(1,3))
    else:
        print('Incorrect input!')


def game():
    player_One_Choice = int(input('\nLet\'s Rock, Paper, Scissors!\n'
                                    + 'Rock:        1\n'
                                    + 'paper:       2\n'
                                    + 'scissors:    3\n'
                                    + 'Suprise me:  4\n'))
    player_One_Choice = controls(player_One_Choice)
    return play(player_One_Choice)
