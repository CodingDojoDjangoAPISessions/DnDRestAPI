from dotenv import dotenv_values
import requests

MY_DOTENV = dotenv_values("../../.env")

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


def get_alignment_by_index(index):
    if index not in ALIGNMENTS:
        print(f"WARNING: {index} not in list of Alignments")
    try:
        response = requests.get(f"{BASE_URL}/alignments/{index}")
        return response.json()
    except Exception as e:
        return f"{e}"
