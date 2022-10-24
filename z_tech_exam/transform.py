import pandas as pd


def transform_characters(char_dict) -> pd.DataFrame:
    df = pd.json_normalize(char_dict)
    df = df[
        [
            "id",
            "name",
            "description",
            "comics.available",
            "series.available",
            "stories.available",
            "events.available",
        ]
    ]
    df = df.rename(
        columns={
            "comics.available": "comics",
            "series.available": "series",
            "stories.available": "stories",
            "events.available": "events",
        }
    )
    return df
