# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A tool for interacting with the Scryfall API."""

import time
from httplib2 import Http
import json
from urllib.parse import urlencode
from google.adk.tools import FunctionTool

BASE_URL = "https://api.scryfall.com"

def _scryfall_request(api_path: str, method: str = "GET", params: dict = None, body: dict = None) -> dict:
    """Makes a request to the Scryfall API and returns the JSON response.

    Args:
        api_path: The API path to request (e.g., "/cards/random").
        method: The HTTP method to use (e.g., "GET", "POST").
        params: A dictionary of query parameters to include in the request.
        body: A dictionary to send as the JSON body of a POST request.

    Returns:
        A dictionary containing the JSON response from the API.
    """
    http_obj = Http()
    url = BASE_URL + api_path
    if params:
        url += "?" + urlencode(params)

    headers = {
        "User-Agent": "ADK-Explorations-Agent/1.0",
        "Accept": "application/json",
        "Content-Type": "application/json; charset=UTF-8",
    }

    request_body = json.dumps(body) if body else None

    try:
        # Scryfall API asks for a 50-100ms delay between requests.
        time.sleep(0.1)
        response, content = http_obj.request(
            uri=url,
            method=method,
            headers=headers,
            body=request_body,
        )

        if response.status == 200:
            return json.loads(content)
        else:
            return {"error": f"Scryfall API returned status {response.status}", "details": json.loads(content)}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

def search_cards(query: str) -> dict:
    """Searches for cards matching a query.

    Args:
        query: The search query. See https://scryfall.com/docs/syntax for
          more details.

    Returns:
        A dictionary containing the search results.
    """
    return _scryfall_request("/cards/search", params={"q": query})

search_cards_tool = FunctionTool(
    func=search_cards,
)

def get_card_by_name(name: str, exact: bool = False) -> dict:
    """Gets a card with a specific name.

    Args:
        name: The name of the card to find.
        exact: If true, performs an exact name match. Otherwise, a fuzzy
          match is performed.

    Returns:
        A dictionary containing the card data.
    """
    params = {"fuzzy": name}
    if exact:
        params = {"exact": name}
    return _scryfall_request("/cards/named", params=params)

get_card_by_name_tool = FunctionTool(
    func=get_card_by_name,
)

def get_random_card() -> dict:
    """Gets a random card.

    Returns:
        A dictionary containing the card data.
    """
    return _scryfall_request("/cards/random")

get_random_card_tool = FunctionTool(
    func=get_random_card,
)

def get_card_by_id(scryfall_id: str) -> dict:
    """Gets a card by its Scryfall ID.

    Args:
        scryfall_id: The Scryfall ID of the card to find.

    Returns:
        A dictionary containing the card data.
    """
    return _scryfall_request(f"/cards/{scryfall_id}")

get_card_by_id_tool = FunctionTool(
    func=get_card_by_id,
)

def autocomplete_card_name(query: str) -> dict:
    """Returns a list of up to 20 full English card names that match a given query.

    Args:
        query: The query to autocomplete.

    Returns:
        A dictionary containing a list of matching card names.
    """
    return _scryfall_request("/cards/autocomplete", params={"q": query})

autocomplete_card_name_tool = FunctionTool(
    func=autocomplete_card_name,
)

def get_card_collection(identifiers: list[dict]) -> dict:
    """Returns a list of cards for a given list of identifiers.

    Args:
        identifiers: A list of dictionaries, where each dictionary
          identifies a card. See https://scryfall.com/docs/api/cards/collection
          for more details on the format of the identifiers.

    Returns:
        A dictionary containing a list of matching cards.
    """
    return _scryfall_request("/cards/collection", method="POST", body={"identifiers": identifiers})

get_card_collection_tool = FunctionTool(
    func=get_card_collection,
)

def get_card_by_code_and_number(code: str, number: int, lang: str = "en") -> dict:
    """Gets a card with a specific collector number and set code.

    Args:
        code: The set code.
        number: The collector number.
        lang: The language to return the card in.

    Returns:
        A dictionary containing the card data.
    """
    return _scryfall_request(f"/cards/{code}/{number}/{lang}")

get_card_by_code_and_number_tool = FunctionTool(
    func=get_card_by_code_and_number,
)

