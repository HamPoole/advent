with open(file="/home/urthor/projects/advent_of_code/advent_2021/day3/input/input",
          mode='r') as input1:
    binary = input1.readlines()

cleaned_bin = [x[:-1] for x in binary]

# print(cleaned_bin[:5])

result_array = [0 for x in range(len(cleaned_bin[0]))]

print(len(result_array))

print(len(cleaned_bin))

for index in range(len(cleaned_bin[0])):

    for number in cleaned_bin:
        result_array[index] += int(number[index])

print(result_array)

final_array = list(result_array)

gamma = [str(int(x - 499 > 0)) for x in list(final_array)]
print(gamma)

str_gamma = int("".join(gamma))
print(str_gamma)
val = bin(str_gamma)
print(val, type(val))
epsi = [str(1 - int(x - 499 > 0)) for x in list(final_array)]

str_epsi = int("".join(epsi))
print(str_epsi)
val2 = bin(str_epsi)
print(val2, type(val2))

print(1300*2795)