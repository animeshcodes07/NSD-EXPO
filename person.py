# '''
# This file accompanies other files in the evacuation simulation project.
# people: Nick B., Matthew J., Aalok S.

# In this file we define a useful class for the agent, 'Person'
# '''

# import random

# class Person:
#     id = None
#     rate = None # how long it takes to move one unit distance
#     strategy = None # probability with which agent picks closes exit
#     loc = None, None # variable tracking this agent's location (xy coordinates)

#     alive = True # TODO get rid of this variable? we don't really need this
#     safe = False # mark safe once successfully exited. helps track how many
#                  # people still need to finish

#     exit_time = 0 # time it took this agent to get to the safe zone from its
#                   # starting point

# def __init__(self, id: int, rate: float = 1.0,
#              strategy: float = 0.7,
#              loc: tuple[int, int] = (0, 0)):
#     # def __init__(self, id, rate:float=1.0, strategy:float=.7, loc:tuple=None):
#         '''
#         constructor method
#         ---
#         rate
#         strategy
#         loc
#         '''
#         self.id = id
#         self.rate = rate
#         self.strategy = strategy
#         self.loc = tuple(loc)
#     def move(self, nbrs, rv=None, occupied=set()):
#         '''
#         when this person has finished their current movement, we must schedule
#         the next one
#         ---
#         graph (dict): a dictionary-like graph storing the floor plan according
#                       to our specification
#         occupied (set): set of (x,y) coordinates that are currently occupied by other people

#         return: tuple, location the agent decided to move to
#         '''
#         # filter out impassable squares (fire or wall)
#         nbrs = [(loc, attrs) for loc, attrs in nbrs
#                 if not (attrs['F'] or attrs['W'])]
#         if not nbrs:
#             return None
#         # Filter out occupied squares, but keep current location if we need to stay put
#         passable_nbrs = [(loc, attrs) for loc, attrs in nbrs if loc not in occupied]
        
#         # If all neighbors are occupied, the person stays in their current location
#         if not passable_nbrs:
#             return self.loc

#         choice = None
#         if rv is None:
#             rv = random.random()

#         if rv <= self.strategy:
#             # Smart movement: prioritize reaching safety while avoiding fire.
#             # We use a scoring system where lower is better.
#             def move_score(tup):
#                 loc, attrs = tup
#                 ds = attrs.get('distS', float('inf'))
#                 df = attrs.get('distF', float('inf'))
                
#                 # If fire is very close (e.g., < 3 tiles), prioritize moving away.
#                 # Penalty for being close to fire.
#                 fire_penalty = 0
#                 if df < 5:
#                     fire_penalty = (5 - df) * 10
                
#                 return ds + fire_penalty

#             choice = min(passable_nbrs, key=move_score)
#         else:
#             choice = random.choice(passable_nbrs)

#         loc, attrs = choice
#         self.loc = loc
#         if attrs['S']:
#             self.safe = True
#         elif attrs['F']:
#             self.alive = False

#         return loc
'''
This file accompanies other files in the evacuation simulation project.
'''

import random


class Person:

    def __init__(self, id: int,
                 rate: float = 1.0,
                 strategy: float = 0.7,
                 loc: tuple[int, int] = (0, 0)):
        """
        constructor method
        """
        self.id = id
        self.rate = rate
        self.strategy = strategy
        self.loc = tuple(loc) if loc is not None else (0, 0)

        self.alive = True
        self.safe = False
        self.exit_time = 0.0

    def move(self, nbrs, rv=None, occupied=None):
        """
        return: tuple location the agent decided to move to
        """

        if occupied is None:
            occupied = set()

        # filter out impassable squares
        nbrs = [(loc, attrs) for loc, attrs in nbrs
                if not (attrs['F'] or attrs['W'])]

        if not nbrs:
            return None

        passable_nbrs = [(loc, attrs) for loc, attrs in nbrs
                         if loc not in occupied]

        if not passable_nbrs:
            return self.loc

        if rv is None:
            rv = random.random()

        if rv <= self.strategy:

            def move_score(tup):
                loc, attrs = tup
                ds = attrs.get('distS', float('inf'))
                df = attrs.get('distF', float('inf'))

                fire_penalty = 0
                if df < 5:
                    fire_penalty = (5 - df) * 10

                return ds + fire_penalty

            choice = min(passable_nbrs, key=move_score)
        else:
            choice = random.choice(passable_nbrs)

        loc, attrs = choice
        self.loc = tuple(loc)

        if attrs['S']:
            self.safe = True
        elif attrs['F']:
            self.alive = False

        return loc