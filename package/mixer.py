import random

items = [1, 2, 3, 4]

def mixin(items):
    return random.randrange(1, len(items), 1)

print(mixin(items))