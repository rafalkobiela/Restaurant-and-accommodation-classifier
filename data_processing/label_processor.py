from typing import Dict


def get_label_encoder() -> Dict:
    return {
        "restaurant": 1,
        "retsaurant": 1,
        "accommodation": 0,
        "acommodation": 0
    }


def get_label_decoder() -> Dict:
    return {
        1: "restaurant",
        0: "accommodation",
    }
