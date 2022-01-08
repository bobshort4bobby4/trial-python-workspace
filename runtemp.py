# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

"""
trial to see if i could parse a json file.
"""
import json

horsedata = []
for line in open('./data/5line-horsepro.json', 'r'):
    horsedata.append(json.loads(line))

print(type(horsedata))
print()
print("lenght of the horsedate file is", len(horsedata))
for i in range(len(horsedata)):
    print(f"type of the {i} th line is", type(horsedata[i]))

###for i in range(len(horsedata)):
# #for key in horsedata[i].items():
#        print(horsedata[i]['mc'])
#print(horsedata[0])
line = horsedata[0]
print(horsedata[0]['mc'][0]['id'])
print(len(horsedata[0]['mc']))
print(len(horsedata[0]['mc'][0]))
print(horsedata[0]['mc'][0]['marketDefinition'])
