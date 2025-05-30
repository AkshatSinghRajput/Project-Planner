from typing import List
from pydantic import BaseModel, Field


class TaskEstimate(BaseModel):
    task_name: str = Field(..., description="Name of the task")
    estimated_time_hours: float = Field(
        ..., description="Estimated time to complete the task in hours"
    )
    required_resources: List[str] = Field(
        ..., description="List of resources required to complete the task"
    )


class Milestone(BaseModel):
    milestone_name: str = Field(..., description="Name of the milestone")
    tasks: List[str] = Field(
        ..., description="List of task IDs associated with this milestone"
    )


class ProjectPlan(BaseModel):
    tasks: List[TaskEstimate] = Field(
        ..., description="List of tasks with their estimates"
    )
    milestones: List[Milestone] = Field(..., description="List of project milestones")


class ProjectInput(BaseModel):
    project_type: str = Field(
        ..., description="Type of the project (e.g., 'software', 'construction')"
    )
    project_objectives: str = Field(..., description="Objectives of the project")
    industry: str = Field(
        ..., description="Industry in which the project is being executed"
    )
    team_members: str = Field(
        ..., description="List of team members involved in the project"
    )
    project_requirements: str = Field(
        ..., description="Requirements and constraints of the project"
    )
