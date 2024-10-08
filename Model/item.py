# Model/item.py

import uuid
from Model.exceptions import NegativeCostException

class Item:
    def __init__(self, owner, name: str, cost: int):
        if cost < 0:
            raise NegativeCostException("Cost cannot be negative.")
        
        self.id = str(uuid.uuid4())  # Unique identifier for each item
        self.owner = owner      # Member object
        self.name = name
        self.cost = cost

    def set_owner(self, new_owner):
        self.owner = new_owner

    def set_cost(self, new_cost: int):
        if new_cost < 0:
            raise NegativeCostException("Cost cannot be negative.")
        self.cost = new_cost

    def __str__(self):
        return f"Item(ID: {self.id}, Name: {self.name}, Cost: {self.cost}, Owner: {self.owner.name})"

    def __eq__(self, other):
        if isinstance(other, Item):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)
