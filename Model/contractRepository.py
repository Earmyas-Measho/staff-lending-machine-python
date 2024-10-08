import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Model.exceptions import IdExistsException
from Model.contract import Contract

class ContractRepository:
    def __init__(self):
        self.contracts = []

    def add_contract(self, contract):
        if any(c.id == contract.id for c in self.contracts):
            raise IdExistsException()
        self.contracts.append(contract)

    def delete_contract(self, contract):
        self.contracts.remove(contract)

    def get_contract(self, contract_id):
        return next((c for c in self.contracts if c.id == contract_id), None)

    def get_all_contracts(self):
        return self.contracts.copy()

    def cancel_contracts_for_item(self, item):
        for contract in self.contracts:
            if contract.item == item and contract.active:
                contract.active = False
