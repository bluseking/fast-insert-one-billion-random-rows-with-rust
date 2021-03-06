"""all the common helper methods used by the Python script
"""
import random
import sqlite3


def create_table(con: sqlite3.Connection):
    con.execute("""
        create table IF NOT EXISTS user
        (
            id INTEGER not null primary key,
            area CHAR(6),
            age INTEGER not null,
            active INTEGER not null
        )
    """)


def get_random_area_code() -> str:
    return str(random.randint(100000, 999999))

# Slightly faster. The doc for random.sample mentions:
# To choose a sample from a range of integers, use a range() object as an argument. This is especially fast and space efficient for sampling from a large population: sample(range(10000000), k=60).
def get_random_age() -> int:
    return random.choice(range(5,16,5))

def get_random_active() -> int:
    return random.getrandbits(1)

def get_random_bool() -> bool:
    return bool(random.getrandbits(1))