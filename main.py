'''
Main function
Author: Mehar Klair
Date: 2023-04-06
'''

from game import Game
from player import Player
PLAYERS = 2
def main():
    ''' main function'''
    val = 1
    display_str = ''
    game = Game()
    for i in range(PLAYERS):
        player = Player(i)
        game.players.append(player)

    game.initialize_from_file('castle.txt')    
    while not game.is_finished():
        
        try:
            game.move()
        except Exception as e:
            print(e)            
        
        game.set_turn((val % PLAYERS))
        val += 1
       
    
    print('The game is finished!')
    for i in range(PLAYERS):
        game.players[i].print_path()
        
    for item in game.players:
        display_str += f'{str(item)}, '
    display_str = display_str[:-2] + '!' 
    print(f'Final score is {display_str} Good game!')
                   
        
main()
