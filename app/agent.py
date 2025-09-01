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
from app.background_agent.agent import background_agent
from app.magic_agent.agent import magic_agent
from app.stock_agent.agent import stock_agent
from app.shared import constants
from app import instructions
from app.tools.terminal_tool import terminal_tool

background_agent_tool = AgentTool(agent=background_agent)
magic_agent_tool = AgentTool(agent=magic_agent)
stock_agent_tool = AgentTool(agent=stock_agent)

root_agent = Agent(
    name="coordination_agent",
    # Note: You may need to update the model to one that supports the features
    # you intend to use.
    model=constants.AGENT_MODEL,
    description=instructions.DESCRIPTION,
    instruction=instructions.INSTRUCTION,
    tools=[background_agent_tool, magic_agent_tool, stock_agent_tool, terminal_tool],
)
