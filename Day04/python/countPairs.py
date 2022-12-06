def doesFullyContain(pair: str) -> bool:
    numLists = [
        list(range(int(i.split('-')[0]),
                   int(i.split('-')[-1]) + 1)) for i in pair.split(',')
    ]

    toCheck = 0 if (len(numLists[0]) < len(numLists[-1])) else -1
    other = abs(toCheck) - 1

    return numLists[toCheck][0] >= numLists[other][0] and numLists[toCheck][
        -1] <= numLists[other][-1]


def doesOverlap(pair: str) -> bool:
    numLists = [
        list(range(int(i.split('-')[0]),
                   int(i.split('-')[-1]) + 1)) for i in pair.split(',')
    ]

    toCheck = 0 if (len(numLists[0]) < len(numLists[-1])) else -1
    other = abs(toCheck) - 1

    return max(numLists[toCheck]) in numLists[other] or min(
        numLists[toCheck]) in numLists[other]


with open('./Day04/input.txt', 'r') as file:
    pairs = file.read().splitlines()

# # part 1
# print(sum(map(doesFullyContain, pairs)))

# part 2
print(sum(map(doesOverlap, pairs)))
