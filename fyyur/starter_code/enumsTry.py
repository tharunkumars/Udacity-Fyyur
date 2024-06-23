from enum import Enum

class enum_list_Of_States(Enum) :
             AL = 'AL'
             AK = 'AK'
             AZ = 'AZ'
             AR = 'AR'
             CA = 'CA'
             CO = 'CO'
             CT = 'CT'
             DE = 'DE'
             DC = 'DC'
             FL = 'FL'
             GA = 'GA'
             HI = 'HI'
             ID = 'ID'
             IL = 'IL'
             IN = 'IN'
             IA = 'IA'
             KS = 'KS'
             KY = 'KY'
             LA = 'LA'
             ME = 'ME'
             MT = 'MT'
             NE = 'NE'
             NV = 'NV'
             NH = 'NH'
             NJ = 'NJ'
             NM = 'NM'
             NY = 'NY'
             NC = 'NC'
             ND = 'ND'
             OH = 'OH'
             OK = 'OK'
             OR = 'OR'
             MD = 'MD'
             MA = 'MA'
             MI = 'MI'
             MN = 'MN'
             MS = 'MS'
             MO = 'MO'
             PA = 'PA'
             RI = 'RI'
             SC = 'SC'
             SD = 'SD'
             TN = 'TN'
             TX = 'TX'
             UT = 'UT'
             VT = 'VT'
             VA = 'VA'
             WA = 'WA'
             WV = 'WV'
             WI = 'WI'
             WY = 'WY'
"""
Key Points:
@classmethod allows defining methods that operate on the class itself.
Class methods are useful for factory methods, class-level utilities, and potentially modifying class behavior.
They offer flexibility in object creation and class-related operations.
"""  
@classmethod
def choices(chcs):
    return [(choice.name, choice.value) for choice in chcs]


@staticmethod
def choices_static():
    return (r"from choices_static")



## moving commonly used Genres Data into Enum Class
class enum_list_Of_Genres (Enum) :
             Alternative = 'Alternative'
             Blues = 'Blues'
             Classical = 'Classical'
             Country = 'Country'
             Electronic = 'Electronic'
             Folk = 'Folk'
             Funk = 'Funk'
             Hip_Hop = 'Hip-Hop'
             Heavy_Metal = 'Heavy Metal'
             Instrumental = 'Instrumental'
             Jazz = 'Jazz'
             Musical_Theatre = 'Musical Theatre'
             Pop = 'Pop'
             Punk = 'Punk'
             RandB = 'R&B'
             Reggae = 'Reggae'
             RocknRoll = 'Rock n Roll'
             Soul = 'Soul'
             Other = 'Other'

@classmethod
def choices(chcs):
    return [(choice.name, choice.value) for choice in chcs]        
# incorporating review comments Ends
