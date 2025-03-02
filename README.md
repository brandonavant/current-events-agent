# Current Events Agent

An intelligent agent that answers questions about current events, including weather and news updates.

## Overview

This project demonstrates how to build a conversational AI agent using OpenAI's GPT models. The agent:

1. Processes natural language queries about weather and news
2. Uses "thought chains" to determine the appropriate action to take
3. Interacts with external APIs to fetch real-time data
4. Responds with helpful, contextual information

## Features

- 🌦️ **Weather updates** - Get current weather conditions for any location
- 📰 **News briefings** - Retrieve the latest news on any topic
- 🧠 **Intelligent processing** - Uses LLM to understand requests and plan responses

## Quick Start

### Prerequisites

- Python 3.8+
- OpenAI API key
- News API token

### Installation

1. Clone the repository
```bash
git clone https://github.com/brandonavant/current-events-agent.git
cd current-events-agent
```

2. Create a virtual environment and install dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your API keys:
```bash
# Copy the example file
cp .env.example .env

# Then edit .env with your actual API keys
```

### Usage

Run the agent with a sample query:
```bash
python main.py
```

To customize the query, edit the `user_inquiry` in `main.py`.

## Project Structure

```
current-events-agent/
├── agent/                 # Core agent functionality
│   ├── actions.py         # API interaction implementations
│   ├── clients.py         # API client wrappers
│   ├── common.py          # Shared utilities and logging
│   ├── config.py          # Configuration and settings
│   ├── constants.py       # System constants
│   ├── models.py          # Pydantic data models
│   └── processing.py      # Query processing and action invocation
├── .env.example           # Template for environment variables
├── .gitignore             # Git ignore file
├── CLAUDE.md              # Documentation for agentic coding tools
├── LICENSE                # MIT License
├── main.py                # Application entry point
└── requirements.txt       # Python dependencies
```

## License

MIT

