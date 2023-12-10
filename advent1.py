import re

numbers = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
regex = r"(?=(\d|" + r"|".join(numbers) + r"))"


def extract(s: str) -> str:
    if s.isdigit():
        return s
    else:
        return str(numbers.index(s))


with open("advent1.data", "r") as file:
    sum = 0
    for line in file.readlines():
        matches = re.findall(regex, line)
        if matches:
            sum += int(extract(matches[0]) + extract(matches[-1]))

print(sum)
