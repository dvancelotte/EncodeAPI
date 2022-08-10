from cgitb import reset
from typing import final
from Cryptography import CodeTable

class Cryptography:
    
    FACTORS:final = { "1" : 78, "2" : 34, "3" : 2}
    LIMIT:final = 78
    CODES:final = CodeTable.CodeTable()


