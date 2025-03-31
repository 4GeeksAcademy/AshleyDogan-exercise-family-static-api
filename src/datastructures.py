
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name, initial_members: list=[]):
        self.last_name = last_name
        self._members = []
        for member in initial_members:
            self.add_member(member)

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 999999)

    def add_member(self, member):
        member['last_name'] = self.last_name
        if 'id' in member:
            self._members.append(member)
        else:
            member['id'] = self._generateId()
            self._members.append(member)


    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return True  # Successfully deleted
        return False  

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None
    
    # def update_member(self, member):
    #     for item in self._members:
    #         if member["id"] == item["id"]:
    #             item = member
    #             print(item)
    #             print(member)
    #             return True
    #     return False

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
