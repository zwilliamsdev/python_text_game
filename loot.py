from debug import debug, simulate
from player import addInventoryItem
import datetime
import random

random.seed(datetime.datetime.now())

CHEST_COMMON = [
    {
        "name": "hPotion",
        "description": "Health Potion"
    },
    {
        "name": "gold",
        "description": "Gold Pieces"
    }
]

CHEST_RARE = [
    {
        "name": "sword",
        "description": "Sharpened Sword"

    },
    {
        "name": "helmet",
        "description": "Shiny Plate Helmet"
    }
]

CHEST_EPIC = [
    {
        "name": "enchanted_necklace",
        "description": "Magical Necklace",
    },
    {
        "name": "mystic_ring",
        "description": "Mysterious Ring"

    }
]


def lootChest(rarity):
    match rarity:
        case "common":
            createLootChest(CHEST_COMMON)
        case "rare":
            createLootChest(CHEST_RARE)
        case "epic":
            createLootChest(CHEST_EPIC)
        case _:
            createLootChest(CHEST_COMMON)


def createLootChest(chest):
    items = len(chest)
    item = chest[random.randint(0, items-1)]
    addInventoryItem(item)
