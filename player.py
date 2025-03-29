class Player:
    def __init__(self):
        self.health = 100
        self.inventory = []  
        self.score = 0
        self.position = [0, 0]  

    def move(self, direction):
        if direction == "left":
            self.position[0] -= 1
        elif direction == "right":
            self.position[0] += 1
        elif direction == "up":
            self.position[1] += 1
        elif direction == "down":
            self.position[1] -= 1
        print("Player moved to " + str(self.position))

    def attack(self, enemy):
        print("Player attacks! " + str(enemy))
        enemy.take_damage(10)

    def take_damage(self, amount):
        self.health -= amount
        print("Player takes " + str(amount) + " damage! Health: " + str(self.health))

    def collect_item(self, item):
        self.inventory.append(item)
        print("Player collects " + item.name)

    def use_item(self, item):
        if item in self.inventory:
            print("Player uses " + item.name)
            self.inventory.remove(item)
        else:
            print(item.name + " not in inventory!")

    def show_inventory(self):
        if not self.inventory:
            print("Inventory is empty!")
        else:
            print("Inventory: ")
            for item in self.inventory:
                print(item.name)

