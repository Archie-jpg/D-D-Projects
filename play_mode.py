import utils, creature
import json


def new_monsters():
    monsters = {}
    choice = ""
    while choice != "n":
        try:
            mon = creature.Monster(input("Monster name: ").lower())
            monsters[mon] = int(input("Number: "))
            choice = input("Add more: ").lower()
        except KeyError:
            print("Invalid monster name")
    return monsters


def preped_combat():
    combat = utils.Combat(input("Combat name: ").lower())
    return combat.monsters


def run_combat(inits, monsters):
    init_dice = utils.Dice(20)
    info = {}
    hps = {}
    for mon in monsters:
        inits[mon.name] = init_dice.roll() + int(mon.stats["dex"])
        info[mon.name] = {"ac": mon.ac,
                          "stats": mon.stats}
        for i in range(0, monsters[mon]):
            hps[mon.name + str(i + 1)] = mon.roll_hp()
    inits = utils.dict_sort(inits, True)
    print("*" * 13 + "Inits" + "*" * 12)
    print(inits)
    print("*" * 11 + "Monsters" + "*" * 11)
    for mon in monsters:
        print(mon.name)
        print(info[mon.name])
    print("*" * 10 + "Hit points" + "*" * 11)
    for hp in hps:
        print(f"{hp}: {hps[hp]}")
    input()


class Session:
    def __init__(self, party_name):
        parties = utils.get_data("storage/parties.json")
        self.name = party_name
        self.party = parties[party_name]
        self.players = []
        print("*" * 30)
        print("Who's in party")
        for p in self.party["players"]:
            if input(f"{p}: ") == "y":
                self.players.append(p)
        print(self.players)

    def combat(self):
        """
        Runs a new combat, with monsters chosen in the combat
        """
        inits = {}
        print("Enter initiatives")
        for p in self.players:
            inits[p] = int(input(f"{p}: "))
        print("*" * 30)
        choice = input("Run prepared combat: ").lower()
        if choice == "y":
            monsters = preped_combat()
        else:
            monsters = new_monsters()
        run_combat(inits, monsters)
