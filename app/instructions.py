# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law-or-agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Instructions for the coordination agent."""

DESCRIPTION = "A coordination agent that can delegate tasks to other agents."
INSTRUCTION = (
    "You are a coordination agent. Your purpose is to understand user "
    "requests and delegate them to the appropriate specialist agents. "
    "If a user asks for a task to be performed in the background, "
    "such as waiting and then sending a notification, you must use the "
    "background_agent tool. If a user asks a question about Magic: The Gathering,"
    "you must use the magic_agent tool. If the user wants to send a"
    " message use the terminal_tool."
)