def get_card_by_multiverse_id(multiverse_id: int) -> dict:
    """Gets a card with a specific Multiverse ID.

    Args:
        multiverse_id: The Multiverse ID.

    Returns:
        A dictionary containing the card data.
    """
    return _scryfall_request(f"/cards/multiverse/{multiverse_id}")

get_card_by_multiverse_id_tool = FunctionTool(
    func=get_card_by_multiverse_id,
)

def get_card_by_mtgo_id(mtgo_id: int) -> dict:
    """Gets a card with a specific MTGO ID.

    Args:
        mtgo_id: The MTGO ID.

    Returns:
        A dictionary containing the card data.
    """
    return _scryfall_request(f"/cards/mtgo/{mtgo_id}")

get_card_by_mtgo_id_tool = FunctionTool(
    func=get_card_by_mtgo_id,
)

def get_card_by_arena_id(arena_id: int) -> dict:
    """Gets a card with a specific Arena ID.

    Args:
        arena_id: The Arena ID.

    Returns:
        A dictionary containing the card data.
    """
    return _scryfall_request(f"/cards/arena/{arena_id}")

get_card_by_arena_id_tool = FunctionTool(
    func=get_card_by_arena_id,
)

def get_card_by_tcgplayer_id(tcgplayer_id: int) -> dict:
    """Gets a card with a specific TCGplayer ID.

    Args:
        tcgplayer_id: The TCGplayer ID.

    Returns:
        A dictionary containing the card data.
    """
    return _scryfall_request(f"/cards/tcgplayer/{tcgplayer_id}")

get_card_by_tcgplayer_id_tool = FunctionTool(
    func=get_card_by_tcgplayer_id,
)

def get_card_by_cardmarket_id(cardmarket_id: int) -> dict:
    """Gets a card with a specific Cardmarket ID.

    Args:
        cardmarket_id: The Cardmarket ID.

    Returns:
        A dictionary containing the card data.
    """
    return _scryfall_request(f"/cards/cardmarket/{cardmarket_id}")

get_card_by_cardmarket_id_tool = FunctionTool(
    func=get_card_by_cardmarket_id,
)

def get_all_sets() -> dict:
    """Returns a list of all sets.

    Returns:
        A dictionary containing a list of all sets.
    """
    return _scryfall_request("/sets")

get_all_sets_tool = FunctionTool(
    func=get_all_sets,
)

def get_set_by_code(code: str) -> dict:
    """Gets a set by its code.

    Args:
        code: The set code.

    Returns:
        A dictionary containing the set data.
    """
    return _scryfall_request(f"/sets/{code}")

get_set_by_code_tool = FunctionTool(
    func=get_set_by_code,
)

def get_set_by_tcgplayer_id(tcgplayer_id: int) -> dict:
    """Gets a set by its TCGplayer ID.

    Args:
        tcgplayer_id: The TCGplayer ID.

    Returns:
        A dictionary containing the set data.
    """
    return _scryfall_request(f"/sets/tcgplayer/{tcgplayer_id}")

get_set_by_tcgplayer_id_tool = FunctionTool(
    func=get_set_by_tcgplayer_id,
)

def get_set_by_id(scryfall_id: str) -> dict:
    """Gets a set by its Scryfall ID.

    Args:
        scryfall_id: The Scryfall ID of the set.

    Returns:
        A dictionary containing the set data.
    """
    return _scryfall_request(f"/sets/{scryfall_id}")

get_set_by_id_tool = FunctionTool(
    func=get_set_by_id,
)

all_scryfall_tools = [
    search_cards_tool,
    get_card_by_name_tool,
    get_random_card_tool,
    get_card_by_id_tool,
    autocomplete_card_name_tool,
    get_card_collection_tool,
    get_card_by_code_and_number_tool,
    get_card_by_multiverse_id_tool,
    get_card_by_mtgo_id_tool,
    get_card_by_arena_id_tool,
    get_card_by_tcgplayer_id_tool,
    get_card_by_cardmarket_id_tool,
    get_all_sets_tool,
    get_set_by_code_tool,
    get_set_by_tcgplayer_id_tool,
    get_set_by_id_tool,
]
