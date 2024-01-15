'''
Game class that creates the needed methods for running the game
Author: Mehar Klair
Date: 2023-04-06
'''

from castle import Castle
from room import Room
from diamond import Diamond
from player import Player
PLAYERS = 2
class Game():
    ''' creates a game object'''
    def __init__(self):
        '''initializes the objects needed to run the game'''
        self.castle = Castle()
        self.players = []
        self.finished = []
        self.turn = 0
        
    def read_file(self, filename):
        ''' reads the textfile for the game'''
        alist = []
        with open(filename, 'r') as file:
            file_list = file.readlines()
        for item in file_list:
            item = item.strip()
            alist.append(item)  
        return alist
    
    def initialize_from_file(self, filename):
        ''' starts the creating of the rooms from the file'''
        
        alist = self.read_file(filename)
        # creates the room as an empty room
        for item in alist:
            items = item.split(':')
            if items[0] == 'E' or items[0] == 'X': 
                self.castle.castle[items[0]] = [items[1]]   
            else:
                self.castle.add_room(Room(),items[0])
        # builds the room by setting everything
        for item in alist:
            self.build_room(item)
        # finds the start and sets the position   
        start = int(self.castle.get_entrance_ID()[0][1])
        for item in self.players:
            item.set_position(start)
            item.add_to_path(start, None)
        
    def build_room(self,item):
        ''' builds the room by seetting links and ids'''
        items = item.split(':')
        room_info = items[1].split(',')
        # does not create a room object for entrance or exit data
        if items[0] == 'E' or items[0] == 'X':
            pass
        else:
            items[0] = int(items[0])
            room = self.castle.castle[items[0]] 
            room.set_id(items[0])
            # builds the links of all the rooms
            if room_info[0].strip() == '0' or room_info[0].strip() == 'E' or room_info[0].strip() == 'X':
                room.set_link('north', room_info[0].strip())
            else:
                room.set_link('north', self.castle.castle[int(room_info[0].strip())])
                
            if room_info[1].strip() == '0' or room_info[1].strip() == 'E' or room_info[1].strip() == 'X':
                room.set_link('south', room_info[1].strip())
            else:
                room.set_link('south', self.castle.castle[int(room_info[1].strip())])
                
                
            if room_info[2].strip() == '0' or room_info[2].strip() == 'E' or room_info[2].strip() == 'X':
                room.set_link('east', room_info[2].strip())
            else:
                room.set_link('east', self.castle.castle[int(room_info[2].strip())])
                
                
            if room_info[3].strip() == '0' or room_info[3].strip() == 'E' or room_info[3].strip() == 'X':
                room.set_link('west', room_info[3].strip())
            else:
                room.set_link('west', self.castle.castle[int(room_info[3].strip())])
           
            # sets the wormholes portals and diamonds
                
            if room_info[-1].strip() == 'W':
                room.set_wormhole(True)
            elif room_info[-1].strip() == 'P':
                room.set_portal(True)
            elif 'D' in room_info[-1]:
                room.set_diamond(Diamond(len(room_info[-1].strip())))

            # checks if there is a wormhole or portal in the room with the exit or entrance
            if type(items[0]) == int:
                room = self.castle.castle[items[0]]
                if room.isthere_entrance_exit_door():
                    if room.get_wormhole() or room.get_portal():
                        raise Exception('cannot have a wormhole or portal in entrance or exit room')
                
    def get_turn(self):
        '''gets the turn'''
        return self.turn
    
    def set_turn(self, turn):
        '''sets the turn'''
        self.turn = turn
        
    def get_player(self, player_id):
        ''' gets current player'''
        
        for item in self.players:
            if item.get_player_id == player_id:
                return item
            
    def move(self):
        ''' gets players input and moves them'''
        player = self.players[self.turn]
        # if the player is done it passes their turn
        if player in self.finished:
            pass
        else:
            current_pos = player.get_position()
            print(f"It's player  {player.get_player_id() + 1}  turn")
            
            # asks the user unitl output it right
            user_input = input('Please input a direction (North, South, East, West): ')
            valid = False
            while not valid:
                if user_input.lower() == 'west' or user_input.lower() == 'east' or user_input.lower() == 'north' or user_input.lower() == 'south':
                    valid = True
                else:
                    print('invalid direction')
                    user_input = input('What direction do you want to move (North, South, East, West): ')
                
            # gets the next room       
            print(f'Player  {player.get_player_id() + 1} , previous room {current_pos}')
            next_room = self.castle.get_next_room(current_pos, user_input)
            
            # for the special cases that are not another room
            if next_room == 'E':
                raise Exception('you entered through that door')
            elif next_room == '0':
                raise Exception('there is nothing through that door')
            elif next_room == 'X':
                self.finished.append(player)
                print(f'Player {player.get_player_id() + 1} exited the castle! {user_input}')
            else:   
                if next_room.get_diamond() != None:
                    self.update_diamonds(player, next_room)
                    
                player.add_to_path(next_room, user_input) 
                
                print(f'Player  {player.get_player_id() + 1} , {user_input.lower()} ,  New room {next_room.get_id()}')
                player.move(next_room)
        
    def is_finished(self):
        ''' checks if the game is finished'''
        if len(self.finished) == PLAYERS:
            return True
        return False
    
    def update_diamonds(self,player, room):
        ''' updates the diamonds for the player and the room'''
        
        room_diamonds = room.get_diamond().get_diamonds()
        player.set_diamonds(room_diamonds)
        room.set_diamond(None)        
        print(f'Number of Diamonds: {room_diamonds} TOTAL:  {player.get_diamonds()}')
       
