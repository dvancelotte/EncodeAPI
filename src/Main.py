from Cryptography import Encode
from Cryptography import Decode


encode = Encode.Encode()
decode = Decode.Decode()

for number in range(100000000):
    code = encode.GetEncode(number)
    decodedNumber = decode.GetNumber(code)
    if(int(decodedNumber) != int(number)): print("number: " + str(number) + " decode:" + str(decodedNumber))

print("RODOU TODOS OS CASOS COM SUCESSO")
