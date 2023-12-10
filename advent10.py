with open("advent10.data", "r") as file:
    lines = [line.strip("\n") for line in file.readlines()]

for row, line in enumerate(lines):
    col = line.find("S")
    if col >= 0:
        start = {"row": row, "col": col}
        break

prev = start.copy()
pos = start.copy()
count = 0


def move():
    global prev
    global pos
    global count
    next = pos.copy()
    match lines[pos["row"]["col"]]:
        case "|":
            next["row"] = (
                pos["row"] - 1 if pos["row"] - 1 != prev["row"] else pos["row"] + 1
            )

    for row in range(max(pos["row"] - 1, 0), min(pos["row"] + 2, len(lines))):
        for col in range(max(pos["col"] - 1, 0), min(pos["col"] + 2, len(lines[0]))):
            found = False
            match lines[row][col]:
                case "|":
                    if col == pos["col"]:
                        found = True
                case "-":
                    if row == pos["row"]:
                        found = True
                case "L":
                    if (row == pos["row"] and col + 1 == pos["col"]) or (
                        row - 1 == pos["row"] and col == pos["col"]
                    ):
                        found = True
                case "J":
                    if (row == pos["row"] and col - 1 == pos["col"]) or (
                        row - 1 == pos["row"] and col == pos["col"]
                    ):
                        found = True
                case "7":
                    if (row == pos["row"] and col - 1 == pos["col"]) or (
                        row + 1 == pos["row"] and col == pos["col"]
                    ):
                        found = True
                case "F":
                    if (row == pos["row"] and col + 1 == pos["col"]) or (
                        row + 1 == pos["row"] and col == pos["col"]
                    ):
                        found = True
                case "S":
                    if row == pos["row"] or col == pos["col"]:
                        found = True

            if found:
                next = {"row": row, "col": col}
                if next != prev and next != pos:
                    prev = pos
                    pos = next
                    count += 1
                    print(pos)
                    return


print(start)
move()
while pos != start:
    move()

print(count // 2)
