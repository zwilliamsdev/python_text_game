import random


class Items:
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    def getName(self) -> str:
        return self.name

    def getDescription(self) -> str:
        return self.description


class Potion(Items):
    def __init__(self, name: str, description: str, isHealingPotion: bool, potionDamage: int) -> None:
        super().__init__(name, description)
        self.isHealingPotion = isHealingPotion
        self.potionDamage = potionDamage

    def drinkPotion(self):
        if self.isHealingPotion:
            print(f"Healing {self.potionDamage} health")
        else:
            print(f"Damaging {self.potionDamage} health")


class Weapon(Items):
    def __init__(self, name: str, description: str, damageType: str, minimumDamage: int, maximumDamage: int) -> None:
        super().__init__(name, description)
        self.damageType = damageType
        self.minimumDamage = minimumDamage
        self.maximumDamage = maximumDamage

    def dealDamage(self):
        damage = random.randint(self.minimumDamage, self.maximumDamage)
        print(f"Deal damage {damage}")


items = {
    ### Weapons ###
    "woodenClub": Weapon("Wooden Club", "A small club made out of wood.", "crushing", 5, 10),
    "sharpenedSword": Weapon("Steel Sword", "A recently sharpened sword.", "slashing", 10, 20),
    ### Potions ###
    "minorHealthPotion": Potion("Minor Health Potion", "Restores a small amount of health if consumed.", True, 25),
    "minorPoisonPotion": Potion("Minor Poison Potion", "You notice a skull written on the label of the vial.", False, 25),
    ### Items ###
    "coinPurse": Items("Coin Purse", "Several gold pieces in a leather coin purse."),
    "enchantedNecklace": Items("Mystical Necklace", "The necklace seems to be eminating with power.")
}

# loot = {
#     "hPotion": "Health Potion",
#     "gold": "Gold Pieces",
#     "sword": "Sharpened Sword",
#     "helmet": "Shiny Plate Helmet",
#     "enchanted_necklace": "Magical Necklace",
#     "mystic_ring": "Mysterious Ring",
# }
