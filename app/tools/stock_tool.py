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

"""A tool for interacting with the AlphaVantage API."""
from httplib2 import Http
import json
from urllib.parse import urlencode
from google.adk.tools import FunctionTool

BASE_URL = "https://www.alphavantage.co/query"

def _alpha_vantage_query(symbol: str) -> dict:
    """Makes a request to the AlphaVantage API and returns the JSON response.

    Args:
        symbol: The stock ticker to look up

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
            return {"error": f"AlphaVantage API returned status {response.status}", "details": json.loads(content)}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

def search_stock(stock: str) -> dict:
    """Searches for the stock given the symbol.

    Args:
        stock: the stock ticker to look for

    Returns:
        A dictionary containing the search results.
    """
    return _alpha_vantage_query(stock)

search_stock_tool = FunctionTool(
    func=search_stock,
)