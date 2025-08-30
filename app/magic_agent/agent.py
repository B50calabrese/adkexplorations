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

"""Defines the Magic: The Gathering expert agent."""

from google.adk.agents import LlmAgent
from app.tools import scryfall_tool

magic_agent = LlmAgent(
    name='magic_agent',
    model='gemini-1.5-flash',
    description='An agent that is an expert on Magic: The Gathering.',
    instruction=(
        'You are an expert on Magic: The Gathering. Your purpose is to provide '
        'information about cards, sets, and other game-related topics. You must '
        'use the available tools to answer any questions.'
    ),
    tools=scryfall_tool.all_scryfall_tools,
)
