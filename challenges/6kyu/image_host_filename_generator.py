import string
import random

ALFABET = tuple(string.ascii_letters)
FILE_NAME_LENGHT = 6

def generateName()
    name = ''
    for i in range(FILE_NAME_LENGHT)
        name += random.choice(ALFABET)
    if not photoManager.nameExists(name)
        return name
