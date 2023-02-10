from menu import greetingMenu, createMenu
from loot import lootChest
from debug import debug, simulate
from player import Player

NAME = "Adventure Testing"
ply = Player()


def main():
    print(dir(Player))
    greetingMenu(NAME)
    createMenu("You awake in a cold damp room with only a dim amount of light coming through a small crack in the wall. You notice a chest on the far side of the room.",
               "Look through the crack", "Try to smash the wall", "Open the chest")
    lootChest(ply, "common")
    lootChest(ply, "rare")
    lootChest(ply, "epic")
    Player.getInventoryItems(ply)
    Player.hurtPlayer(ply, 50)
    Player.healPlayer(ply, 25)
    Player.hurtPlayer(ply, 100)


if __name__ == "__main__":
    main()
