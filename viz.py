import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
from matplotlib import colors, colorbar
import numpy as np
from random import Random


class Plotter:

    def __init__(self):
        '''
        '''
        plt.ion()

    def draw_grid(self, gdata):
        '''
        '''
        r, c = len(gdata), len(gdata[0])

        # create discrete colormap
        # 0: Normal, 1: Wall, 2: Fire, 3: Safe, 4: Bottleneck, 5: Burning Wall
        cmap = colors.ListedColormap(['#ecf0f1', '#2c3e50', '#e74c3c',
                                      '#27ae60', '#f39c12', '#c0392b'])
        bounds = [-.5, .5, 1.5, 2.5, 3.5, 4.5, 5.5]
        norm = colors.BoundaryNorm(bounds, cmap.N)

        plt.imshow(gdata, cmap=cmap, norm=norm)

        # draw gridlines
        plt.grid(which='major', axis='both', linestyle='-', color='#bdc3c7', linewidth=0.5)
        plt.xticks(np.arange(-0.5, c, 1), [])
        plt.yticks(np.arange(-0.5, r, 1), [])


    def draw_people(self, x=[], y=[], c=[]):
        '''
        '''
        #                               alive      ded    safe    unknown
        cmap = colors.ListedColormap(['#3498db', '#34495e', '#2ecc71', '#f1c40f'])
        bounds = [-.5, .5, 1.5, 2.5, 3.5]
        norm = colors.BoundaryNorm(bounds, cmap.N)

        plt.scatter(x, y, c=c, cmap=cmap, norm=norm, edgecolors='white', linewidths=0.5, s=100)


    def visualize(self, graph={(3,4): {'F': 1}}, people=None, delay=.01):
        '''
        Draw the current state of `graph` and `people`.

        Parameters
        ----------
        graph : dict
            Floorplan graph mapping locations to attribute dictionaries.
        people : iterable
            List of Person objects to plot.
        delay : float
            Time (seconds) to pause after drawing; controls animation speed.
        '''

        # an arbitrary assignment of integers for each of the attributes for our
        # colormap
        attrmap = {'N': 0, 'W': 1, 'F': 2, 'S': 3, 'B': 4}

        # detect rows and columns
        r, c = 0, 0
        for loc, attrs in graph.items():
            r = max(r, loc[0]+1)
            c = max(c, loc[1]+1)

        # start with a blank grid and fill into attributes
        gdata = np.zeros(shape=(r, c))

        for loc, attrs in graph.items():
            for att in 'SWBF':
                if att not in attrs: continue
                if attrs[att]:
                    gdata[loc] = attrmap[att]
                    if att == 'W' and attrs['F']:
                        gdata[loc] = 5
                    break

        # use the accumulated data to draw the grid
        self.draw_grid(gdata)

        X, Y, C = [], [], []
        if people is not None:
            for p in people:
                row, col = p.loc
                R = Random(p.id)
                x, y = col-.5 + R.random(), row-.5 + R.random()
                if p.safe:
                    c = 2
                elif not p.alive:
                    c = 1
                elif p.alive:
                    c = 0
                else:
                    c = 3  # unknown state??

                X += [x]
                Y += [y]
                C += [c]

        self.draw_people(X, Y, C)

        # title does not display simulation time because it's not tracked here
        plt.title('Fire Evacuation Simulation', fontsize=14, color='#2c3e50')
        
        # matplotlib housekeeping
        plt.draw()
        plt.pause(max(delay, 0.001))
        plt.clf()







if __name__ == '__main__':
    print("Viz module loaded. Use through Plotter class.")
