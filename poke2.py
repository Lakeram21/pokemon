import pandas as pd
import matplotlib.pyplot as plt
from os import path


# reading an csv file with pandas
pdb = pd.read_csv("pokemon.csv")
newpk = pdb.drop(['abilities', 'against_bug', 'against_dark', 'against_dragon',
                  'against_electric', 'against_fairy', 'against_fight', 'against_fire',
                  'against_flying', 'against_ghost', 'against_grass', 'against_ground',
                  'against_ice', 'against_normal', 'against_poison', 'against_psychic',
                  'against_rock', 'against_steel', 'against_water', 'base_egg_steps',
                  'base_happiness', 'base_total', 'capture_rate', 'japanese_name',
                  'percentage_male', ], axis=1)


input1 = input("what is the name of the First Pokemon?:")
input2 = input("what is the name of the second Pokemon?:")

if ((input1 != type(str) or input2 != type(str)) and (len(input1) < 4 and len(input2) < 4)):
    print("Invalid Entry! or length of entry is too short")
    input1 = input("what is the name of the First Pokemon?:")
    input2 = input("what is the name of the First Pokemon?:")
name1 = input1.capitalize()  # Handeling lower case errors
name2 = input2.capitalize()

folderpath = "image"  # setting the path for the image to be saved
result1 = pdb.loc[pdb['name'].str.contains(name1)]
result2 = pdb.loc[pdb['name'].str.contains(name2)]


# making a new varibale so that title can be printed
title1 = result1['name'].values
title2 = result2['name'].values
type_poke1 = result1['type1'].values
type_poke2 = result2['type1'].values

# setting what is goin to be on the graph
real1 = result1[['defense', 'hp', 'sp_attack', 'sp_defense', 'speed', 'type1']]
real2 = result2[['defense', 'hp', 'sp_attack', 'sp_defense', 'speed', 'type1']]

# first choice
real1.plot(kind="bar", title=title1[0]+" Type: "+type_poke1[0], grid=True, color=[
    'C0', 'C1', 'C2', 'C3', 'C4'])
plt.figure(1)
plt.xlabel("Skill Type")
plt.ylabel("Skill Level")
plt.savefig(path.join(folderpath, 'plot1.png'.format()))

# second choice
real2.plot(kind="bar", title=title2[0]+" Type: "+type_poke2[0], grid=True, color=[
    'C0', 'C1', 'C2', 'C3', 'C4'])

plt.figure(2)

plt.xlabel("Skill Type")
plt.ylabel("Skill Level")
# Saving the image to a path
plt.savefig(path.join(folderpath, 'plot2.png'.format()))


plt.tight_layout()
plt.show()
