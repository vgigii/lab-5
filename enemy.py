import random

class Enemy:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage
        self.position = [random.randint(1, 5), random.randint(1, 5)]  

    def move(self, player_position):
        if self.position[0] < player_position[0]:
            self.position[0] += 1
        elif self.position[0] > player_position[0]:
            self.position[0] -= 1

        if self.position[1] < player_position[1]:
            self.position[1] += 1
        elif self.position[1] > player_position[1]:
            self.position[1] -= 1

        print("Enemy moved to " + str(self.position))

    def attack(self, player):
        player.take_damage(self.damage)

    def take_damage(self, amount):
        self.health -= amount
        print("Enemy takes " + str(amount) + " damage! Health: " + str(self.health))
        if self.health <= 0:
            print("Enemy defeated!")

