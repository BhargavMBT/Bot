import random
from typing import Text

import requests


def fetch_a_joke() -> Text:
    """
    randomly picks any API to fetch the joke
    checks which API is been picked
    calls that API and fetches the joke
    processes the joke value fetched from API
    :return: string value of joke
    """
    jokes_api_dict = {
        "icanhazdadjoke": "https://icanhazdadjoke.com/",
        "deno": "https://joke.deno.dev/",
        "chucknorris": "https://api.chucknorris.io/jokes/random"
    }
    jokes_api_names = ["icanhazdadjoke", "deno", "chucknorris"]
    joke_api = random.choice(jokes_api_names)
    if joke_api == "deno":
        joke_response = requests.get(jokes_api_dict[joke_api])
        json_joke = joke_response.json()
        joke = {"text": f"{json_joke['setup']} ... {json_joke['punchline']}"}
    elif joke_api == "chucknorris":
        joke_response = requests.get(jokes_api_dict[joke_api])
        json_joke = joke_response.json()
        joke = {"text": f"{json_joke['value']}"}
    else:
        joke_response = requests.get(url=jokes_api_dict[joke_api], headers={"Accept": "application/json"})
        json_joke = joke_response.json()
        joke = {"text": f"{json_joke['joke']}"}

    joke['image'] = get_meme()
    return joke


def get_meme() -> Text:
    meme_response = requests.get("http://alpha-meme-maker.herokuapp.com/")
    json_meme = meme_response.json().get("data")
    random_meme = random.choice(json_meme)
    return random_meme.get("image")
