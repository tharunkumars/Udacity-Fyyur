import re

import fyyur.starter_code.enumsTry

"""class Human:
   def __init__(self, first_name, last_name, age):
       self.first_name = first_name
       self.last_name = last_name
       self.age= age

sarah = Human("Sarah","Silverman",48)

bob =  Human("Bob","Saget",54)    

class subHuman(Human):
       def __init__(selfsubHuman, subHumanfirst_name, subHumanlast_name, subHumanage):
        selfsubHuman.first_name = subHumanfirst_name
        selfsubHuman.last_name = subHumanlast_name
        selfsubHuman.age= subHumanage

subHumansarah = subHuman("Sarah","Silverman",48)

print("Human bob age " , bob.age)

print("subHuman Sarah age " , subHumansarah.age)
"""

def is_valid_phone(phoneNumber):
    regexPattern = re.compile(r'^\{?([0-9]{3})?[-. ]?([0-9]{3})?[-. ]?([0-9]{4})$')
    if re.match(regexPattern, phoneNumber):
        print(" Pattern matched")
        return True
    else:
        print(" Pattern NOT matched")
        return False
    
is_valid_phone("999.999.1234")

print (" Trying Enums as per review comments ")

choices_static()