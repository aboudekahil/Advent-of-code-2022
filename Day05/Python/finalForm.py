def SanitizeMove(move: str):
    moveList = move.split(' ')

    for i in moveList:
        if not i.isnumeric():
            moveList.remove(i)

    return list(map(int, moveList))


def moveStuff(stacks: list[list[str]], move: str):
    if (move == ''):
        return

    moveList = SanitizeMove(move)

    for _ in range(min(moveList[0], len(stacks[moveList[1] - 1]))):
        stacks[moveList[2] - 1].append(stacks[moveList[1] - 1].pop())


def moveStuff9001(stacks: list[list[str]], move: str):
    if (move == ''): return

    moveList = SanitizeMove(move)

    stacks[moveList[2] -
           1] += stacks[moveList[1] -
                        1][max(0,
                               len(stacks[moveList[1] - 1]) - moveList[0]):]

    for _ in range(min(moveList[0], len(stacks[moveList[1] - 1]))):
        stacks[moveList[1] - 1].pop()


with open('./Day05/input.txt', 'r') as file:
    cratesAndMoves = file.read().split(' 1   2   3   4   5   6   7   8   9 ',
                                       1)

crates = cratesAndMoves[0].splitlines()
moves = cratesAndMoves[-1].splitlines()

stacks = [[] for _ in range(9)]

for i in crates:
    for j in range(0, len(i), 4):
        if (i[j:j + 4].strip() != str()):
            stacks[j // 4].append(i[j + 1])

stacks = [i[::-1] for i in stacks]

for move in moves:
    # # part 1
    # moveStuff(stacks, move)

    # part 2
    moveStuff9001(stacks, move)

[print(stack[-1], end="") for stack in stacks]
