class SingleObject():
    instance = None

    def __init__(self, player_1, score_1, player_2, score_2):
        if SingleObject.instance != None:
            raise Exception("This is singleton class")
        else:
            SingleObject.instance = self
            self.player1 = player_1
            self.player2 = player_2
            self.score1 = score_1
            self.score2 = score_2

    def show_player1(self):
        print("Player 1 is {p1}".format(p1=self.player1))

    def show_player2(self):
        print("Player 2 is {p2}".format(p2=self.player2))

    def show_score_player1(self):
        print("Player 1 get {s1}".format(s1=self.score1))

    def show_score_player2(self):
        print("Player 2 get {s2}".format(s2=self.score2))

    def show_result(self):
        if self.score1 > self.score2:
            print("Player {win} is WINNER !!!".format(win=self.player1))
        elif self.score1 < self.score2:
            print("Player {win} is WINNER !!!".format(win=self.player2))
        elif self.score1 == self.score2:
            print("This game is DRAW")

if __name__ == '__main__':
    game1 = SingleObject('A', 1, 'B', 2)
    game1.show_result()

    game2 = SingleObject('C', 2, 'D', 1)
    game2.show_result()