from importlib.resources import files
from typing import Dict


def load_word_list() -> Dict[str, str]:
    try:
        word_list_content = (files("password_dice") / "data" / "word_list.txt").read_text()
    except FileNotFoundError:
        raise FileNotFoundError("Word list file not found in package resources")
    word_list: Dict[str, str] = {}
    for line in word_list_content.strip().splitlines():
        parts: list[str] = line.strip().split("\t")
        if len(parts) != 2:
            raise ValueError(f"Expected line to have 2 parts but received {len(parts)} parts: {line.strip()}")
        id: str = parts[0]
        word: str = parts[1]
        word_list[id] = word
    return word_list
