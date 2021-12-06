
with open(file="/home/urthor/projects/advent_of_code/advent_2021/day4/input/input",
          mode='r') as input1:
    binary = input1.readlines()



# Track all rows and columns of each

print(type(binary))
print(list(binary)[2:])

calls = [int(x) for x in binary[0].split(",")]
after_input = list(binary)[2:]




nums = [int(x) for x in after_input.strip().split(",")]

print(nums[:10])