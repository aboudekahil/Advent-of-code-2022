import functools


def fetchPriority(letter):
    if (ord('a') <= ord(letter) <= ord('z')):
        return ord(letter) - ord('a') + 1

    if (ord('A') <= ord(letter) <= ord('Z')):
        return ord(letter) - ord('A') + 27


def fetchCommonLetter(*toFind) -> str:
    toFind = toFind[0]

    reduced = [set(i) for i in toFind]

    reduced = functools.reduce(lambda a, b: a & b, reduced)

    return reduced.pop()


with open('./Day03/input.txt', 'r') as file:
    sackList = file.read().splitlines()

# # part 1
# sum = 0
# for sack in sackList:
#     letter = fetchCommonLetter(sack[:len(sack) // 2], sack[len(sack) // 2:])
#     sum += fetchPriority(letter)

# print(sum)

# part 2

sum = 0
for i in range(0, len(sackList), 3):
    common = fetchCommonLetter(sackList[i:i+3])
    sum += fetchPriority(common)

print(sum)
