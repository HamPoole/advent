import string

with open(file="/home/urthor/projects/advent_of_code/advent_2021/day8/input8",
          mode='r') as input8:
    input_file = input8.readlines()

print(input_file[:5])
cleaned = [x[:-1] for x in input_file]

print(cleaned)

s = file="/home/urthor/projects/advent_of_code/advent_2021/day8/input8"

for x,y in [x.split('|') for x in open(0)]:  # split signal and output
    l = {len(s): set(s) for s in x.split()}    # get number of segments

    n = ''
    for o in map(set, y.split()):
        print(type(o), o) # loop over output digits
        match len(o), len(o&l[4]), len(o&l[2]):  # mask with known digits
            case 2,_,_: n += '1'
            case 3,_,_: n += '7'
            case 4,_,_: n += '4'
            case 7,_,_: n += '8'
            case 5,2,_: n += '2'
            case 5,3,1: n += '5'
            case 5,3,2: n += '3'
            case 6,4,_: n += '9'
            case 6,3,1: n += '6'
            case 6,3,2: n += '0'
    s += int(n)

print(s)
