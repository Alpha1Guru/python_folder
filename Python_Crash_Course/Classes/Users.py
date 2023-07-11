from dataclasses import dataclass

@dataclass
class User:
    import random as rn
    """An attempt to model a user"""
    first_name: str
    last_name: str
    age: int
    favorite_num: int
    # user_name: str = last_name[:2] + first_name + str(rn.randrange(10,99))
    def describe(self):
        print(f"""\
              
              First_name is {self.first_name}
              {self.first_name} is {self.age} old
              {self.first_name}"s last name is {self.last_name}""")