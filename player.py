'''
player class that creates the player and holds their specific info
Author: Mehar Klair
Date: 2023-04-06
'''

class Player():
    ''' creates a player object to hold the players info within the game'''
    def __init__(self, player_id):
        '''initializes the player class'''
        self.player_id = player_id
        self.current_pos = None
        self.diamonds = 0
        self.moves = []
    def __str__(self):
        ''' returns a string repr of player'''
        return f'Player {self.player_id + 1}: {self.diamonds} diamonds'
   
    
    def get_position(self):
        ''' gets the players position'''
        return self.current_pos
    
    def set_position(self, ID):
        '''sets the players position to a new one'''
        # could add the old one in this step
        if 1 <= ID <= 25:
            self.current_pos = ID
        else:
            raise Exception('cannot create room outside of castle')
        
    def get_player_id(self):
        ''' get the players id'''
        return self.player_id
    
    def get_diamonds(self):
        ''' gets the number of diamonds collected'''
        return self.diamonds
    
    def set_diamonds(self,count):
        ''' sets the nubmer of diamonds'''
        # maybe plus equal
        self.diamonds += count
        
    def print_path(self):
        ''' prints the current path'''
        path = ''
        for item in self.moves:
            path += f' -> {item}'
        path = path[4:-4]
        print(path)
        
    def add_to_path(self, room_id, door_id):
        ''' adds the direction the player went to the path'''
        if door_id == None:
            self.moves.append(f'{room_id}')
        else:
            self.moves.append(f'{door_id.lower()}, {room_id.get_id()}')
        
    def move(self,room):
        ''' moves the current path '''
        room_id = room.get_id()
        self.set_position(room_id)