class Items:
    def __init__(self, itemId: str, name: str, description: str) -> None:
        self.name
        self.description

        def getDescription(self):
            return self.description


class Potion(Items):
    def __init__(self, itemId: str, name: str, description: str, isHealingPotion: bool, potionDamage: int) -> None:
        super().__init__(name, description)
        self.isHealingPotion = isHealingPotion
        self.potionDamage = potionDamage

    def drinkPotion(self):
        if self.isHealingPotion:
            f"Healing {self.potionDamage} health"
        else:
            f"Damaging {self.potionDamage} health"


minorHealthPotion = Potion("minorHealthPotion", "Minor Health Potion",
                           "Restores a small amount of health if consuemed.", True, 25)
minorPoisonPotion = Potion("minorPoisonPotion", "Minor Health Potion",
                           "Restores a small amount of health if consuemed.", True, 25)
# loot = {
#     "hPotion": "Health Potion",
#     "gold": "Gold Pieces",
#     "sword": "Sharpened Sword",
#     "helmet": "Shiny Plate Helmet",
#     "enchanted_necklace": "Magical Necklace",
#     "mystic_ring": "Mysterious Ring",
# }
