from debug import debug, simulate
from loot import lootChest


class Player:
    def __init__(self):
        self.playerHealth = 100
        self.playerInventory = []

    def healPlayer(self, amount):
        # Perform heal if not full health
        if self.playerHealth < 100:
            self.playerHealth += amount
        else:
            print('You are not injured.')

        # Ensure health does not go above 100
        if self.playerHealth > 100:
            self.playerHealth = 100

        print(f'You have been healed to {self.playerHealth} HP.')

    def hurtPlayer(self, amount):
        self.playerHealth -= amount
        if self.playerHealth > 0:
            print(
                f'You have suffered {amount} damage and now have {self.playerHealth} HP.')
        else:
            print('You have died. Please try again.')

    def addInventoryItem(self, item):
        self.playerInventory.append(item)

    def getInventoryItems(self):
        itemCount = len(self.playerInventory)
        if itemCount > 0:
            i = 0
            while i < itemCount:
                print(self.playerInventory[i]["description"])
                i += 1
        else:
            print('Your pockets are empty.')

    def loot(self, type, rarity):
        match type:
            case "chest":
                self.addInventoryItem(lootChest(rarity))
