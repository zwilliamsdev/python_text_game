import random


class Item:
    def __init__(self, name: str, description: str, rarity: str) -> None:
        self.name = name
        self.description = description
        self.rarity = rarity

    def __getItem__(self, key):
        return getattr(self, key)


class Potion(Item):
    def __init__(self, name: str, description: str, rarity: str, isHealingPotion: bool, potionDamage: int) -> None:
        super().__init__(name, description, rarity)
        self.isHealingPotion = isHealingPotion
        self.potionDamage = potionDamage

    def drinkPotion(self) -> None:
        if self.isHealingPotion:
            print(f"Healing {self.potionDamage} health")
        else:
            print(f"Damaging {self.potionDamage} health")


class Weapon(Item):
    def __init__(self, name: str, description: str, rarity: str, damageType: str, minimumDamage: int, maximumDamage: int) -> None:
        super().__init__(name, description, rarity)
        self.damageType = damageType
        self.minimumDamage = minimumDamage
        self.maximumDamage = maximumDamage

    def dealDamage(self) -> None:
        damage = random.randint(self.minimumDamage, self.maximumDamage)
        print(f"Deal damage {damage}")


itemList = {
    ### Weapons ###
    "woodenClub":
        Weapon("Wooden Club", "A small club made out of wood.",
               "common", "crushing", 5, 10),

    "sharpenedSword":
        Weapon("Steel Sword", "A recently sharpened sword.",
               "rare", "slashing", 10, 20),

    ### Potions ###
    "minorHealthPotion":
        Potion("Minor Health Potion",
               "Restores a small amount of health if consumed.", "common", True, 25),

    "minorPoisonPotion":
        Potion("Minor Poison Potion",
               "You notice a skull written on the label of the vial.", "rare", False, 25),

    ### Item ###
    "coinPurse":
        Item("Coin Purse", "Several gold pieces in a leather coin purse.", "common"),

    "enchantedNecklace":
        Item("Mystical Necklace",
             "The necklace seems to be eminating with power.", "epic")
}

# loot = {
#     "hPotion": "Health Potion",
#     "gold": "Gold Pieces",
#     "sword": "Sharpened Sword",
#     "helmet": "Shiny Plate Helmet",
#     "enchanted_necklace": "Magical Necklace",
#     "mystic_ring": "Mysterious Ring",
# }
