def createMenu(description, *args):
    print(description)
    i = 1
    for option in args:
        print(f"{i} - {option}")
        i += 1


def greetingMenu(name):
    length = len(name)
    outline = "*" * length
    print(f"\t**{outline}**")
    print(f'\t* {name} *')
    print(f"\t**{outline}**")
    print('Welcome to this text adventure game. Please follow the prompts in order to play.')
