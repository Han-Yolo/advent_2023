import re

with open("advent3.data", "r") as file:
    lines = file.readlines()

NUM_LINES = len(lines)
LINE_LEN = 140

# valid = [[False for _ in range(LINE_LEN)] for _ in range(NUM_LINES)]
# notSymbolPattern = re.compile(r"[0-9\.]")
# for i in range(NUM_LINES):
#     for j in range(LINE_LEN):
#         if not notSymbolPattern.match(lines[i][j]):
#             for ii in range(i - 1, i + 2):
#                 for jj in range(j - 1, j + 2):
#                     if ii > 0 or ii < NUM_LINES - 1 or jj > 0 or jj < LINE_LEN - 1:
#                         valid[ii][jj] = True

# result = 0
# numberPattern = re.compile(r"[0-9]+")
# for i in range(NUM_LINES):
#     for match in re.finditer(numberPattern, lines[i]):
#         if any(valid[i][match.start() : match.end()]):
#             result += int(lines[i][match.start() : match.end()])

# print(result)

result = 0
for i in range(NUM_LINES):
    for gear in re.finditer(r"\*", lines[i]):
        j = gear.start()
        nums = []
        for ii in range(i - 1, i + 2):
            if ii >= 0 and ii < NUM_LINES:
                for number in re.finditer(r"[0-9]+", lines[ii]):
                    if number.start() <= j + 1 and number.end() >= j:
                        nums.append(int(lines[ii][number.start() : number.end()]))
        if len(nums) == 2:
            result += nums[0] * nums[1]

print(result)
