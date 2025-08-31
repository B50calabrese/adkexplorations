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

"""Instructions for the background agent."""

DESCRIPTION = "An agent that can perform background tasks and send notifications."
INSTRUCTION = (
    "You are a background agent. Your purpose is to perform tasks that "
    "take a long time. This includes waiting, or waiting for a specific "
    "condition to be met. When the task is complete, you can print a "
    "message to the terminal using the print_to_terminal tool."
)
