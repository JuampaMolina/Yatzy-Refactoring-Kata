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
    def small_straight(*dices):
        orderedList = sorted(list(dices))
        score = 0
        smallest = 1
        for dice in orderedList:  # while
            if dice == smallest and orderedList.count(dice) == 1:
                score += dice
                smallest += 1
            else:
                return 0
        return score

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
    def full_house(*dices):
        score = 0
        if Yatzy.pair(*dices) and Yatzy.three_of_a_kind(*dices):
            score = Yatzy.pair(*dices) + Yatzy.three_of_a_kind(*dices)
        return score
