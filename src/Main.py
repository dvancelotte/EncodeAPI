from Cryptography import Encode
from Cryptography import Decode
from fastapi import FastAPI,HTTPException

app = FastAPI()

@app.on_event('startup')
def init_data():
    global encode 
    global decode 
    
    encode = Encode.Encode()    
    decode = Decode.Decode()
    


@app.get("/encode/{number}")
def getEncode(number : int):        
    try:
        code = encode.GetCode(number)
        return {"result": code}
    except ValueError as err:
        raise HTTPException(status_code = 400, detail=str(err))
    except Exception as err:
        raise HTTPException(status_code = 500, detail=str(err) )
    

@app.get("/decode/{code}")
def getDecode(code : str):        
    try:
        number = decode.GetNumber(code)
        return {"result": number}
    except ValueError as err:
        raise HTTPException(status_code = 400, detail=str(err))
    except Exception as err:
        raise HTTPException(status_code = 500, detail=str(err) )
