# models/contract.py

from datetime import date
from .exceptions import InvalidEndDateException

class Contract:
    def __init__(self, id: str, item, borrower, start_date: date, end_date: date):
        if end_date < start_date:
            raise InvalidEndDateException("End date cannot be before start date.")
        
        self.id = id
        self.item = item              # Item object
        self.borrower = borrower      # Member object
        self.start_date = start_date
        self.end_date = end_date
        self.active = True

    def conflicts_with(self, other_contract):
        if self.item != other_contract.item:
            return False
        if not self.active or not other_contract.active:
            return False
        # Check if date ranges overlap
        return not (self.end_date < other_contract.start_date or self.start_date > other_contract.end_date)

    def __str__(self):
        return (f"Contract(ID: {self.id}, Item: {self.item.name}, Borrower: {self.borrower.name}, "
                f"Start Date: {self.start_date}, End Date: {self.end_date}, Active: {self.active})")

    def __eq__(self, other):
        if isinstance(other, Contract):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)
