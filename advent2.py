import re
import functools
import operator

# result = 0
# with open("advent2.data", "r") as file:
#     for i, line in enumerate(file.readlines()):
#         possible = True
#         for match in re.findall(r"(\d+) red", line):
#             if int(match) > 12:
#                 possible = False
#         for match in re.findall(r"(\d+) green", line):
#             if int(match) > 13:
#                 possible = False
#         for match in re.findall(r"(\d+) blue", line):
#             if int(match) > 14:
#                 possible = False
#         if possible:
#             result += i + 1
# print(result)

result = 0
with open("advent2.data", "r") as file:
    for line in file.readlines():
        m = [0, 0, 0]
        for match in re.findall(r"(\d+) red", line):
            m[0] = max(m[0], int(match))
        for match in re.findall(r"(\d+) green", line):
            m[1] = max(m[1], int(match))
        for match in re.findall(r"(\d+) blue", line):
            m[2] = max(m[2], int(match))
        result += functools.reduce(operator.mul, m)
print(result)
