from Cryptography import Cryptography 

class Decode(Cryptography):

    def __init__(self):
        super().__init__()
    
    def __CalculateNumber(self,group,code):

        quotient = self.Codes.Decode[code[0:1]]
        rest = self.Codes.Decode[code[1:2]]
        return quotient * self.__FACTORS[group] + rest

    def GetNumber(self,group,code):

        quotient = self.Codes.Decode[code[0:1]]
        rest = self.Codes.Decode[code[1:2]]
        return quotient * self.__FACTORS[group] + rest