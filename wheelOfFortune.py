#!/bash/bin/python2

def winner(candidates):
    if len(candidates) > 3:
        return False

    bestScore = 0
    TempWinner = ""

    for candidate in candidates:
        if len(candidate) != 2 or len(candidate["scores"]) > 2 or len(candidate["scores"]) < 1:
            return False

        result = sum(candidate["scores"])

        if result > bestScore and result <= 100:
            TempWinner = candidate["name"]
            bestScore = result

    if bestScore > 0:
        return TempWinner
    else:
        return False


c1 = {"name": "Bob", "scores": [10, 65]}
c2 = {"name": "Bill", "scores": [90, 15]}
c3 = {"name": "Charlie", "scores": [40, 55]}
print ("And the winner is %s" %(winner([c1, c2, c3])))
