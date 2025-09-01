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
from typing import Optional

BASE_URL = "https://www.alphavantage.co/query"

def _alpha_vantage_query(params: dict) -> dict:
    """Makes a request to the AlphaVantage API and returns the JSON response.

    Args:
        params: A dictionary of query parameters to include in the request.

    Returns:
        A dictionary containing the JSON response from the API.
    """
    http_obj = Http()
    params["apikey"] = os.environ.get("ALPHAVANTAGE_API_KEY")
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
    params = {"function": "TIME_SERIES_DAILY_ADJUSTED", "symbol": symbol}
    return _alpha_vantage_query(params)

get_daily_adjusted_tool = FunctionTool(
    func=get_daily_adjusted,
)

def get_news_sentiment(
    tickers: Optional[str] = None,
    topics: Optional[str] = None,
    time_from: Optional[str] = None,
    time_to: Optional[str] = None,
    sort: Optional[str] = None,
    limit: Optional[int] = None,
) -> dict:
    """
    Gets news and sentiment data from the AlphaVantage API.

    Args:
        tickers: The stock/crypto/forex symbols to search for.
        topics: The news topics to search for.
        time_from: The start time for the search.
        time_to: The end time for the search.
        sort: The sort order for the results.
        limit: The maximum number of results to return.

    Returns:
        A dictionary containing the news and sentiment data.
    """
    params = {"function": "NEWS_SENTIMENT"}
    if tickers:
        params["tickers"] = tickers
    if topics:
        params["topics"] = topics
    if time_from:
        params["time_from"] = time_from
    if time_to:
        params["time_to"] = time_to
    if sort:
        params["sort"] = sort
    if limit:
        params["limit"] = limit
    return _alpha_vantage_query(params)

get_news_sentiment_tool = FunctionTool(
    func=get_news_sentiment,
)

all_stock_tools = [get_daily_adjusted_tool, get_news_sentiment_tool]