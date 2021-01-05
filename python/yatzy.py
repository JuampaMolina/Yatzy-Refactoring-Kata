class Yatzy:

    @staticmethod
    def chance(*dices):
        total = 0
        for dice in dices:
            total += dice
        return total

    @staticmethod
    def yatzy(*dices):
        firstDice = dices[0]
        for dice in dices:
            if dice != firstDice:
                return 0
        return 50

    @staticmethod
    def ones(*dices):
        sum = 0
        for dice in dices:
            if dice == 1:
                sum += dice
        return sum

    @staticmethod
    def twos(*dices):
        sum = 0
        for dice in dices:
            if dice == 2:
                sum += dice
        return sum

    @staticmethod
    def threes(*dices):
        sum = 0
        for dice in dices:
            if dice == 3:
                sum += dice
        return sum

    @staticmethod
    def fours(*dices):
        sum = 0
        for dice in dices:
            if dice == 4:
                sum += dice
        return sum

    @staticmethod
    def fives(*dices):
        sum = 0
        for dice in dices:
            if dice == 5:
                sum += dice
        return sum

    @staticmethod
    def sixes(*dices):
        sum = 0
        for dice in dices:
            if dice == 6:
                sum += dice
        return sum

    @staticmethod
    def pair(*dices):
        score = 0
        for dice in dices:
            if dices.count(dice) >= 2 and (dice * 2) > score:
                score = dice * 2
        return score

    @staticmethod
    def two_pairs(*dices):
        score = 0
        havePair = []
        for dice in dices:
            if dices.count(dice) >= 2 and dice not in havePair:
                score += dice * 2
                havePair.append(dice)
        if len(havePair) >= 2:
            return score
        else:
            return 0

    @staticmethod
    def three_of_a_kind(*dices):
        score = 0
        for dice in dices:
            if dices.count(dice) >= 3 and (dice * 3) > score:
                score = dice * 3
        return score

    @staticmethod
    def four_of_a_kind(*dices):
        score = 0
        for dice in dices:
            if dices.count(dice) >= 4 and (dice * 4) > score:
                score = dice * 4
        return score

    @staticmethod
    def small_straight(d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[0] == 1 and
            tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
                tallies[4] == 1):
            return 15
        return 0

    @staticmethod
    def large_straight(*dices):
        orderedList = sorted(list(dices))
        score = 0
        smallest = 2
        for dice in orderedList:  # while
            if dice == smallest and orderedList.count(dice) == 1:
                score += dice
                smallest += 1
            else:
                return 0
        return score

    @staticmethod
    def full_house(d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2):
                _2 = True
                _2_at = i+1

        for i in range(6):
            if (tallies[i] == 3):
                _3 = True
                _3_at = i+1

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0


if __name__ == "__main__":
    assert 0 == Yatzy.large_straight(1, 2, 2, 4, 5)
