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

"""Defines the main coordination agent for the ADK explorations project."""

from google.adk.agents import Agent
from google.adk.tools import AgentTool
from google.adk.tools import google_search
from app.background_agent.agent import background_agent
from app.tools.stock_tool import stock_tool

background_agent_tool = AgentTool(agent=background_agent)

root_agent = Agent(
    name='coordination_agent',
    # Note: You may need to update the model to one that supports the features
    # you intend to use.
    model='gemini-1.5-flash',
    description='A coordination agent that can delegate tasks to other agents.',
    instruction=(
        'You are a coordination agent. Your purpose is to understand user '
        'requests and delegate them to the appropriate specialist agents. '
        'If a user asks for a task to be performed in the background, '
        'such as waiting and then sending a notification, you must use the '
        'background_agent tool. If a user asks for a stock price, you '
        'must use the get_stock_price tool.'
    ),
    tools=[google_search, background_agent_tool, stock_tool],
)
