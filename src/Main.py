from Cryptography import Encode
from Cryptography import Decode
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from Documentation import config
from Models import Code,Error,Number

apiInfo = config.Config().getAPIInfo()

app = FastAPI(    
    title        = apiInfo['title'],
    description  = apiInfo['description'],
    version      = apiInfo['version'],
    contact      = apiInfo['contact'],
    openapi_tags = apiInfo['tags'])

@app.on_event('startup')
def init_data():
    global encode 
    global decode
    
    encode = Encode.Encode()    
    decode = Decode.Decode()
    

@app.get("/encode/{number}" 
         ,tags=["Cryptography"]
         ,response_model=Code.Code
         ,responses={422:{"model":Error.Erro},500:{"model":Error.Erro}}
         )
def getEncode(number):        
    try:
        code = encode.GetCode(number)
        return {"code": code}
    except ValueError as err:
        return JSONResponse(status_code = 422, content={"message":str(err)})
    except Exception as err:
        return JSONResponse(status_code = 500, content={"message":str(err)})
    

@app.get("/decode/{code}"
        ,tags=["Cryptography"]
        ,response_model=Number.Number
        ,responses={422:{"model":Error.Erro},500:{"model":Error.Erro}}
        )
def getDecode(code):        
    try:
        number = decode.GetNumber(code)
        return {"number": int(number)}
    except ValueError as err:
        return JSONResponse(status_code = 400, content={"message":str(err)})
    except Exception as err:
        return JSONResponse(status_code = 500, content={"message":str(err)})
