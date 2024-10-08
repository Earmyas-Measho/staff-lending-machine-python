# model/credit_system.py

class CreditSystem:
    def __init__(self, member_repository):
        self.member_repository = member_repository

    def add_credits(self, member, amount):
        if member:
            member.add_credits(amount)

    def deduct_credits(self, member, amount):
        if member:
            member.deduct_credits(amount)
