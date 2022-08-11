# EncodeAPI

### Run

```bash
Install libs
pip install -r requirements.txt
```

```bash
Run API
cd app/
uvicorn main:app --reload
```
### Docker

```bash
Build Image
docker build -t encodeapi .
```
```bash
Run Docker
docker run -d --name encodeapicontanier -p 80:80 encodeapi
```

### Test

```bash
pip install pytest
```
```bash
Run Test
pytest tests/main*
```

