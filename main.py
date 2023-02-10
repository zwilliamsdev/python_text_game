from menu import greetingMenu, createMenu
from loot import lootChest
from player import getInventoryItems
from debug import debug, simulate

NAME = "Adventure Testing"


def main():
    greetingMenu(NAME)
    simulate("MENU CREATION")
    createMenu("You awake in a cold damp room with only a dim amount of light coming through a small crack in the wall. You notice a chest on the far side of the room.",
               "Look through the crack", "Try to smash the wall", "Open the chest")
    simulate("CHECK EMPTY INVENTORY")
    getInventoryItems()
    simulate("LOOTING CHESTS")
    lootChest("common")
    lootChest("rare")
    lootChest("epic")
    simulate("DUMPING INVENTORY")
    getInventoryItems()


if __name__ == "__main__":
    main()
