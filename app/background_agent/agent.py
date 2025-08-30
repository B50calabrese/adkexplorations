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

"""Defines the background agent for performing long-running tasks."""

from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool
from app.stock_agent.agent import stock_agent
from app.tools.google_chat_tool import google_chat_tool
from app.tools.terminal_tool import terminal_tool
from app.tools.wait_tool import wait_tool

stock_agent_tool = AgentTool(agent=stock_agent)

background_agent = LlmAgent(
    name='background_agent',
    model='gemini-1.5-flash',
    description='An agent that can perform background tasks and send notifications.',
    instruction=(
        'You are a background agent. Your purpose is to perform tasks that '
        'take a long time. This includes waiting, or waiting for a specific '
        'condition to be met. If you are asked to wait for a stock market '
        'metric, you must use the stock_agent tool to check the metric, '
        'and the wait tool to pause between checks. When the task is complete, '
        'you can send a notification using the send_google_chat_message '
        'tool or print a message to the terminal using the print_to_terminal '
        'tool.'
    ),
    tools=[google_chat_tool, wait_tool, terminal_tool, stock_agent_tool],
)
