myScore = 0

with open('./Day02/input.txt', 'r') as file:
    rounds = file.read().split('\n')


def getPoints(move, comparedTo):
    return ord(move) - ord(comparedTo)


def getScore(round):
    if round == '':
        return 0

    playerPoints = getPoints(round[-1], 'X') + 1
    oppPoints = getPoints(round[0], 'A') + 1

    score = playerPoints
    if (playerPoints == oppPoints):  # tie
        score += 3

    elif ((playerPoints == 1 and oppPoints == 3)
          or (playerPoints == 2 and oppPoints == 1)
          or (playerPoints == 3 and oppPoints == 2)):  # we win!
        score += 6

    return score


def getScore2(round):
    if (round == ''):
        return 0

    win = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    lose = {'A': 'Z', 'B': 'X', 'C': 'Y'}

    if (round[-1] == 'Y'):
        return getPoints(round[0], 'A') + 1 + 3

    elif (round[-1] == 'Z'):
        return getPoints(win[round[0]], 'X') + 1 + 6

    return getPoints(lose[round[0]], 'X') + 1


# # part1 score
# score = sum(map(getScore, rounds))

# part 2
print(sum(map(getScore2, rounds)))