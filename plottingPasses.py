import matplotlib.pyplot as plt
from mplsoccer import Pitch, Sbopen

"""
    first, to deal with the data of course we need to open the dataset
"""

parser = Sbopen();
df, releated, freeze, tactics = parser.event(69301);
passes = df.loc[df['type_name'] == 'Pass'].loc[df['sub_type_name'] != "Throw-in"].set_index('id');

"""
    Now that we have the passes, we need to plot it in some way
    so, let run throught the data and try to plot the data
    we will plot the passes made just by one especific player
    to do so, we will verify if the passs was made by Lucy Bronze, if so we will plot it
    and to realy plot the pass we gonna take the coordinates of the start of the pass
    and plot a circle in the this position
    but, a pass have a direction and a trajectory, right ? To plot it 
    we will subtract the coordinates of the beggining from the coordinates of the end of the pass
    in order to draw arrows that will represent the passes
"""

"""
    But, first to draw something in a pitch we need a picth 
"""
pitch = Pitch(line_color="black");

fig, ax = pitch.draw(figsize=(10,7));

""" now lets iterate """

for i, thepass in passes.iterrows():
    """ let verify if it was a pass made by lucy bronze """
    if thepass['player_name'] == 'Lucy Bronze':
        x = thepass['x']
        y = thepass['y']
        """ plot circle """
        passCircle = plt.Circle((x, y), 2, color="blue")
        passCircle.set_alpha(.2)
        ax.add_patch(passCircle)
        dx = thepass['end_x']-x
        dy = thepass['end_y']-y
        """ plot arrow """
        passArrow = plt.arrow(x, y, dx, dy, width=1, color="blue")
        ax.add_patch(passArrow)

ax.set_title("Lucy Bronze passes against Sweden", fontsize=24)
fig.set_size_inches(10,7)
plt.show()