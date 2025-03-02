# CLAUDE.md - Agent Instructions

## Commands
- Run app: `python main.py`
- Run tests: `pytest`
- Run single test: `pytest path/to/test.py::test_function`
- Linting: `flake8`
- Type checking: `mypy agent/ main.py`

## Code Style
- **Imports**: Group imports (stdlib, third-party, local) with blank line between groups
- **Typing**: Strong typing with annotations for function params and returns
- **Naming**: 
  - snake_case for variables/functions
  - PascalCase for classes/Pydantic models
  - UPPER_CASE for constants
- **Error handling**: Try/except blocks with specific exceptions, logging
- **Models**: Use Pydantic for data validation and serialization
- **Formatting**: Black formatter compatible: 88 character line limit
- **Documentation**: Docstrings for classes and non-trivial functions
- **Environment**: Use dotenv for configuration, settings via Pydantic

## Project Overview
This project creates an intelligent agent that answers questions about current events like weather and news. It uses 
OpenAI's GPT-4o-mini model for language processing and integrates with external APIs to fetch real-time data.