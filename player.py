from debug import debug, simulate

playerInventory = []
playerHealth = 100


def healPlayer(amount):
    # Perform heal if not full health
    if playerHealth < 100:
        playerHealth += amount
    else:
        print('You are not injured.')

    # Ensure health does not go above 100
    if playerHealth > 100:
        playerHealth = 100

    print(f'You have been healed to {playerHealth} HP.')


def hurtPlayer(amount):
    playerHealth -= amount
    if playerHealth > 0:
        print(
            f'You have suffered {amount} damage and now have {playerHealth} HP.')
    else:
        print('You have died. Please try again.')


def addInventoryItem(item):
    playerInventory.append(item)


def getInventoryItems():
    itemCount = len(playerInventory)
    if itemCount > 0:
        i = 0
        while i < itemCount:
            print(playerInventory[i]["description"])
            i += 1
    else:
        print('Your pockets are empty.')
