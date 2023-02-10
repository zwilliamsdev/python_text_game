from menu import greetingMenu, createMenu
from loot import lootChest
from debug import debug, simulate
from player import Player

NAME = "Adventure Testing"
ply = Player()


def main():
    greetingMenu(NAME)
    createMenu("You awake in a cold damp room with only a dim amount of light coming through a small crack in the wall. You notice a chest on the far side of the room.",
               "Look through the crack", "Try to smash the wall", "Open the chest")
    ply.loot("chest", "common")
    ply.loot("chest", "rare")
    ply.loot("chest", "epic")
    ply.getInventoryItems()
    ply.hurtPlayer(50)
    ply.healPlayer(25)
    ply.hurtPlayer(100)


if __name__ == "__main__":
    main()
