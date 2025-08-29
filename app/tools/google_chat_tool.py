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

"""A tool for sending messages to Google Chat."""

import os
from json import dumps
from httplib2 import Http
from google.adk.tools import Tool

def send_google_chat_message(message: str) -> str:
    """Sends a message to a Google Chat space.

    Args:
        message: The message to send.

    Returns:
        A string indicating the result of the operation.
    """
    webhook_url = os.environ.get("GOOGLE_CHAT_WEBHOOK_URL")
    if not webhook_url:
        return "Error: GOOGLE_CHAT_WEBHOOK_URL environment variable not set."

    app_message = {"text": message}
    message_headers = {"Content-Type": "application/json; charset=UTF-8"}

    try:
        http_obj = Http()
        response, content = http_obj.request(
            uri=webhook_url,
            method="POST",
            headers=message_headers,
            body=dumps(app_message),
        )
        if response.status == 200:
            return f"Message sent successfully to Google Chat: {message}"
        else:
            return f"Error sending message to Google Chat: {response.status} {content}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

google_chat_tool = Tool(
    name="send_google_chat_message",
    description="Sends a message to a Google Chat space.",
    func=send_google_chat_message,
)
