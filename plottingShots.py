import matplotlib.pyplot as plt
import numpy as np
from mplsoccer import Pitch, Sbopen, VerticalPitch

"""
    First thing to do is, obvius, to open the dataset
    we gonna use a parse available in mplsoccer, SBopen
    Using the method event and putting the id of the game as parameter we load the data
    The data is store in a dataframe named df 
    from this dataframe we will take out the name of the two teams
    then, we gonna filter the dataframe to see only the shots
"""
parser = Sbopen();
df, related, freeze, tactics = parser.event(69301);

""" here we goona take the team names """
team1, team2 = df.team_name.unique();

""" Now it is time to filter the data to see only the shots, that is what we are looking for """
shots = df.loc[df["type_name"] == 'Shot'].set_index('id');

"""
    making the shots map using iterative solution
"""

"""
    first, lets draw the pitch using the MPL soccer class
    we will set the variable of the width and height of the pitch, using the stats bombs coordinates
    they use yards

    To plot the data, we will run throught the shot data that we have filtered before
    we will take the x and y coordinates of the shot, the team name and if the goal was scored or not
    if the goal was scored we plot a solid circle with the name of the player
    if not, we plot a translucid circle
    To have england shots on one half and Sweden shots on the other half, we subtract x and y from the
    pitch width and height

    Football data tends to be attacking left to right, and we will use this as default in the course.
"""

pitch = Pitch(line_color="black");
fig, ax = pitch.draw(figsize=(10,7));
#Size of the pitch in yards
pitchLengthX = 120;
pitchWidthY  = 80;

#plot the shots by looping through them
for i, shot in shots.iterrows():
    #get the information
    x=shot['x']
    y=shot['y']
    goal = shot['outcome_name'] == 'Goal'
    team_name = shot['team_name']
    #set circlesize
    circleSize = 2
    #ploting england
    if (team_name == team1):
        if goal:
            shotCircle = plt.Circle((x,y), circleSize, color="red")
            plt.text(x+1, y-2, shot['player_name'])
        else:
            shotCircle = plt.Circle((x,y), circleSize, color="red")
            shotCircle.set_alpha(.2)
    #ploting sweden
    else:
        if goal:
            shotCircle = plt.Circle((pitchLengthX-x, pitchWidthY-y), circleSize, color="blue")
            plt.text(pitchLengthX-x+1, pitchWidthY-y-2, shot['player_name'])
        else:
            shotCircle = plt.Circle((pitchLengthX-x, pitchWidthY-y), circleSize, color="blue")
            shotCircle.set_alpha(.2)
    ax.add_patch(shotCircle)

fig.suptitle("England (red) and Sweden (blue) shots", fontsize= 24)
fig.set_size_inches(10,7)
plt.show()
