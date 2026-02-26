'''
This file accompanies other files in the evacuation simulation project.
people: Nick B., Matthew J., Aalok S.

In this file we define a useful class to model bottlenecks, 'Bottleneck'
'''

from collections import deque

# bottleneck object, represents an area where people must queue to leave, given
# a set rate at which they can pass through, one by one
from typing import Deque, Tuple, Optional

class Bottleneck:
    # instance attributes will be initialized in __init__
    loc: Tuple[int, int]
    queue: Deque
    numInQueue: int = 0

    # takes a person, and inserts them into the queue of the bottleneck
    def enterBottleNeck(self, person, throughput=1):
        assert self.queue is not None, "queue not initialized"
        self.queue.append(person)
        self.numInQueue = self.numInQueue + throughput

    # removes a person from the queue
    def exitBottleNeck(self, throughput=1):
        assert self.queue is not None, "queue not initialized"
        if len(self.queue) > 0:
            personLeaving = self.queue.popleft()
            self.numInQueue = self.numInQueue - throughput
            return personLeaving
        else:
            return None

    def __init__(self, loc: Tuple[int, int]):
        '''
        constructor method
        ---
        loc (tuple xy): location (coordinates) of this bottleneck
        '''
        self.loc = loc              # coordinates of the bottleneck
        self.queue = deque()        # queue to represent the bottleneck
