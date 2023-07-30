-- create empty tables
CREATE TABLE pokemon (pokemon_number INTEGER NOT NULL,
    pokemon_name VARCHAR(255) NOT NULL,
    type_1 VARCHAR(255) NOT NULL,
    type_2 VARCHAR(255),
    total INTEGER,
    hp INTEGER,
    attack INTEGER,
    defense INTEGER,
    sp_atk INTEGER,
    sp_def INTEGER,
    speed INTEGER,
    generation INTEGER,
    legendary BOOLEAN
);

CREATE TABLE pokemon_moves (
    move_number INTEGER NOT NULL,
    move_name VARCHAR(255),
    effect VARCHAR,
    attack_type VARCHAR(255),
    kind VARCHAR(255),
    power INTEGER,
    accuracy VARCHAR(255),
    pp INTEGER
);

-- read in the files
COPY pokemon
FROM '/docker-entrypoint-initdb.d/data/pokemon-stats.csv'
DELIMITER ','
CSV HEADER;

COPY pokemon_moves
FROM '/docker-entrypoint-initdb.d/data/pokemon-moves.csv'
DELIMITER ','
CSV HEADER;

