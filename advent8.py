import re
import functools

with open("advent8.data", "r") as file:
    lines = file.readlines()

instr = [0 if char == "L" else 1 for char in re.findall(r"[LR]", lines[0])]
print(instr)

nodes = {}
for line in lines[2:]:
    parts = re.findall(r"[A-Z0-9]{3}", line)
    nodes[parts[0]] = (parts[1], parts[2])
print(nodes)

# node = "AAA"
# i = 0
# count = 0
# while node != "ZZZ":
#     node = nodes[node][instr[i]]
#     i = (i + 1) % len(instr)
#     count += 1
# print(count)


starts = list(filter(lambda node: node[2] == "A", nodes.keys()))
print(starts)

counts = []
for start in starts:
    pos = start
    i = 0
    count = 0
    while pos[2] != "Z":
        pos = nodes[pos][instr[i]]
        i = (i + 1) % len(instr)
        count += 1
    counts.append(count)


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    lcm = (x * y) // gcd(x, y)
    return lcm


print(functools.reduce(lcm, counts))
