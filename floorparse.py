#!/usr/bin/env python3

from collections import defaultdict

class FloorParser:

    def __init__(self):
        pass

    def parse(self, floor):
        '''
        parses a txt floor
        '''
        grid = []

        for row in floor.split('\n'):
            if not row: continue
            sqs = row.split(';')
            rowattrs = [set(sq.strip().split(',')) for sq in sqs]
            # debug output removed – the caller may not want to see each
            # row of the parsed floor plan on every invocation
            grid += [rowattrs]


        # every square has the same set of numeric attributes; use a helper
        # so that a fresh dictionary is created for every new key instead of
        # sharing the same mutable object (which was a subtle bug before the
        # refactor that added the new flags).
        def default_attrs():
            return {'nbrs': set(), 'W': 0, 'S': 0, 'B': 0, 'F': 0, 'N': 0, 'P': 0}
        
        graph = defaultdict(default_attrs)

        R, C = len(grid), len(grid[0])

        for i in range(R):
            for j in range(C):
                attrs = grid[i][j]
                
                for off in {-1, 1}:
                    if 0 <= i+off < R:
                        graph[(i,j)]['nbrs'].add((i+off, j))

                    if 0 <= j+off < C:
                        graph[(i,j)]['nbrs'].add((i, j+off))
                
                for att in 'WSBFNP':
                    graph[(i,j)][att] = int(att in attrs)

        self.graph = dict(graph.items())
        return self.graph


    def tostr(self, graph):
        '''
        '''
        r, c = 0, 0
        for loc, attrs in graph.items():
            r = max(r, loc[0])
            c = max(c, loc[1])
        r, c = r+1, c+1

        s = ''
        for r_ in range(r):
            for c_ in range(c):
                sq = graph[(r_, c_)]
                # this =
                att = ','.join([a for a in sq if a in 'BNSFWP' and sq[a]])
                s += '{:>4}'.format(att)
            s += '\n'

        return s
