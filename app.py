# sample_usage.py

from Model.member import Member
from Model.item import Item
from Model.contract import Contract
from Model.memberRepository import MemberRepository
from Model.itemRepository import ItemRepository
from Model.contractRepository import ContractRepository
from Model.exceptions import (
    EmailExistsException,
    PhoneExistsException,
    NegativeCreditsException,
    NegativeAmountException,
    NegativeCostException,
    InvalidEndDateException,
    IdExistsException,
    InvalidEmailFormatException,
    InvalidPhoneNumberException,
    ItemNotFoundException,
    BorrowerNotFoundException,
    ContractConflictException,
    InsufficientCreditsException,
    InvalidDateFormatException,
    ContractNotFoundException,
    MemberNotFoundException
)



from datetime import date

def main():
    # Initialize repositories
    member_repo = MemberRepository()
    item_repo = ItemRepository()
    contract_repo = ContractRepository()

    # Define regex patterns for email and phone
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    phone_pattern = r'^\d+$'

    try:
        # Create Members
        member1 = Member(id="M1", name="Alice Smith", email="alice@example.com",
                         phone="1234567890", credits=100, email_pattern=email_pattern,
                         phone_pattern=phone_pattern)
        member_repo.add_member(member1)

        member2 = Member(id="M2", name="Bob Johnson", email="bob@example.com",
                         phone="0987654321", credits=150, email_pattern=email_pattern,
                         phone_pattern=phone_pattern)
        member_repo.add_member(member2)

        # Create Items
        item1 = Item(owner=member1, name="Laptop", cost=50)
        item_repo.add_item(item1)

        item2 = Item(owner=member2, name="Projector", cost=30)
        item_repo.add_item(item2)

        # Create Contracts
        contract1 = Contract(id="C1", item=item1, borrower=member2,
                             start_date=date(2024, 1, 10), end_date=date(2024, 1, 15))
        contract_repo.add_contract(contract1)

        # Attempt to create a conflicting contract
        try:
            contract2 = Contract(id="C2", item=item1, borrower=member1,
                                 start_date=date(2024, 1, 14), end_date=date(2024, 1, 20))
            # Check for conflicts
            for existing_contract in contract_repo.get_all_contracts():
                if existing_contract.conflicts_with(contract2):
                    raise ContractConflictException("Conflicting contract exists.")
            contract_repo.add_contract(contract2)
        except ContractConflictException as e:
            print(f"Error: {e}")

        # Display all members
        print("\nAll Members:")
        for member in member_repo.get_all_members():
            print(member)

        # Display all items
        print("\nAll Items:")
        for item in item_repo.get_all_items():
            print(item)

        # Display all contracts
        print("\nAll Contracts:")
        for contract in contract_repo.get_all_contracts():
            print(contract)

    except (EmailExistsException, PhoneExistsException, IdExistsException,
            InvalidEmailFormatException, InvalidPhoneNumberException,
            NegativeCreditsException, NegativeCostException) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
