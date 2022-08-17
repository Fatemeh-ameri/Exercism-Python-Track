"""Your task is to write methods that return the highest score from the list, 
the last added score and the three highest scores."""

class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return max(self.scores)

    def personal_top_three(self):
        temp = self.scores [:]
        for i in temp:
            if len(temp) >= 3:
                temp.sort()
                temp.reverse()
                return temp [0:3]
            elif 0 < len(temp) and len(temp) < 3:
                temp.sort()
                temp.reverse()
                return temp 
            else:
                return temp()



