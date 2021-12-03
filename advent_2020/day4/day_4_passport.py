import re

with open(file="/home/urthor/projects/advent_of_code/advent_2020/day4/input/input",
          mode='r') as input1:
    problem_input = input1.read()

regex_input = re.split(pattern='\s|\n', string=problem_input)

print(type(regex_input))
print(regex_input[:100])
