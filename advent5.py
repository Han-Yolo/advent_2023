import re

with open("advent5.data", "r") as file:
    lines = file.readlines()

# seeds = [int(n) for n in re.findall(r"\d+", lines[0])]
# print("seeds", seeds)
# maps = [
#     "seed-to-soil",
#     "soil-to-fertilizer",
#     "fertilizer-to-water",
#     "water-to-light",
#     "light-to-temperature",
#     "temperature-to-humidity",
#     "humidity-to-location",
# ]
# i = 0
# for map in maps:
#     while not map in lines[i]:
#         i += 1
#         continue
#     i += 1
#     ms = []
#     while i < len(lines):
#         m = [int(n) for n in re.findall(r"\d+", lines[i])]
#         i += 1
#         if len(m) == 0:
#             break
#         ms.append(m)
#     print(map, ms)
#     for j, seed in enumerate(seeds):
#         for m in ms:
#             if seed >= m[1] and seed < m[1] + m[2]:
#                 seeds[j] = seed + m[0] - m[1]
#                 break
#     print("seeds", seeds)

# print(min(seeds))

nums = [int(n) for n in re.findall(r"\d+", lines[0])]
pairs = []
for k in range(0, len(nums), 2):
    pairs.append((nums[k], nums[k] + nums[k + 1]))
print(pairs)
maps = [
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
]
i = 0
mss = []
for map in maps:
    while not map in lines[i]:
        i += 1
        continue
    i += 1
    ms = []
    while i < len(lines):
        nums = [int(n) for n in re.findall(r"\d+", lines[i])]
        i += 1
        if len(nums) == 0:
            break
        m = (nums[1], nums[1] + nums[2], nums[0] - nums[1])
        ms.append(m)
    print(map, ms)
    mss.append(ms)

for ms in mss:
    newPairs = []
    for pair in pairs:
        pfrags = [pair]
        for m in ms:
            # m[0] start, m[1] end, m[2] mod
            toRemove = 0
            for pi in range(len(pfrags)):
                if pfrags[pi][0] < m[1] and pfrags[pi][1] > m[0]:
                    newStart = max(pfrags[pi][0], m[0]) + m[2]
                    newEnd = min(pfrags[pi][1], m[1]) + m[2]
                    newPairs.append((newStart, newEnd))
                    toRemove += 1
                    if pfrags[pi][0] < m[0]:
                        pfrags.append((pfrags[pi][0], m[0]))
                    if pfrags[pi][1] > m[1]:
                        pfrags.append((m[1], pfrags[pi][1]))
            for _ in range(toRemove):
                pfrags.pop(0)
        newPairs += pfrags
    pairs = newPairs

print(min([pair[0] for pair in pairs]))
