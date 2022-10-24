import pandas as pd

from get_characters import get_all_characters
from transform import transform_characters


def main() -> pd.DataFrame:
    characters = get_all_characters()
    return transform_characters(characters)
