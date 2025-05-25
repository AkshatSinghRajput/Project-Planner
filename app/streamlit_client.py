import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from typing import Dict, Any
from crews.crew import crew as ProjectPlannerCrew

# Load environment variables
load_dotenv()

# Configure page settings
st.set_page_config(page_title="Project Planner", page_icon="📋", layout="wide")


def process_project_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Process project data using the ProjectPlannerCrew directly."""
    try:
        result = ProjectPlannerCrew.kickoff(inputs=data)

        result = result.pydantic.dict()

        # Calculate costs
        costs = (
            0.150
            * (
                ProjectPlannerCrew.usage_metrics.prompt_tokens
                + ProjectPlannerCrew.usage_metrics.completion_tokens
            )
            / 1_000_000
        )

        return result, costs, ProjectPlannerCrew.usage_metrics
    except Exception as e:
        st.error(f"Error during project planning: {str(e)}")
        return None, None, None


def main():
    st.title("🚀 Project Planner")
    st.write("Enter your project details below to get a comprehensive project plan.")

    with st.form("project_form"):
        # Project Type
        project_type = st.text_input(
            "Project Type",
            placeholder="e.g., software, construction, marketing",
            help="Enter the type of project you want to plan",
        )

        # Project Objectives
        project_objectives = st.text_area(
            "Project Objectives",
            placeholder="What are the main goals and objectives of your project?",
            help="Clearly state what you want to achieve with this project",
        )

        # Industry
        industry = st.text_input(
            "Industry",
            placeholder="e.g., Technology, Healthcare, Finance",
            help="Enter the industry sector for this project",
        )

        # Team Members
        team_members = st.text_area(
            "Team Members",
            placeholder="List your team members and their roles\nExample:\nJohn Doe - Senior Developer\nJane Smith - Project Manager",
            help="Enter the team members who will be working on this project",
        )

        # Project Requirements
        project_requirements = st.text_area(
            "Project Requirements",
            placeholder="List the key requirements and constraints for your project",
            help="Include both functional and non-functional requirements",
        )

        submitted = st.form_submit_button("Generate Project Plan")

        if submitted:
            if not all(
                [
                    project_type,
                    project_objectives,
                    industry,
                    team_members,
                    project_requirements,
                ]
            ):
                st.error("Please fill in all fields before submitting.")
                return

            with st.spinner(
                "Generating your project plan... This may take a few minutes..."
            ):
                project_data = {
                    "project_type": project_type,
                    "project_objectives": project_objectives,
                    "industry": industry,
                    "team_members": team_members,
                    "project_requirements": project_requirements,
                }

                result, costs, usage_metrics = process_project_data(project_data)

                if result:
                    st.success("Project plan generated successfully!")

                    # Display Usage Metrics
                    st.header("📊 Usage Metrics")
                    st.metric("Total Cost", f"${costs:.4f}")
                    if usage_metrics:
                        df_usage_metrics = pd.DataFrame([usage_metrics.dict()])
                        st.dataframe(df_usage_metrics)

                    # Display Tasks
                    st.header("📋 Tasks")
                    tasks = result["tasks"]
                    df_tasks = pd.DataFrame(tasks)
                    st.dataframe(
                        df_tasks.style.set_table_attributes('border="1"')
                        .set_caption("Task Details")
                        .set_table_styles(
                            [{"selector": "th, td", "props": [("font-size", "120%")]}]
                        )
                    )

                    # Display Milestones
                    st.header("🏁 Milestones")
                    milestones = result["milestones"]
                    df_milestones = pd.DataFrame(milestones)
                    st.dataframe(
                        df_milestones.style.set_table_attributes('border="1"')
                        .set_caption("Milestone Details")
                        .set_table_styles(
                            [{"selector": "th, td", "props": [("font-size", "120%")]}]
                        )
                    )

                    # Calculate and display total estimated time
                    total_time = df_tasks["estimated_time_hours"].sum()
                    st.metric(
                        "Total Estimated Project Duration", f"{total_time:.1f} hours"
                    )


if __name__ == "__main__":
    main()
