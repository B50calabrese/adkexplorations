# ADK Explorations

This project is an exploration of Google's Agent Development Kit (ADK). It provides a basic structure for building a multi-agent system, starting with a main coordination agent.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python 3.9 or higher
*   A Google API key for Gemini. You can get one from [Google AI Studio](https://aistudio.google.com/apikey).

### Installation

1.  **Create and activate a virtual environment (recommended):**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

2.  **Install the required packages:**

    The dependencies are `google-adk`, `httplib2`, and `polygon-python-client`.

    ```bash
    pip install google-adk httplib2 polygon-python-client
    ```

### Configuration

1.  **Set up your API key:**

    In the `app/` directory, you will find a file named `.env.example`. Make a copy of this file and name it `.env`:

    ```bash
    cp app/.env.example app/.env
    ```

2.  **Add your API key to the `.env` file:**

    Open the `app/.env` file and replace `PASTE_YOUR_ACTUAL_API_KEY_HERE` with your actual Google API key.

    ```
    # app/.env
    GOOGLE_GENAI_USE_VERTEXAI=FALSE
    GOOGLE_API_KEY=YOUR_API_KEY_HERE
    ```

### Running the Agent

1.  **Navigate to the `app` directory:**

    ```bash
    cd app
    ```

2.  **Run the agent using the ADK web interface:**

    ```bash
    adk web
    ```

3.  Open your web browser and go to `http://localhost:8000`. You should see the `coordination_agent` listed and ready to interact with.

## Multi-Agent Architecture

This project uses a multi-agent architecture where a `coordination_agent` delegates tasks to specialized sub-agents. The four agents are:

### 1. Coordination Agent
The `coordination_agent` is the main entry point for user requests. It understands the user's intent and delegates tasks to the appropriate specialist agent. It has the following tools:
*   `google_search`: Searches the web for information.
*   `stock_agent`: A sub-agent that is an expert on the stock market.
*   `background_agent`: A sub-agent for performing long-running tasks.
*   `magic_agent`: A sub-agent that is an expert on Magic: The Gathering.

### 2. Stock Agent
The `stock_agent` is a specialist agent that handles all stock market related queries. It has the following tool:
*   `get_stock_price(ticker: str)`: Fetches the latest stock price for a given ticker symbol. Requires a `POLYGON_API_KEY` in the `.env` file.

### 3. Background Agent
The `background_agent` is a sub-agent that can perform long-running tasks, such as waiting for a condition to be met and then sending a notification. It has the following tools:
*   `wait(seconds: int)`: Waits for a specified number of seconds.
*   `send_google_chat_message(message: str)`: Sends a message to a Google Chat space. Requires a `GOOGLE_CHAT_WEBHOOK_URL` in the `.env` file.
*   `print_to_terminal(message: str)`: Prints a message to the terminal where the agent is running.
*   `stock_agent`: The specialist stock market agent, used for monitoring stock metrics.

### 4. Magic: The Gathering Agent
The `magic_agent` is a specialist agent that handles all queries about Magic: The Gathering. It has a comprehensive set of tools for interacting with the Scryfall API.

### Example Usage

You can ask the `coordination_agent` to perform various tasks, for example:

**Get a stock price:**
> "What is the stock price of GOOGL?"

The `coordination_agent` will delegate this task to the `stock_agent`.

**Perform a background task:**
> "Wait for 10 seconds and then send a message to Google Chat saying 'Task complete!'"

The `coordination_agent` will delegate this task to the `background_agent`.

**Monitor a stock price:**
> "Let me know when the price of GOOGL goes above $150."

The `coordination_agent` will delegate this task to the `background_agent`, which will then use the `stock_agent` to monitor the price.

**Ask a Magic: The Gathering question:**
> "Search for a card named 'Black Lotus'"

The `coordination_agent` will delegate this task to the `magic_agent`.