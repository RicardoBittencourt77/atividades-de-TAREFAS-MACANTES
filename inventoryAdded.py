def addToInventory(inventory, addedItems):
    count = {}
    for i in addedItems:
        count.setdefault(i, 0)
        count[i] += 1
    dics = inventory.copy()
    for k, v in count.items():
        if k in dics:
            dics[k] += v
        else:
            dics[k] = v
    return dics


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
invFinal = addToInventory(inv, dragonLoot)

displayInventory(invFinal)
