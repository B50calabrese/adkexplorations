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

    The only dependency is `google-adk`.

    ```bash
    pip install google-adk
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