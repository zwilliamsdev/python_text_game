class Items:
    def __init__(self, itemId: str, name: str, description: str) -> None:
        self.itemId = itemId
        self.name = name
        self.description = description

    def getDescription(self):
        return self.description


class Potion(Items):
    def __init__(self, itemId: str, name: str, description: str, isHealingPotion: bool, potionDamage: int) -> None:
        super().__init__(itemId, name, description)
        self.isHealingPotion = isHealingPotion
        self.potionDamage = potionDamage

    def drinkPotion(self):
        if self.isHealingPotion:
            print(f"Healing {self.potionDamage} health")
        else:
            print(f"Damaging {self.potionDamage} health")


minorHealthPotion = Potion("minorHealthPotion", "Minor Health Potion",
                           "Restores a small amount of health if consumed.", True, 25)
minorPoisonPotion = Potion("minorPoisonPotion", "Minor Poison Potion",
                           "You notice a skull written on the label of the vial.", False, 25)


def itemTest():
    print(minorPoisonPotion.getDescription())
    print(minorHealthPotion.getDescription())
    minorPoisonPotion.drinkPotion()
    minorHealthPotion.drinkPotion()

# loot = {
#     "hPotion": "Health Potion",
#     "gold": "Gold Pieces",
#     "sword": "Sharpened Sword",
#     "helmet": "Shiny Plate Helmet",
#     "enchanted_necklace": "Magical Necklace",
#     "mystic_ring": "Mysterious Ring",
# }
