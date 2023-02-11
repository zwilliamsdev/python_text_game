from menu import greetingMenu, createMenu
from loot import lootChest
from debug import debug, simulate
from player import Player

NAME = "Adventure Testing"


def main():
    # Show initial menu to greet player
    greetingMenu(NAME)

    # Create player object and get player name
    # ply = Player(getPlayerName())
    simulate('Creating character: Daixso')
    ply = Player("Daixso")
    print(f"You are the great hero {ply.getPlayerName()}!")

    # Create initial menu prompt
    createMenu("You awake in a cold damp room with only a dim amount of light coming through a small crack in the wall. You notice a chest on the far side of the room.",
               "Look through the crack", "Try to smash the wall", "Open the chest")
    # TESTING CORE FUNCTIONALITY
    simulate('Looting common, rare, epic chests')
    ply.loot("chest", "common")
    ply.loot("chest", "rare")
    ply.loot("chest", "epic")
    debug('Dumping inventory')
    ply.getInventoryItems()
    simulate('Hurting player')
    ply.hurtPlayer(50)
    simulate('Drinking health potion')
    ply.drinkHealthPotion()
    print(f'You now have {ply.getPlayerHealth()} HP.')
    simulate('Kill player')
    ply.hurtPlayer(100)


def getPlayerName():
    while True:
        playerName = input("What is your name? ")
        correct = input(f"Is {playerName} correct? Y/N ")
        if correct == "Y" or correct == "y":
            return playerName


if __name__ == "__main__":
    main()
