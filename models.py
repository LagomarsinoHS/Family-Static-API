from random import randint


class Family:
    def __init__(self, last_name):
        self._last_name = last_name
        self._members = [{
            "id": 1,
            "first_name": "Humberto",
            "last_name": "Jackson",
            "age": 30,
            "lucky_numbers": [7, 12, 15]
        },
            {
                "id": 2,
                "first_name": "Diego",
                "last_name": "Jackson",
                "age": 25,
                "lucky_numbers": [13, 46, 79]
        },
            {
                "id": 3,
                "first_name": "Luis",
                "last_name": "Jackson",
                "age": 35,
                "lucky_numbers": [54, 101, 1]
        }]

    def _generateId(self):
        return randint(0, 100)

    def add_member(self, member):
        member["id"]=self._generateId() #se lo paso del otro lado
        member["last_name"] = self._last_name
        self._members.append(member)
        return member

    def delete_member(self, id):
        member = self.get_member(id)
        self._members.remove(member)
        return True

    def update_member(self, id, member):
        selfmember = self.get_member(id)
        selfmember.update(member)
        return selfmember

        #FormaLarga
        #selfmember.update({"dato": member["first_name"]})

    def get_member(self, id):
        miembroX = list(filter(lambda miembro: miembro["id"] == id, self.get_all_members()))
        #miembroX = filter(lambda miembro: miembro["id"] == id, fam.get_all_members())  
        if miembroX[0]:
            return miembroX[0]
        else:
            return None

    def get_all_members(self):
        return self._members
