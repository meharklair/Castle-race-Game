'''
creates the room object that will be contained within the castle class
Author: Mehar Klair
Date: 2023-04-06
'''

import random
from diamond import Diamond
class Room:
    ''' represents a room object that the player moves into'''
    def  __init__(self, ID = None, north = None, south = None, east = None, west = None, portal: bool = False, wormhole: bool = False, diamonds: Diamond = None):
        ''' intializes the room class'''
        self.ID = ID
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.portal = portal
        self.wormhole = wormhole
        self.diamonds = diamonds
    def get_id(self):
        ''' returns the ID'''
        return self.ID
    def set_id(self, ID):
        ''' sets the ID'''
        if type(ID) == int:
            self.ID = ID
        else: 
            raise Exception('Id has to be of type integer')
        
    def generate_random_room_id(self):
        ''' generates a random room if a wormhole is found'''
        if self.wormhole == True:
            found_room = False
            while not found_room:
                ID = random.randint(1,25)
                if ID != self.ID:
                    found_room = True
            return ID
        else:
            raise Exception('There is no wormhole in this room (generate room function in room class)')
        
    def get_portal(self):
        '''checks if the current room has a portal'''
        return self.portal
    def set_portal(self,portal: bool):
        ''' sets the portal'''
        self.portal = portal
    def get_wormhole(self):
        ''' checks if current room has a wormhole'''
        return self.wormhole
    def set_wormhole(self, wormhole:bool):
        ''' sets the wromhole'''
        self.wormhole = wormhole
    def get_diamond(self):
        ''' gets the diamonds'''
        return self.diamonds
    def set_diamond(self, diamond: Diamond):
        ''' sets the diamonds'''
        self.diamonds = diamond
    def get_door(self,direction):
        ''' gets what value is at the door entered by the user'''
        if direction.lower() == 'east':
            return self.east
        elif direction.lower() == 'west':
            return self.west
        elif direction.lower() == 'north':
            return self.north
        elif direction.lower() == 'south':
            return self.south       
        else:
            raise Exception('invalid dircetion given')
    def set_link(self, direction, val):
        ''' will set the link of the door to something'''
        if val == '0' or 'E' or 'X' or type(val) == 'Room':
            if direction.lower() == 'east':
                self.east = val
            elif direction.lower() == 'west':
                self.west = val
            elif direction.lower() == 'north':
                self.north = val
            elif direction.lower() == 'south':
                self.south = val      
            else:
                raise Exception('invalid dircetion given')
        else:
            raise Exception('incorret value given for setting room link')
    def isthere_entrance_exit_door(self):
        ''' checks if a room has a entrance or exit'''
        if self.east == 'E' or self.east == 'X':
            return True
        elif self.west == 'E' or self.west == 'X':
            return True
        elif self.north == 'E' or self.north == 'X':
            return True
        elif self.south == 'E' or self.south == 'X':
            return True
        else:
            return False
