from debug import debug, simulate
from items import itemList
import time
import random
import logging

random.seed(time.time())

CHEST_COMMON = []
CHEST_RARE = []
CHEST_EPIC = []


def createChests():
    debug("Spawning chests")
    for i in itemList.keys():
        if itemList[i].rarity == "common":
            CHEST_COMMON.append(i)
        elif itemList[i].rarity == "rare":
            CHEST_RARE.append(i)
        elif itemList[i].rarity == "epic":
            CHEST_EPIC.append(i)
        else:
            logging.error("Item " + i + " does not have a rarity")


def lootChest(rarity):
    if rarity == "common":
        return CHEST_COMMON[len(CHEST_COMMON) - 1]
    elif rarity == "rare":
        return CHEST_RARE[len(CHEST_RARE) - 1]
    elif rarity == "epic":
        return CHEST_EPIC[len(CHEST_EPIC) - 1]
    else:
        logging.error("Rarity '" + rarity + "' does not exist")
