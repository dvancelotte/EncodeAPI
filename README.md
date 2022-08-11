# EncodeAPI

## Info

Python Version : 3.10.5

### Run

#### Install libs
```bash
pip install -r requirements.txt
```

####  Run API
```bash
cd app/
uvicorn main:app --reload
```

### Docker

#### Build Image
```bash
docker build -t encodeapi .
```

#### Run Docker
```bash
docker run -d --name encodeapicontanier -p 80:80 encodeapi
```

### Test

```bash
pip install pytest
```

```bash
pytest tests/main*
```

