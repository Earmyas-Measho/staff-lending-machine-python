# Model/itemRepository.py

from Model.exceptions import IdExistsException, ItemNotFoundException
from Model.item import Item

class ItemRepository:
    def __init__(self):
        self.items = []  # List of Item objects

    def add_item(self, item: Item):
        if any(i.id == item.id for i in self.items):
            raise IdExistsException(f"Item with ID '{item.id}' already exists.")
        self.items.append(item)
        item.owner.add_item(item)

    def delete_item(self, item: Item):
        if item in self.items:
            self.items.remove(item)
            item.owner.remove_item(item)
        else:
            raise ItemNotFoundException(f"Item with ID '{item.id}' not found.")

    def get_all_items(self):
        return self.items.copy()

    def get_item_by_id(self, item_id: str) -> Item:
        for item in self.items:
            if item.id == item_id:
                return item
        raise ItemNotFoundException(f"Item with ID '{item_id}' not found.")

    def item_exists(self, item: Item) -> bool:
        return any(i.id == item.id for i in self.items)
