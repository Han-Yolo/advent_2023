import re

# result = 0
# with open("advent9.data", "r") as file:
#     for line in file:
#         seq = [[int(n) for n in re.findall(r"[\d-]+", line)]]
#         while not all([n == 0 for n in seq[-1]]):
#             new_len = len(seq[-1]) - 1
#             new_seq = [0] * new_len
#             for i in range(new_len):
#                 new_seq[i] = seq[-1][i + 1] - seq[-1][i]
#             seq.append(new_seq)

#         for i in range(len(seq) - 2, -1, -1):
#             seq[i].append(seq[i][-1] + seq[i + 1][-1])
#         result += seq[0][-1]

# print(result)


result = 0
with open("advent9.data", "r") as file:
    for line in file:
        seq = [[int(n) for n in re.findall(r"[\d-]+", line)]]
        while not all([n == 0 for n in seq[-1]]):
            new_len = len(seq[-1]) - 1
            new_seq = [0] * new_len
            for i in range(new_len):
                new_seq[i] = seq[-1][i + 1] - seq[-1][i]
            seq.append(new_seq)

        extr = 0
        for i in range(len(seq) - 2, -1, -1):
            extr = seq[i][0] - extr
        result += extr

print(result)
