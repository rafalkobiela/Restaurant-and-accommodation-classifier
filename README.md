### readme

To start up server you need to have `docker` and `docker-compose` installed.
```
docker-compose up
```
Server should startup at: [http://0.0.0.0:5004/](http://0.0.0.0:5004/)

If you don't want to use docker it is suggested to use python virtualenvs

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

To startup server please run:
```
python run.py
```

Server should startup at: [http://0.0.0.0:5000/](http://0.0.0.0:5000/)

To retrain model please run:
```
pyton train.py
```

If you want to change configuration please go to `config/config.yaml`.

