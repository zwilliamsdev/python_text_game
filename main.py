from menu import greetingMenu, createMenu
from loot import lootChest
from player import getInventoryItems
from debug import debug

NAME = "Adventure Testing"


def main():
    greetingMenu(NAME)
    debug("SIMULATE MENU CREATION")
    createMenu("You awake in a cold damp room with only a dim amount of light coming through a small crack in the wall. You notice a chest on the far side of the room.",
               "Look through the crack", "Try to smash the wall", "Open the chest")
    debug("CHECK EMPTY INVENTORY")
    getInventoryItems()
    debug("SIMULATE LOOTING CHESTS")
    debug("CHEST COMMON")
    lootChest("common")
    debug("CHEST RARE")
    lootChest("rare")
    debug("CHEST EPIC")
    lootChest("epic")
    debug("DUMPING INVENTORY")
    getInventoryItems()


if __name__ == "__main__":
    main()
