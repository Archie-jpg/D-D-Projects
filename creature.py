import utils
from utils import Dice


class Creature:
    def __init__(self, file: str, name: str):
        data = utils.get_data(file)
        creature = data[name]
        self.name = name
        self.data = creature
        self.stats = creature["stats"]


class Monster(Creature):
    def __init__(self, name):
        super().__init__("storage/monsters.json", name)
        self.ac = self.data["ac"]
        self.hp = self.data["hp"]
        self.cr = self.data["cr"]

    def roll_hp(self):
        hit_points = 0
        dice = Dice(int(self.hp[1]))
        for i in range(0, int(self.hp[0])):
            hit_points += dice.roll()
        hit_points += int(self.stats["con"]) * int(self.hp[0])
        return hit_points


class NPC(Creature):
    def __init__(self, name):
        super().__init__("storage/npcs.json", name)