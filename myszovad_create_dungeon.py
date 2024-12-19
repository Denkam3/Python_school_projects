# Generate labyrinth
import random

class Lab_map:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.size = (height, width)
        self.dungeon_map = []
        self.starting_position = (1, 1)
        self.tunels = int(width * 1.5)

    def generate(self): # from the lesson
        for i in range(self.size[0]):
            dungeon_row = []
            for j in range(self.size[1]):
                dungeon_row.append("▓")
            self.dungeon_map.append(dungeon_row)
        self.dungeon_map[self.starting_position[0]][self.starting_position[1]] = "."

    def __str__(self):  # from the lesson
        dungeon_str = ""
        for row in self.dungeon_map:
            for place in row:
                dungeon_str += place
            dungeon_str += "\n"
        return dungeon_str
    
    def tunel(self):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        x, y = self.starting_position
        dig = 0
        while dig < self.tunels:
            random.shuffle(directions)
            for move_x, move_y in directions:
                steps = random.randint(1, min(self.width, self.height) - 2) # rectangle or square
                new_x = x + move_x * steps
                new_y = y + move_y * steps
            
                if 1 <= new_x < self.width - 1 and 1 <= new_y < self.height - 1:
                    if self.dungeon_map[new_y][new_x] == "▓" or self.dungeon_map[new_y][new_x] == ".":
                        for step in range(steps + 1):
                            if move_x != 0:
                                self.dungeon_map[y][x + (move_x * step)] = "." # generate path horizontal
                            if move_y != 0:
                                self.dungeon_map[y + (move_y * step)][x] = "." # generate path vertical
                        x, y = new_x, new_y
                        dig += 1
                else:
                    break
                
height = int(input("Define height of the labyrinth: "))
width = int(input("Define width of the labyrinth: "))

Labyrinth = Lab_map(height, width)
Labyrinth.generate()

Labyrinth.tunel()
print(Labyrinth)
