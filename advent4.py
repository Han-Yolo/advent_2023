import re

# result = 0
# with open("advent4.data", "r") as file:
#     for line in file:
#         parts = line.split(":")[1].split("|")
#         winning = re.findall(r"\d+", parts[0])
#         having = re.findall(r"\d+", parts[1])
#         count = sum([h in winning for h in having])
#         if count > 0:
#             result += 2 ** (count - 1)

# print(result)


with open("advent4.data", "r") as file:
    lines = file.readlines()

cards = [1] * len(lines)
result = 0
for i, line in enumerate(lines):
    result += cards[i]
    parts = line.split(":")[1].split("|")
    winning = re.findall(r"\d+", parts[0])
    having = re.findall(r"\d+", parts[1])
    count = sum([h in winning for h in having])
    for j in range(i + 1, min(i + count + 1, len(lines))):
        cards[j] += cards[i]

print(result)
