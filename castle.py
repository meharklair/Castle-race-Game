'''
Castle class that creates the castle object and the needed methods to traverse through it
Author: Mehar Klair
Date: 2023-04-06
'''

from room import Room
class Castle:
    ''' creates a castle object that will contain room objects for the player to traverse through'''
    def __init__(self):
        ''' initalizes the castle'''
        self.castle = {}
        
    def add_room(self,room:Room, room_ID):
        ''' adds a room if possible'''
        if room_ID == 'E' or room_ID == 'X':
            pass
        else:
            try:
                room_ID = int(room_ID) 
            except Exception:
                raise Exception('key needs to be of type int')                
            
        for key in self.castle.keys():
            if key == room_ID:
                raise Exception('room already exists at the given spot')
        self.castle[room_ID] = room
        
    def get_room(self, ID):
        '''checks to see if a given room is within the castle'''
        for key in self.castle.keys():
            if key == ID:
                return self.castle[ID]
        raise Exception('the given ID was not found in the castle')
        
    def change_room(self,ID,new_room):
        ''' changes the room at the given ID to the a new room'''
        if 1 <= ID <= 25:
            for key in self.castle.key():
                if key == ID:
                    self.castle[ID] = new_room
                        
        else:
            raise Exception('invalid ID (not within 1-25)')
        
    def get_next_room(self, room_id, door):
        current_room = self.castle[room_id] 
        next_room = current_room.get_door(door)
       
        if next_room == 'X' or next_room == 'E' or next_room == '0':
            return next_room

        if next_room.get_wormhole():
            print('Wormhole devoured you')
            room = self.castle[next_room.generate_random_room_id()]
            while room.get_wormhole():
                room = self.castle[next_room.generate_random_room_id()]
            next_room = room
        
            
        elif next_room.get_portal():
            print('You entered a portal')
            next_room = self.castle[int(self.get_entrance_ID()[0][1])]
         
            
        return next_room
   
    def get_entrance_ID(self):
        ''' returns the ID of the entrance'''
        for key in self.castle.keys():
            if key == 'E':
                return self.castle[key]
            
    def get_exit_ID(self):
        ''' returns the ID of exit'''
        for key in self.castle.keys():
            if key == 'X':
                return self.castle[key]
    

