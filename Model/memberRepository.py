from Model import Member
from Model.exceptions import EmailExistsException, IdExistsException, MemberNotFoundException, PhoneExistsException


class MemberRepository:
    def __init__(self):
        self.members = []  # List of Member objects

    def add_member(self, member: Member):
        if any(m.id == member.id for m in self.members):
            raise IdExistsException(f"Member with ID '{member.id}' already exists.")
        if any(m.email == member.email for m in self.members):
            raise EmailExistsException(f"Member with Email '{member.email}' already exists.")
        if any(m.phone == member.phone for m in self.members):
            raise PhoneExistsException(f"Member with Phone '{member.phone}' already exists.")
        self.members.append(member)

    def delete_member(self, member: Member):
        if member in self.members:
            self.members.remove(member)
        else:
            raise MemberNotFoundException(f"Member with ID '{member.id}' not found.")

    def get_member_by_id(self, member_id: str):
        for member in self.members:
            if member.id == member_id:
                return member
        raise MemberNotFoundException(f"Member with ID '{member_id}' not found.")

    def get_all_members(self):
        return self.members.copy()

    def email_exists(self, email: str):
        return any(m.email == email for m in self.members)

    def phone_exists(self, phone: str):
        return any(m.phone == phone for m in self.members)
