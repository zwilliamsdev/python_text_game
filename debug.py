DEBUG = True


def debug(msg):
    if DEBUG:
        print(f'DEBUG: {msg}')


def simulate(msg):
    if DEBUG:
        print(f'SIMULATE: {msg}')
