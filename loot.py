from debug import debug, simulate
import datetime
import random

random.seed(datetime.datetime.now())

CHEST_COMMON = [
    "hPotion",
    "gold"
]

CHEST_RARE = [
    "sword",
    "helmet"
]

CHEST_EPIC = [
    "enchanted_necklace",
    "mystic_ring"
]


def lootChest(rarity):
    match rarity:
        case "common":
            return createLootChest(CHEST_COMMON)
        case "rare":
            return createLootChest(CHEST_RARE)
        case "epic":
            return createLootChest(CHEST_EPIC)
        case _:
            return createLootChest(CHEST_COMMON)


def createLootChest(chest):
    items = len(chest)
    return chest[random.randint(0, items-1)]
