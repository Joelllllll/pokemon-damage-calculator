# Pokemon Damage API


## Starting off

### Note:
  * This calculator only has data until Pokemon Generate 8.
  * To update this the 2 files in the `pokemon-damage-api/sql/data` dir will need to be updated

* You can build the image using the compose file
  - ```docker-compose build```

* Start the API
  - ```docker-compose up```


### Usage
* GET `pokemon/{pokemon_name}`
  - expects a body of evs and ivs, you don't need to define all stats. All stats (Evs and Ivs) have a default value of 0
```python
import requests
r = requests.get("http://0.0.0.0:8000/pokemon/mew", json={"evs": {"hp": 100}, "ivs": {"attack": 2}})
r.json() #/ returns
{'pokemon':{
  'type_2': None,
  'pokemon_number': 151,
  'hp': 100,
  'defense': 100,
  'sp_def': 100,
  'speed': 100,
  'legendary': False,
  'type_1': 'Psychic',
  'total': 600,
  'pokemon_name': 'Mew',
  'attack': 100,
  'sp_atk': 100,
  'generation': 1
  },
'evs': {
  'hp': 100,
  'attack': 0,
  'defense': 0,
  'special_attack': 0,
  'special_defense': 0,
  'speed': 0
  },
'ivs': {
  'hp': 0,
  'attack': 2,
  'defense': 0,
  'special_attack': 0,
  'special_defense': 0,
  'speed': 0
  },
'level': 100,
'move_name': None}
```
* POST `battle/`
  - Takes in 2 pokemon runs a simulation and returns the max and min damages possible

```python
import requests

r = requests.post("http://0.0.0.0:8000/battle",
json={
  "attacking": {
    "pokemon_name": "pikachu",
    "evs": {"hp": 100},
    "ivs": {"hp": 31},
    "level": 100,
    "move_name": "Pound"
  },
  "defending": {
    "pokemon_name": "metapod",
    "evs": {},
    "ivs": {},
    "level": 100
  }
}
)
r.json() #/ returns
{'min': 14.41, 'max': 16.95}

```
### Running Tests
* ```docker-compose run -e RAILS_ENV=test api bash -c 'pytest'```