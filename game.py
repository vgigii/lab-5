from player import Player
from enemy import Enemy
from item import Item
import random

class Game:
    def __init__(self):
        self.is_running = True
        self.player = Player()
        self.enemies = [Enemy(50, 10), Enemy(50, 10), Enemy(50, 10)]  
        self.items = [Item("Health Pack"), Item("Sword")]

    def start_game(self):
        print("Game Started!")
        while self.is_running:
            self.game_loop()

    def game_loop(self):
        action = input("Enter action (move/attack/collect/use): ")
        if action == "move":
            direction = input("Enter direction (left/right/up/down): ")
            self.player.move(direction)
        elif action == "attack":
            enemy = self.enemies[random.randint(0, len(self.enemies)-1)]  
            self.player.attack(enemy)
            if enemy.health <= 0:
                self.enemies.remove(enemy)
        elif action == "collect":
            item = self.items[random.randint(0, len(self.items)-1)]  
            self.player.collect_item(item)
        elif action == "use":
            item_name = input("Enter item name to use: ")
            item = next((i for i in self.player.inventory if i.name == item_name), None)
            if item:
                self.player.use_item(item)
            else:
                print("Item not found in inventory.")
        
        if self.player.health <= 0:
            print("Game Over! Player defeated.")
            self.is_running = False

        for enemy in self.enemies:
            enemy.move(self.player.position)
            if enemy.position == self.player.position:
                enemy.attack(self.player)
                if self.player.health <= 0:
                    print("Game Over! Player defeated.")
                    self.is_running = False

        if len(self.enemies) == 0:
            print("All enemies defeated. You win!")
            self.is_running = False

