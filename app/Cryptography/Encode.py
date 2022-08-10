from Cryptography import Cryptography 

class Encode():
    
    def __CalculateCharacter(self,number, divisor):
        
        rest     = int(number % divisor)
        quotient = int(number / divisor)

        return f'{Cryptography.Cryptography.CODES.Encode[quotient]}{Cryptography.Cryptography.CODES.Encode[rest]}' 
    
    def __ValidateNumber(self,number):

        if(len(str(number)) > 8 ):
            raise ValueError("The number lenght must be less or equal 8.") 

        if(not str(number).isnumeric()):
            raise ValueError("The number must have only integer numbers.")

     


    def GetCode(self,number):
        
        self.__ValidateNumber(number)

        code = ""
        number = str(number).rjust(8,"0")

        for factor in Cryptography.Cryptography.FACTORS:

            group = int(factor)
            start = (group -1)*3

            if( group <= 2 ):    
                finish = start +3
            else:
                finish = start +2
                
            code = f'{code}{self.__CalculateCharacter(int(number[start:finish]),Cryptography.Cryptography.FACTORS[factor])}'

        return code

