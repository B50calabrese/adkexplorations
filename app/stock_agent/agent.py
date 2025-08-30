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

"""Defines the stock market expert agent."""

from google.adk.agents import LlmAgent
from app.tools.stock_tool import stock_tool

stock_agent = LlmAgent(
    name='stock_agent',
    model='gemini-1.5-flash',
    description='An agent that is an expert on the stock market.',
    instruction=(
        'You are an expert on the stock market. Your purpose is to provide '
        'information about stock prices. You must use the get_stock_price '
        'tool to answer any questions about stock prices.'
    ),
    tools=[stock_tool],
)
