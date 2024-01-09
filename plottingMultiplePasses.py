import matplotlib.pyplot as plt
from mplsoccer import Sbopen, Pitch

parser = Sbopen();
df, releated, freeze, tactics = parser.event(69301);

"""
    to plot multiple passes from one time
    first, we need to filter the data to get the players from just one team
"""

mask_england = (df.type_name == "Pass") & (df.team_name == "England Women's") & (df.sub_type_name != "Throw-in")
df_passes = df.loc[mask_england, ['x', 'y', 'end_x', 'end_y', 'player_name']]

""" get the list of all players of the match that made a pass """
names = df_passes["player_name"].unique()

""" draw 4x4 pitches """
pitch = Pitch(line_color="black", pad_top=20)
fig, axs = pitch.grid(ncols=4, nrows=4, grid_height=0.85, title_height=0.06, axis=False, endnote_height=0.04, title_space=0.04, endnote_space=0.01)

""" for each player """
for name, ax in zip(names, axs['pitch'].flat[:len(names)]):
    #put player name over the plot
    ax.text(60, -10, name, ha='center', va='center', fontsize=14)
    #take only passes by this player
    player_df = df_passes.loc[df_passes["player_name"] == name]
    #scatter
    pitch.scatter(player_df.x, player_df.y, alpha = 0.2, s = 50, color = "blue", ax=ax)
    #plot arrow
    pitch.arrows(player_df.x, player_df.y, player_df.end_x, player_df.end_y, color = "blue", ax=ax, width=1)

#We have more than enough pitches - remove them
for ax in axs['pitch'][-1, 16 - len(names):]:
    ax.remove()

#Another way to set title using mplsoccer
axs['title'].text(0.5, 0.5, 'England passes against Sweden', ha='center', va='center', fontsize=30)
plt.show()