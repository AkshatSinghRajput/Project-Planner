"""
crew.py
Professionalized and modularized Crew setup for Project Planner.
"""
import os
import yaml
from crewai import Agent, Crew, Task, LLM
from app.types.types import ProjectPlan

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, "config")

# LLM Initialization
llm = LLM(
    model="openai/gpt-4o",
    api_key=os.getenv("OPENAI_API_KEY"),
)

# Config file paths
CONFIG_FILES = {
    "agents": os.path.join(CONFIG_DIR, "agents.yaml"),
    "tasks": os.path.join(CONFIG_DIR, "tasks.yaml"),
}

def load_yaml_config(file_path: str) -> dict:
    """Load YAML configuration from a file."""
    with open(file_path, "r") as file:
        return yaml.safe_load(file)

def get_configs() -> dict:
    """Load all required configurations."""
    return {key: load_yaml_config(path) for key, path in CONFIG_FILES.items()}

# Load configurations
configs = get_configs()
agents_config = configs["agents"]
tasks_config = configs["tasks"]

# Agent creation
project_planning_agent = Agent(config=agents_config["project_planning_agent"])
estimation_agent = Agent(config=agents_config["estimation_agent"])
resource_allocation_agent = Agent(config=agents_config["resource_allocation_agent"])

# Task creation
task_breakdown = Task(
    config=tasks_config["task_breakdown"], agent=project_planning_agent
)
time_resource_estimation = Task(
    config=tasks_config["time_resource_estimation"], agent=estimation_agent
)
resource_allocation = Task(
    config=tasks_config["resource_allocation"],
    agent=resource_allocation_agent,
    output_pydantic=ProjectPlan,
)

# Crew assembly
crew = Crew(
    agents=[project_planning_agent, estimation_agent, resource_allocation_agent],
    tasks=[task_breakdown, time_resource_estimation, resource_allocation],
    verbose=True,
)
