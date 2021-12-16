with open(file="/home/urthor/projects/advent_of_code/advent_2021/day13/input13") as myinput:
    input_file = myinput.readlines()

cleaned_matrix = [x[:-1] for x in input_file]

for index in range(len(cleaned_matrix)):
    cleaned_matrix[index] = list((map(int, cleaned_matrix[index])))


print(cleaned_matrix)