with open("advent11.data", "r") as file:
    lines = [line.strip("\n") for line in file.readlines()]

row_empty = ["#" not in line for line in lines]
col_empty = [True] * len(lines[0])
for col in range(len(lines[0])):
    for row in range(len(lines)):
        if lines[row][col] == "#":
            col_empty[col] = False
            break

# Part 1
# exp_val = 1

# Part 2
exp_val = 999999

stars = []
row_exp = 0
for row, line in enumerate(lines):
    if row_empty[row]:
        row_exp += exp_val
    else:
        col_exp = 0
        for col, char in enumerate(line):
            if col_empty[col]:
                col_exp += exp_val
            elif char == "#":
                stars.append((row + row_exp, col + col_exp))

result = 0
for sta in range(len(stars)):
    for stb in range(sta + 1, len(stars)):
        result += abs(stars[sta][0] - stars[stb][0]) + abs(
            stars[sta][1] - stars[stb][1]
        )
print(result)
