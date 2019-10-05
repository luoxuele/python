class Master():
    def __init__(self):
        self.kongfu = "降龙十八掌"

    def play(self):
        print("我会%s" % self.kongfu)
        print(self)


dashi = Master()
dashi.play()


class Prentice(Master):
    pass

tudi = Prentice()
tudi.play()
