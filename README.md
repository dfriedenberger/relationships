# relationships


## Installation

```bash
pip install -r requirements.txt
```

```
docker build -t frittenburger/relationships:0.0.1 .
```

## Usage

```bash
uvicorn server:app --port 9999 --reload
```

### Create rdf file for analyse
```bash
python create_rdf.py --relations data/relations.yaml
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Authors and acknowledgment

- For readme file I used format from https://www.makeareadme.com/

## License
[GPLv3](LICENSE)
