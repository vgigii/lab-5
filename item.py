class Item:
    def __init__(self, name):
        self.name = name

    def use(self, player):
        print(player + " uses " + self.name)

