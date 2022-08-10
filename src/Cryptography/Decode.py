from Cryptography import Cryptography
import re

class Decode():

    #__PATTERN = re.compile("[A-Z][0-9]!@#$%*()|-_=+^/?")
    __PATTERN = re.compile("!|[A-Z]|[a-z]|[0-9]|@|#|\$|%|\*|\(|\)|\||\-|\_|\=|\+|\^|\/|\?|")


    def __ValidateCode(self,code):

        if(len(str(code)) != 6 ):
            raise ValueError("The code lenght must be equal 6.") 

        if(not self.__PATTERN.match(code)):
            raise ValueError("The code is invalid.")     

        print("validate")

    def __CalculateNumber(self,code,factor,limit):

        quotient = Cryptography.Cryptography.CODES.Decode[code[0:1]]
        rest = Cryptography.Cryptography.CODES.Decode[code[1:2]]
        result = quotient * factor + rest

        if(len(str(result))> limit): raise ValueError("The code is invalid.")
        
        return str(result).rjust(limit,"0") 

    def GetNumber(self,code):
        
        self.__ValidateCode(code)
        number=""
        limit = 0

        for factor in Cryptography.Cryptography.FACTORS:

            group = int(factor)
            start = (group -1)*2
            finish = start +2          

            if(group<=2): limit = 3
            else: limit =2
                
            number = f'{number}{self.__CalculateNumber(code[start:finish],Cryptography.Cryptography.FACTORS[factor],limit)}'

        return int(number)