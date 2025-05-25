# Project Planner

Project Planner is a modular, agent-based application designed to automate project planning, estimation, and resource allocation using AI agents. It leverages the CrewAI framework and OpenAI's GPT models to streamline the process of breaking down projects, estimating timelines and resources, and generating structured project plans.

## Features
- **Agent-based architecture:** Modular agents for project planning, estimation, and resource allocation.
- **Configurable:** Agents and tasks are defined in YAML files for easy customization.
- **Structured output:** Generates project plans as Pydantic models for integration with other systems.
- **Extensible:** Easily add new agents or tasks as your workflow evolves.

## Project Structure
```
app/
  main.py                # Main entry point
  streamlit_client.py    # Streamlit UI (if used)
  config/
    agents.yaml          # Agent configurations
    tasks.yaml           # Task configurations
  crews/
    crew.py              # Crew and agent/task setup
  types/
    types.py             # Pydantic models and type definitions
run.py                   # Script to run the application
requirements.txt         # Python dependencies
```

## Getting Started

### Prerequisites
- Python 3.10+
- OpenAI API key (for GPT-4o)

### Installation
1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd Project\ Planner
   ```
2. Create a virtual environment and activate it:
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set your OpenAI API key:
   ```sh
   export OPENAI_API_KEY=your-api-key
   ```

### Configuration
- Edit `app/config/agents.yaml` and `app/config/tasks.yaml` to customize agent behaviors and task definitions.

### Running the Application
- To run the backend logic:
  ```sh
  python run.py
  ```
- If using the Streamlit client:
  ```sh
  streamlit run app/streamlit_client.py
  ```

## File Overview
- `app/crews/crew.py`: Loads agent/task configs, initializes agents, tasks, and assembles the Crew.
- `app/types/types.py`: Defines the `ProjectPlan` Pydantic model for structured output.
- `app/config/agents.yaml` & `tasks.yaml`: YAML files for agent/task configuration.
- `run.py`: Main script to launch the application.

## Customization
- Add new agents or tasks by updating the YAML config files and extending the Python setup in `crew.py`.
- Integrate with other tools or UIs as needed.

## License
[MIT License](LICENSE)

## Acknowledgements
- [CrewAI](https://github.com/joaomdmoura/crewAI)
- [OpenAI GPT](https://platform.openai.com/docs/models)

---
For questions or contributions, please open an issue or pull request.
