# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law of a an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A tool for waiting a specified amount of time."""

import time
from google.adk.tools import Tool

def wait(seconds: int) -> str:
    """Waits for a specified number of seconds.

    Args:
        seconds: The number of seconds to wait.

    Returns:
        A string indicating that the wait is complete.
    """
    time.sleep(seconds)
    return f"Waited for {seconds} seconds."

wait_tool = Tool(
    name="wait",
    description="Waits for a specified number of seconds.",
    func=wait,
)
