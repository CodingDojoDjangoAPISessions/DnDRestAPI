# from dotenv import dotenv_values
import requests
from pprint import pprint

# MY_DOTENV = dotenv_values("../../dnd_api/.env")
#
# print(MY_DOTENV)

BASE_URL = 'https://www.dnd5eapi.co/api'

## Alignments

ALIGNMENTS = [
    "chaotic-neutral",
    "chaotic-evil",
    "chaotic-good",
    "lawful-neutral",
    "lawful-evil",
    "lawful-good",
    "neutral",
    "neutral-evil",
    "neutral-good"
]

CLASSES = [
    'barbarian',
    'bard',
    'cleric',
    'druid',
    'fighter',
    'monk',
    'paladin',
    'ranger',
    'rogue',
    'sorcerer',
    'warlock',
    'wizard'
]


def get_alignment_by_index(index):
    if index not in ALIGNMENTS:
        print(f"WARNING: {index} not in list of Alignments")
    try:
        response = requests.get(f"{BASE_URL}/alignments/{index}")
        print(response.status_code)
        return response.json()
    except Exception as e:
        return f"{e}"


def get_all_alignments():
    return [get_alignment_by_index(a) for a in ALIGNMENTS]


def get_class_by_index(index):
    if index not in CLASSES:
        print(f"WARNING: {index} not in list of Classes")
    try:
        response = requests.get(f"{BASE_URL}/classes/{index}")
        print(response.status_code)
        return response.json()
    except Exception as e:
        return f"{e}"


def get_all_classes():
    return [get_class_by_index(c) for c in CLASSES]
