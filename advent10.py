import re

with open("advent10.data", "r") as file:
    lines = [line.strip("\n") for line in file.readlines()]

for row, line in enumerate(lines):
    col = line.find("S")
    if col >= 0:
        start = {"row": row, "col": col}
        break

prev = start.copy()
pos = start.copy()
pos["row"] -= 1

# count = 1
# while pos != start:
#         next = pos.copy()
#         match lines[pos["row"]][pos["col"]]:
#             case "|":
#                 if pos["row"] - 1 != prev["row"]:
#                     next["row"] -= 1
#                 else:
#                     next["row"] += 1
#             case "-":
#                 if pos["col"] - 1 != prev["col"]:
#                     next["col"] -= 1
#                 else:
#                     next["col"] += 1
#             case "L":
#                 if pos["row"] - 1 != prev["row"]:
#                     next["row"] -= 1
#                 else:
#                     next["col"] += 1
#             case "J":
#                 if pos["row"] - 1 != prev["row"]:
#                     next["row"] -= 1
#                 else:
#                     next["col"] -= 1
#             case "7":
#                 if pos["row"] + 1 != prev["row"]:
#                     next["row"] += 1
#                 else:
#                     next["col"] -= 1
#             case "F":
#                 if pos["row"] + 1 != prev["row"]:
#                     next["row"] += 1
#                 else:
#                     next["col"] += 1
#         prev = pos
#         pos = next
#         count += 1
# 
# print(count // 2)

inner = "R"
marks = [[0] * len(lines[0]) for _ in range(len(lines))]
marks[start["row"]][start["col"]] = 3
while pos != start:
        next = pos.copy()
        marks[pos["row"]][pos["col"]] = 3
        match lines[pos["row"]][pos["col"]]:
            case "|":
                if pos["row"] - 1 != prev["row"]:
                    next["row"] -= 1
                else:
                    next["row"] += 1
                if inner == "R" and 
                        
            case "-":
                if pos["col"] - 1 != prev["col"]:
                    next["col"] -= 1
                else:
                    next["col"] += 1
            case "L":
                if pos["row"] - 1 != prev["row"]:
                    next["row"] -= 1
                else:
                    next["col"] += 1
            case "J":
                if pos["row"] - 1 != prev["row"]:
                    next["row"] -= 1
                else:
                    next["col"] -= 1
            case "7":
                if pos["row"] + 1 != prev["row"]:
                    next["row"] += 1
                else:
                    next["col"] -= 1
            case "F":
                if pos["row"] + 1 != prev["row"]:
                    next["row"] += 1
                else:
                    next["col"] += 1
        prev = pos
        pos = next

with open("advent10.out", "w") as out:
    for mark in marks:
        for m in mark:
            out.write(str(m))
        out.write("\n")