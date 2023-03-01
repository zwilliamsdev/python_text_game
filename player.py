from debug import debug, simulate
from items import itemList
from loot import lootChest


class Player:
    def __init__(self, name):
        self.playerName = name
        self.playerHealth = 100
        self.playerInventory = []
        self.healthPotionAmount = 25

    ###
    # Player Name
    ###
    def getPlayerName(self):
        return self.playerName

    ###
    # Player Health
    ###
    def getPlayerHealth(self):
        return self.playerHealth

    def healPlayer(self, amount):
        # Perform heal if not full health
        if self.playerHealth < 100:
            self.playerHealth += amount
        else:
            print('You are not injured.')
            return

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
                print(self.playerInventory[i])
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

    ###
    # Useable Items
    ###
    def drinkHealthPotion(self):
        if self.playerInventory.count("hPotion") > 0:
            self.playerInventory.remove("hPotion")
            print('You uncork the potion and chug it down\n feeling a tingling sensation as your wounds begin to heal.')
            self.healPlayer(self.healthPotionAmount)
        else:
            print('You dont have a potion to drink.')
