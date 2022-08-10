class Config():
    
    __APIInfo = {
        'title':'Encode API',
        'description':'',
        'version':'1.0.0',
        'contact':{
            'name':'Deborah Vancelotte',
            'email':'vancelotted@gmail.com',
        },
        'tags':[{
        "name": "Cryptography",
        "description": "",
        }]
    }

    
    def getAPIInfo(self):
        return self.__APIInfo
