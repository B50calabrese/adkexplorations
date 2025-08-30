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

"""A tool for printing messages to the terminal."""

from google.adk.tools import Tool

def print_to_terminal(message: str) -> str:
    """Prints a message to the terminal.

    Args:
        message: The message to print.

    Returns:
        A string confirming that the message was printed.
    """
    print(f"Message from agent: {message}")
    return "Message printed to terminal."

terminal_tool = Tool(
    name="print_to_terminal",
    description="Prints a message to the terminal.",
    func=print_to_terminal,
)
