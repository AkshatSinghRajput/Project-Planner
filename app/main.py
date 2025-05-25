from fastapi import FastAPI, HTTPException
import uvicorn
from dotenv import load_dotenv
from app.crews.crew import crew as ProjectPlannerCrew
from app.types.types import ProjectInput

app = FastAPI()

# Load environment variables from .env file
load_dotenv()


@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


@app.get("/health")
async def health_check():
    try:
        # Simulate a health check
        return {"status": "healthy"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/plan-project")
async def plan_project(project_data: ProjectInput):
    try:

        result = ProjectPlannerCrew.kickoff(
            inputs={
                "project_type": project_data.project_type,
                "project_objectives": project_data.project_objectives,
                "industry": project_data.industry,
                "team_members": project_data.team_members,
                "project_requirements": project_data.project_requirements,
            }
        )
        return result

    except Exception as e:
        print(f"Error during project planning: {e}")
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
