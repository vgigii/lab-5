import random

class Level:
    def __init__(self, level_number):
        self.level_number = level_number
        self.obstacles = self.generate_obstacles()

    def generate_obstacles(self):
        return [[random.randint(0, 5), random.randint(0, 5)] for _ in range(5)] 

