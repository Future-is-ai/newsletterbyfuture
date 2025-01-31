from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task, llm
#from langchain_google_vertexai import VertexAI
from application_schema import news_results as AS
from dotenv import load_dotenv
import os
# Set the path to your service account key JSON file
load_dotenv()
from crewai_tools import ScrapeWebsiteTool

scrape_web_tool = ScrapeWebsiteTool()

@CrewBase
class CrewaiGcpCrew:
    """CrewaiGcp crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # defining the VertexAI Gemini model
    @llm
    def gemini_llm(self):
        return LLM(
        model="gemini/gemini-2.0-flash-exp",
        api_key=os.getenv("VERTEX_AI_API_KEY"),
        #base_url="https://europe-west9-aiplatform.googleapis.com/"
        )

        #for local LLM => llm = LLM(
        #model="ollama/{model_name}",
        #base_url="http://localhost:{local_port_number_for_Ollama_serving}/"
        #)

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            # tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
            tools=[scrape_web_tool],
            verbose=True,
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["reporting_analyst"],
            verbose=True,
            tools=[scrape_web_tool],
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"],
            agent=self.researcher(), 
            output_pydantic=AS.NewsResults
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config["reporting_task"],
            agent=self.reporting_analyst(),
            output_pydantic=AS.NewsResults, 
            output_file="report.md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CrewaiGcp crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            share_crew=False,
            # memory=True,
            # planning=True,
            # planning_llm=self.gemini_llm(),
            # embedder={
            #     "provider": "vertexai",
            #     "config": {"model": "textembedding-gecko@003"},
            # },
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
