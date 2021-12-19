from collections import Counter

tpl, _, *rules = open("/home/urthor/projects/advent_of_code/advent_2021/day14/input14").read().split('\n')
rules = dict(r.split(" -> ") for r in rules)

pairs = Counter(map(str.__add__, tpl, tpl[1:]))
chars = Counter(tpl)

print(pairs)
print(chars)
print(tpl)

print(pairs.copy().items())

for index in range(40):
    for (a, b), c in pairs.copy().items():
        print(a, b, c)
        x = rules[a + b]
        pairs[a + b] -= c
        pairs[a + x] += c
        pairs[x + b] += c
        chars[x] += c

# For each pair:
# Copy the current number of pairs
# Take all the values from that pair, then add those values to the pairs "pair first + result"
# Trick in efficient use of counters is really difficult to get.


print(max(chars.values()) - min(chars.values()))

print(max(chars.values()) - min(chars.values()), max(chars.values()), min(chars.values()))

print(max(pairs.values()) - min(pairs.values()))
print(chars)
print(pairs)