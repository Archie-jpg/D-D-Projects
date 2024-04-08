import add, play_mode
import utils


def main():
    choice = ""
    while choice != "0":
        print("*" * 10 + "MAIN MENU" + "*" * 11)
        print("0) Exit")
        print("1) Play")
        print("2) Add creature")
        print("3) Edit creature")
        print("4) Add party")
        print("6) Add combat")
        print("7) Create Combat")
        print("*" * 30)
        choice = input("-> ")
        match choice:
            case "1":
                print("Session begin")
                session = play_mode.Session(input("Choose party: "))
                play_menu(session)
            case "2":
                print("*" * 10 + "What to add" + "*" * 9)
                print("1) Monster")
                print("2) NPC")
                print("*" * 30)
                choice = input("-> ")
                match choice:
                    case "1":
                        add.add_monster()
                    case "2":
                        add.add_npc()
            case "3":
                print("Edit something")
            case "4":
                add.add_party()
            case "5":
                add.add_combat()
            case "6":
                print("Create combat")
                # TODO Be able to create and balance combats using CR/XP
            case _:
                print("Invalid choice")
        input()
    print("Goodbye")


def play_menu(session):
    choice = ""
    while choice != "0":
        print("*" * 10 + "MAIN MENU" + "*" * 11)
        print("0) Exit")
        print("1) Combat")
        print("2) Edit party")
        print("*" * 30)
        choice = input("-> ")
        match choice:
            case "1":
                session.combat()


main()
