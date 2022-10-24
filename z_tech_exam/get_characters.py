import hashlib
import requests
import datetime
import os
import typing as t

timestamp = datetime.datetime.now().strftime("%Y-%m-%d%H:%M:%S")
pub_key = os.environ.get("MARVEL_PUBLIC_KEY")
priv_key = os.environ.get("MARVEL_PRIVATE_KEY")
CHARACTER_URL = "http://gateway.marvel.com/v1/public/characters"

JSONType = t.Union[str, int, float, bool, None, t.Dict[str, t.Any], t.List[t.Any]]


def hash_params() -> str:
    hash_md5 = hashlib.md5()
    hash_md5.update(f"{timestamp}{priv_key}{pub_key}".encode("utf-8"))
    hashed_params = hash_md5.hexdigest()
    return hashed_params


def get_characters(offset: int, limit: int) -> JSONType:
    params = {"ts": timestamp, "apikey": pub_key, "hash": hash_params()}
    params.update({"offset": offset, "limit": limit})
    res = requests.get(CHARACTER_URL, params=params)
    results = res.json()
    return results


def get_all_characters() -> t.List[JSONType]:
    limit = 100
    offset = 1
    api_res_list = []
    while True:
        response = get_characters(offset, limit)
        if response["data"]["count"] == 0:
            break
        api_res_list.extend(response["data"]["results"])
        offset += limit

    return api_res_list
