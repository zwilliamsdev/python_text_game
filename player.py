from debug import debug

INVENTORY = []


def addInventoryItem(item):
    INVENTORY.append(item)
    debug('adding ' + item["name"] + " " + item["description"])


def getInventoryItems():
    itemCount = len(INVENTORY)
    if itemCount > 0:
        i = 0
        while i < itemCount:
            print(INVENTORY[i]["name"], INVENTORY[i]["description"])
            i += 1
    else:
        print('Your pockets are empty.')
