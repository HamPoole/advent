import operator

with open(file="/home/urthor/projects/advent_of_code/advent_2021/day3/input/input",
          mode='r') as input1:
    binary = input1.readlines()

data = [x[:-1] for x in binary]

data = ['00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010',
        '01010']

length = len(data)

# print(cleaned_bin[:5])

result_array = [0 for x in range(len(data[0]))]

print(len(result_array))

print(len(data))

for index in range(len(data[0])):

    for number in data:
        result_array[index] += int(number[index])

final_array = list(result_array)

gamma = [str(int(x - length / 2 > 0)) for x in list(final_array)]

str_gamma = int("".join(gamma))

val = bin(str_gamma)
epsi = [str(1 - int(x - length / 2 > 0)) for x in list(final_array)]

str_epsi = int("".join(epsi))
val2 = bin(str_epsi)

print(gamma, epsi, str_gamma, str_epsi)
print(1300 * 2795)

for index in range(len(data[0])):

    for number in data:
        result_array[index] += int(number[index])

# 101011101011
# 10100010100

oxy_array = list(data)
prev_oxy = oxy_array

print(str_gamma, type(str_gamma))

max_count_similar = 0

oxy_gen = ''
co2 = ''


def calc_oxco2(operator):
    max_count_similar = 0

    bin_and = str_gamma & int(number)
    count_similar = 0

    for digit in str(bin_and):
        if digit != '1':
            count_similar += 1
        else:
            break

    if operator(count_similar, max_count_similar):
        max_count_similar = count_similar
        co2 = number


print(oxy_gen, 'here oxy')
print(co2, 'here co2')

# 001111100111
# 100000000101

print(0b100000000101 * 0b001111100111)
