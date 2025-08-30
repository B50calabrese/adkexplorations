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

"""A tool for fetching stock prices."""

import os
from google.adk.tools import Tool
from polygon import RESTClient

def get_stock_price(ticker: str) -> str:
    """Fetches the latest stock price for a given ticker symbol.

    Args:
        ticker: The stock ticker symbol (e.g., "AAPL" for Apple).

    Returns:
        A string containing the stock price, or an error message.
    """
    api_key = os.environ.get("POLYGON_API_KEY")
    if not api_key:
        return "Error: POLYGON_API_KEY environment variable not set."

    try:
        with RESTClient(api_key) as client:
            resp = client.get_real_time_stock_prices(tickers=[ticker])
            if hasattr(resp, 'aggs') and resp.aggs:
                price = resp.aggs[0].close
                return f"The latest price for {ticker} is ${price}."
            else:
                return f"Could not find stock price for ticker: {ticker}"

    except Exception as e:
        return f"An unexpected error occurred: {e}"

stock_tool = Tool(
    name="get_stock_price",
    description="Fetches the latest stock price for a given ticker symbol.",
    func=get_stock_price,
)
