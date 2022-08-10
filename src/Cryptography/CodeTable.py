from typing import final
from string import ascii_letters
from string import digits


class CodeTable:

    __SPECIALS_CHARACTERS:final = "!@#$%*()|-_=+^/?"

    Encode = {}
    Decode = {}
    Size = 0

    def __init__(self):
        self.__BuildTables()

    def __BuildTables(self):
        
        characteres = self.__SPECIALS_CHARACTERS + ascii_letters + digits
        
        for index, char in enumerate(characteres):
            self.Encode[index] = char
            self.Decode[char] = index
            