def loadDungeon():
    with open('dungeon.txt') as f:
        dungeon = f.readlines()
    return dungeon


