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


marks = [[0] * len(lines[0]) for _ in range(len(lines))]
marks[start["row"]][start["col"]] = 3


def setMark(row, col):
    global marks
    if row >= 0 and row < len(lines) and col >= 0 and col < len(lines[0]):
        if marks[row][col] == 0:
            marks[row][col] = 1


inner = "L"
setMark(start["row"], start["col"] - 1)

while pos != start:
    next = pos.copy()
    marks[pos["row"]][pos["col"]] = 3
    match lines[pos["row"]][pos["col"]]:
        case "|":
            if pos["row"] - 1 != prev["row"]:
                next["row"] -= 1
            else:
                next["row"] += 1

            if inner == "R":
                setMark(pos["row"], pos["col"] + 1)
            elif inner == "L":
                setMark(pos["row"], pos["col"] - 1)

        case "-":
            if pos["col"] - 1 != prev["col"]:
                next["col"] -= 1
            else:
                next["col"] += 1

            if inner == "R":
                setMark(pos["row"] + 1, pos["col"])
            elif inner == "L":
                setMark(pos["row"] - 1, pos["col"])

        case "L":
            if pos["row"] - 1 != prev["row"]:
                next["row"] -= 1
            else:
                next["col"] += 1

            match inner:
                case "R":
                    inner = "U"
                case "U":
                    inner = "R"
                case "L":
                    inner = "D"
                case "D":
                    inner = "L"

            if inner == "L" or inner == "D":
                setMark(pos["row"], pos["col"] - 1)
                setMark(pos["row"] + 1, pos["col"] - 1)
                setMark(pos["row"] + 1, pos["col"])

        case "J":
            if pos["row"] - 1 != prev["row"]:
                next["row"] -= 1
            else:
                next["col"] -= 1

            match inner:
                case "R":
                    inner = "D"
                case "D":
                    inner = "R"
                case "L":
                    inner = "U"
                case "U":
                    inner = "L"

            if inner == "R" or inner == "D":
                setMark(pos["row"], pos["col"] + 1)
                setMark(pos["row"] + 1, pos["col"] + 1)
                setMark(pos["row"] + 1, pos["col"])

        case "7":
            if pos["row"] + 1 != prev["row"]:
                next["row"] += 1
            else:
                next["col"] -= 1

            match inner:
                case "U":
                    inner = "R"
                case "R":
                    inner = "U"
                case "D":
                    inner = "L"
                case "L":
                    inner = "D"

            if inner == "U" or inner == "R":
                setMark(pos["row"] - 1, pos["col"])
                setMark(pos["row"] - 1, pos["col"] + 1)
                setMark(pos["row"], pos["col"] + 1)

        case "F":
            if pos["row"] + 1 != prev["row"]:
                next["row"] += 1
            else:
                next["col"] += 1

            match inner:
                case "U":
                    inner = "L"
                case "L":
                    inner = "U"
                case "D":
                    inner = "R"
                case "R":
                    inner = "D"

            if inner == "U" or inner == "L":
                setMark(pos["row"] - 1, pos["col"])
                setMark(pos["row"] - 1, pos["col"] - 1)
                setMark(pos["row"], pos["col"] - 1)

    prev = pos
    pos = next

count = 0
for line in marks:
    active = False
    for m in line:
        if m == 1:
            active = True
            count += 1
        elif m == 0 and active:
            count += 1
        else:
            active = False

print(count)


# with open("advent10.out", "w") as out:
#     for mark in marks:
#         for m in mark:
#             out.write(str(m))
#         out.write("\n")
