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
from app.tools.google_chat_tool import google_chat_tool
from app.tools.wait_tool import wait_tool

background_agent = LlmAgent(
    name='background_agent',
    model='gemini-1.5-flash',
    description='An agent that can perform background tasks and send notifications.',
    instruction=(
        'You are a background agent. Your purpose is to perform tasks that '
        'take a long time, such as waiting or calling an external API. '
        'When the task is complete, you must use the send_google_chat_message '
        'tool to send a notification.'
    ),
    tools=[google_chat_tool, wait_tool],
)
