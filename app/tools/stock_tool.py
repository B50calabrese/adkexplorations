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
import os
import time
from httplib2 import Http
import json
from urllib.parse import urlencode
from google.adk.tools import FunctionTool

BASE_URL = "https://www.alphavantage.co/query"

def _alpha_vantage_query(function: str, symbol: str) -> dict:
    """Makes a request to the AlphaVantage API and returns the JSON response.

    Args:
        function: The API function to call (e.g., "TIME_SERIES_DAILY_ADJUSTED").
        symbol: The stock ticker to look up.

    Returns:
        A dictionary containing the JSON response from the API.
    """
    http_obj = Http()
    params = {
        "function": function,
        "symbol": symbol,
        "apikey": os.environ.get("ALPHAVANTAGE_API_KEY"),
    }
    url = BASE_URL + "?" + urlencode(params)

    headers = {
        "User-Agent": "ADK-Explorations-Agent/1.0",
        "Accept": "application/json",
        "Content-Type": "application/json; charset=UTF-8",
    }

    try:
        time.sleep(0.1)
        response, content = http_obj.request(
            uri=url,
            method="GET",
            headers=headers,
        )

        if response.status == 200:
            return json.loads(content)
        else:
            return {"error": f"AlphaVantage API returned status {response.status}", "details": json.loads(content)}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

def get_daily_adjusted(symbol: str) -> dict:
    """Gets the daily adjusted time series for a given stock.

    Args:
        symbol: The stock ticker to look up.

    Returns:
        A dictionary containing the daily adjusted time series data.
    """
    return _alpha_vantage_query("TIME_SERIES_DAILY_ADJUSTED", symbol)

get_daily_adjusted_tool = FunctionTool(
    func=get_daily_adjusted,
)

all_stock_tools = [get_daily_adjusted_tool]