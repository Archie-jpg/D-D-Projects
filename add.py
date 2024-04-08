import creature
import utils


def add_monster(name=""):
    print("*" * 8 + "Create monster" + "*" * 8)
    if name == "":
        name = input("Name: ")
    new_data = {
        name: {
            "ac": input("AC: "),
            "hp": input("HP: ").split("d"),
            "cr": input("CR: "),
            "stats": {"str": input("Str: "),
                      "dex": input("Dex: "),
                      "con": input("Con: "),
                      "int": input("Int: "),
                      "wis": input("Wis: "),
                      "cha": input("Cha: ")},
        }
    }
    print("*" * 30)
    utils.dump_data("storage/monsters.json", new_data)


def add_npc():
    print("*" * 10 + "Create npc" + "*" * 10)
    new_data = {
        input("Name: "): {
            "stats": {"str": input("Str: "),
                      "dex": input("Dex: "),
                      "con": input("Con: "),
                      "int": input("Int: "),
                      "wis": input("Wis: "),
                      "cha": input("Cha: ")},
        }
    }
    print("*" * 30)
    utils.dump_data("storage/npcs.json", new_data)


def add_party():
    name = input("Party name: ")
    print("Enter players")
    choice = ""
    players = []
    while choice != "n":
        players.append(input("Player name: ").title())
        choice = input("Add more? ").lower()
    new_data = {
        name: {
            "players": players,
        }
    }
    utils.dump_data("storage/parties.json", new_data)


def add_combat():
    print("*" * 9 + "Create combat" + "*" * 8)
    name = input("Combat name: ")
    location = input("Location: ")
    monsters = {}
    choice = ""
    while choice != "n":
        name = input("Monster name: ").lower()
        try:
            monster = creature.Monster(name)
            if monster in monsters:
                print("Already added")
            else:
                number = int(input("Number: "))
                monsters[name] = number
        except KeyError:
            print("Invalid monster")
            # TODO finish this
            if input("Add new monster").lower() == "y":
                add_monster(name)
                number = int(input("Number: "))
                monsters[name] = number
        choice = input("Add more: ").lower()
    new_data = {
        name: {
            "location": location,
            "monsters": monsters,
        }
    }
    utils.dump_data("storage/combats.json", new_data)
