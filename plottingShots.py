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