# models/member.py

import re
from .exceptions import (
    NegativeCreditsException,
    InvalidEmailFormatException,
    InvalidPhoneNumberException,
    NegativeAmountException
)

class Member:
    def __init__(self, id: str, name: str, email: str, phone: str, credits: int, email_pattern: str, phone_pattern: str):
        if credits < 0:
            raise NegativeCreditsException("Credits cannot be negative.")
        if not re.match(email_pattern, email):
            raise InvalidEmailFormatException("Invalid email format.")
        if not re.match(phone_pattern, phone):
            raise InvalidPhoneNumberException("Invalid phone number format.")
        
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.credits = credits
        self.items = []        # List of Item objects
        self.contracts = []    # List of Contract objects

    def add_credits(self, amount: int):
        if amount < 0:
            raise NegativeAmountException("Cannot add a negative amount of credits.")
        self.credits += amount

    def deduct_credits(self, amount: int):
        if amount < 0:
            raise NegativeAmountException("Cannot deduct a negative amount of credits.")
        if self.credits - amount < 0:
            raise NegativeCreditsException("Credits cannot be negative after deduction.")
        self.credits -= amount

    def add_item(self, item):
        if item not in self.items:
            self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def add_contract(self, contract):
        if contract not in self.contracts:
            self.contracts.append(contract)

    def remove_contract(self, contract):
        if contract in self.contracts:
            self.contracts.remove(contract)

    def __str__(self):
        return f"Member(ID: {self.id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Credits: {self.credits})"

    def __eq__(self, other):
        if isinstance(other, Member):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)
