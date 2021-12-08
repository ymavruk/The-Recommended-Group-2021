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
                start ="The {} game is recommended ".format(col)
                for i, val in enumerate(ratings):
                    # print(col)
                    # print(val)

                    if val < 3:
                        lowRatedUsers.append(indeces[i])

                        # print(
                        #     "Hey {}, you might not like {}, but your friend {} loves it, so maybe give it a try.".format(
                        #         indeces[i], col, highestUser))
                    if val >= 3:
                        highRatedUsers.append(indeces[i])
                        # print("Hey {}, you will love {}".format(indeces[i], col))

                # highRStr = str(highRatedUsers).replace("[", "").replace("]", "")
                # lowRStr = str(lowRatedUsers).replace("[", "").replace("]", "")
                # if len(lowRatedUsers) == 0:
                #     print("{} is great because you all, ".format(col) + highRStr + ", will like game.")
                # elif len(highRatedUsers) == 0:
                #     print("{} is not a right choice because you all, ".format(col) +
                #           lowRStr + ", will not like the game.")
                # elif len(lowRatedUsers) > len(highRatedUsers):
                #     print("{} is not a right choice because the group members: ".format(col) +
                #           lowRStr + " will not like the game, but the group members: " +
                #           highRStr + " will like the game.")
                # elif len(lowRatedUsers) < len(highRatedUsers):
                #     print("{} is a good choice because the group members: ".format(col) +
                #           highRStr + " will like the game, but the group members: " +
                #           lowRStr + " will not like the game.")

                print("{} is recommended because it has a group score of {} due to the highest rating determined for "
                      "user with id {}. Also, it avoids misery within the group with a threshold of {} determined for "
                      "user with id {}.".format(col, round(maxG, 2), highestUser, round(minG, 2), lowestUser))

    def calculateNumOfLows(self, ratings):
        count = 0
        for val in ratings:
            if val < 3.75:
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
    exp.generateExp(testdf, privacy=True)
