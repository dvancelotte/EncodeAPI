# EncodeAPI

### Run

```bash
Virtual Enviroment
python -m venv ./venv
```
```bash
Install libs
pip install -r requirements.txt
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

