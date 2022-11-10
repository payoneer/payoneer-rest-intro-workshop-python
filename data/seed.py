from ..models.item import Item


items = []
for x in range(1,10):
    items.append(Item(f'Item {x}'))