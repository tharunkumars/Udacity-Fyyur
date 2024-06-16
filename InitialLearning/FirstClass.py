class Human:
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

