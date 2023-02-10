from debug import debug, simulate
from loot import lootChest


class Player:
    def __init__(self, name):
        self.playerName = name
        self.playerHealth = 100
        self.playerInventory = []

    ###
    # Player Name
    ###
    def getPlayerName(self):
        return self.playerName

    ###
    # Player Health
    ###
    def getPlayerHealth(self):
        print(f"You currently have {self.playerHealth} HP.")

    def healPlayer(self, amount):
        # Perform heal if not full health
        if self.playerHealth < 100:
            self.playerHealth += amount
        else:
            print('You are not injured.')

        # Ensure health does not go above 100
        if self.playerHealth > 100:
            self.playerHealth = 100

        print(f'You have been healed for {amount} HP.')

    def hurtPlayer(self, amount):
        self.playerHealth -= amount
        if self.playerHealth > 0:
            print(
                f'You have suffered {amount} HP worth of damage.')
        else:
            print('You have died. Please try again.')

    ###
    # Player Inventory
    ###
    def getInventoryItems(self):
        itemCount = len(self.playerInventory)
        if itemCount > 0:
            i = 0
            while i < itemCount:
                print(self.playerInventory[i]["description"])
                i += 1
        else:
            print('Your pockets are empty.')

    def addInventoryItem(self, item):
        self.playerInventory.append(item)

    ###
    # Looting
    ###
    def loot(self, type, rarity):
        match type:
            case "chest":
                self.addInventoryItem(lootChest(rarity))
