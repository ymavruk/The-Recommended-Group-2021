import pandas as pd
import numpy as np


class ExpGenerator:

    def generateExp(self, df, privacy=True):
        indeces = df.index.values.ravel()
        for col in df:
            ratings = df[col].values.ravel()
            minG = min(ratings)
            maxG = max(ratings)
            lowNum = self.calculateNumOfLows(ratings)
            if privacy:
                if lowNum < 3 and maxG >= 4:
                    print("The majority of the group will love the game: {}.".format(col))
                elif lowNum == 3 and maxG >= 4 and minG > 3:
                    print("The majority of the group will like {}, some will love it!".format(col))
                elif minG > 2 and maxG < 4:
                    print("The majority of the group will like {}.".format(col))
                elif lowNum >= 3 and maxG >= 4:
                    print("{} is not the top choice for majority, but some will love it. Why not give it a try?".format(
                        col))
                elif lowNum == 1 and maxG > 3.8:
                    print(
                        "One person might not like the game, but the majority of the group will love the game: {}.".format(
                            col))
            else:
                lowUser = np.where(ratings == minG)
                highUser = np.where(ratings == maxG)
                highestUser = df.index.values.ravel()[highUser[0]][0]
                for i, val in enumerate(ratings):
                    if val < 3.5:
                        print(
                            "Hey {}, you might not like {}, but your friend {} loves it, so maybe give it a try.".format(
                                indeces[i], col, highestUser))
                    elif val >= 3.5:
                        print("Hey {}, you will love {}".format(indeces[i], col))

    def calculateNumOfLows(self, ratings):
        count = 0
        for val in ratings:
            if val < 3.5:
                count += 1
        return count

    def test(self):
        users = [11, 22, 33, 44, 55]
        games = ["Fallout", "Raft", "Fall Guys", "Oregon", "Lemon Head"]
        testdf = pd.DataFrame(np.random.uniform(low=2, high=5.5, size=(5, 5)), index=users, columns=games)
        print(testdf)
        return testdf


if __name__ == "__main__":
    exp = ExpGenerator()
    testdf = exp.test()
    exp.generateExp(testdf, privacy=False)
