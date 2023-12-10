import re
import math

with open("advent6.data", "r") as file:
    lines = file.readlines()

# time = [int(t) for t in re.findall(r"\d+", lines[0])]
# distance = [int(d) for d in re.findall(r"\d+", lines[1])]

# result = 1
# for i in range(len(time)):
#     square = math.sqrt((time[i] ** 2) - (4 * distance[i]))
#     sol1 = (time[i] + square) / 2
#     sol2 = (time[i] - square) / 2
#     start = int(sol2) + 1 if sol2.is_integer() else math.ceil(sol2)
#     end = int(sol1) if sol1.is_integer() else math.ceil(sol1)
#     result *= end - start

# print(result)

time = int("".join(re.findall(r"\d+", lines[0])))
distance = int("".join(re.findall(r"\d+", lines[1])))

square = math.sqrt((time**2) - (4 * distance))
sol1 = (time + square) / 2
sol2 = (time - square) / 2
start = int(sol2) + 1 if sol2.is_integer() else math.ceil(sol2)
end = int(sol1) if sol1.is_integer() else math.ceil(sol1)
result = end - start

print(result)
