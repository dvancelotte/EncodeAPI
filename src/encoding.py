#Fazer o dicionario se montar sozinho
#Fazer o algoritimo de encode
#Fazer o algoritimo de decode
#Fazer o teste
table = {0:"!",1:"@",2:"#",3:"$",4:"%",5:"*",6:"(",7:")",8:"|", 9:"-", 10:"_", 11:"=", 12:"+", 13:"^", 14:"/"}

tableDecode = {"!":0,
        "@":1,
        "#":2,
        "$":3,
        "%":4,
        "*":5,
        "(":6,
        ")":7,
        "|":8,
        "-":9,
        "_":10,
        "=":11,
        "+":12,
        "^":13,
        "/":14
    }

size = 0


def CalculateOverTable(number, divisor):
    code = ""
    resto = int(number % divisor)
    div = int(number / divisor)

    if(div > size): return "?" + CalculateOverTable(div) + table[resto]
    return table[div] + table[resto]



def Encode(number):

    numberFormatted = str(number).rjust(8,"0")
    
    numero = int(numberFormatted[0:3])
    code = EncodeChar78(numero,2)   

    numero = int(numberFormatted[3:6])
    code = code + EncodeChar39(numero,2)  

    numero = int(numberFormatted[6:8])
    code = code + EncodeChar02(numero,1)

    return code

def EncodeChar78(number,size):
    return (CalculateOverTable(number,78)).rjust(size,"!")

def EncodeChar39(number,size):
    return (CalculateOverTable(number,39)).rjust(2,"!")    

def EncodeChar02(number,size):
    return (CalculateOverTable(number,2)).rjust(size,"!")

def DecodeChar78(code):
    dividendo = tableDecode[code[0:1]]
    resto = tableDecode[code[1:2]]
    return dividendo * 78 + resto

def DecodeChar39(code):
    dividendo = tableDecode[code[0:1]]
    resto = tableDecode[code[1:2]]
    return dividendo * 39 + resto

def DecodeChar02(code):
    dividendo = tableDecode[code[0:1]]
    resto = tableDecode[code[1:2]]
    return dividendo * 2 + resto

def Decode(code):

    part = code[0:2]
    numero = str(DecodeChar78(part)).rjust(3,"0") 

    part = code[2:4]
    numero = numero + str(DecodeChar39(part)).rjust(3,"0") 

    part = code[4:6]
    numero = numero + str(DecodeChar02(part)).rjust(2,"0")

    return int(numero)


def BuildTable():
    
    character = 'a'
    startIndex = len(table)

    for index in range(61):
        table[startIndex + index] = character
        tableDecode[character] = startIndex + index
        if(character == 'z'): character = 'A'
        elif(character == 'Z'): character = '0'
        elif(character == '1' or character == '2' or character == '3'):character = chr (ord (character) + 1)
        else: character = chr (ord (character) + 1)

    
    
BuildTable()
size = len(table)-1

code = Encode(100000)
decodedNumber = Decode(code)


for number in range(999999):     
    code = Encode(number)
    decodedNumber = Decode(code)
    print()
    if(int(decodedNumber) != int(number)): print("number: " + str(number) + " decode:" + str(decodedNumber))

print("RODOU TODOS OS CASOS COM SUCESSO")
