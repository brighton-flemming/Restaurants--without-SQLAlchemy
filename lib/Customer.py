class Customer:
    def __init__(self, first_naame, family_name):
     self._first_name = first_naame
     self._family_name = family_name

    def given_name(self):
       given_name = self._first_name
       return given_name
     
    def family_name(self):
      return self._family_name
     
    def change_family_name(self, new_family_name):
       self._family_name = new_family_name

    def full_name(self, person_name):
        person_name = print(f"{self.given_name}  {self.family_name}")
        return person_name
    
    def all(self):
       customer_list = []
       customer = self.full_name
       customer_list.append(customer)
       return customer_list
