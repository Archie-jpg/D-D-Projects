import random, json


# Dict sort
def __value_getter(item: any) -> any:
    return item[1]


def dict_sort(to_sort: dict[any: any], desc: bool) -> dict[any: any]:
    """
    Sorts a dictionary by its keys
    :param to_sort: The dictionary to be sorted
    :param desc: False - Sorts in ascending order
                 True - Sorts in descending order
    :return: Returns a list of the values sorted by their keys
    """
    sorted_dict = sorted(to_sort.items(), key=__value_getter)
    if desc:
        sorted_dict.reverse()
    sorted_list = []
    for item in sorted_dict:
        sorted_list.append(item[0])
    return sorted_list


# Json utils
def get_data(data_file: str) -> dict[str: any]:
    """
    Returns the data from a json file
    :param data_file: A json file
    :return: The json files data as a dictionary
    """
    with open(data_file) as file:
        data = json.load(file)
        return data


def dump_data(file_name, new_data):
    """
    Dumps data into a json file
    :param file_name: The file to be dumped into
    :param new_data: The data to be dumped
    """
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            data.update(new_data)
    except FileNotFoundError:
        with open(file_name, "w") as file:
            json.dump(new_data, file, indent=4)
    except json.decoder.JSONDecodeError:
        with open(file_name, "w") as file:
            json.dump(new_data, file, indent=4)
    else:
        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)


# Other Utils
def get_monsters():
    data = get_data("storage/monsters.json")
    return [mon for mon in data.keys()]


# Dice Class
class Dice:
    def __init__(self, Sides):
        """
        Creates a new dice
        :param Sides: The number of side the dice has
        """
        self.sides = Sides + 1

    def roll(self):
        return random.randint(1, self.sides)


class Combat:
    def __init__(self, name):
        data = get_data("storage/combats.json")
        combat = data[name]
        self.name = name
        self.location = combat["location"]
        self.monsters = combat["monsters"]
