# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

"""
trial to see if i could parse a json file.
"""
import json

horsedata = []
for line in open('twoline-horsepro.json', 'r'):
    horsedata.append(json.loads(line))

print(type(horsedata))
print()
print("lenght of the horsedate file is", len(horsedata))
print("type of the fisrt line is", type(horsedata[0]))

for key, value in horsedata[0].items():
    print(f"Key: {key} Value {value}")
    print("------------------")
