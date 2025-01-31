#!/usr/bin/env python
import sys
from crewai_gcp.crew import CrewaiGcpCrew
from crewai_gcp import Mailing as mailing

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding necessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information
# from traceloop.sdk import Traceloop
# from opentelemetry.exporter.cloud_trace import CloudTraceSpanExporter

# from traceloop.sdk.decorators import workflow

# exporter = CloudTraceSpanExporter("sa-org-project")
# Traceloop.init(app_name="langchain_example", exporter=exporter)


# @workflow(name="run_aniftos")
def run():
    """
    Run the crew.
    """
    import json
    inputs = {"topic": "AI LLMs"}
    res = CrewaiGcpCrew().crew().kickoff(inputs=inputs)
    #print(res.to_dict())

    def generate_markdown(data):
        md_content = ""
        for entry in data['results']:
            headline = entry['headline']
            description = entry['description']
            md_content += f"## {headline}\n\n{description}\n\n"
            md_content += "### Sources:\n"
            for source in entry['source']:
                md_content += f"- [{source['name']}]({source['url']})\n"
            md_content += "\n"  # Add a newline between entries
        return md_content

    # Generate markdown content
    markdown_content = generate_markdown(res.to_dict())

    # Write to a .md file
    with open("report.md", "w") as file:
        file.write(markdown_content)
        
    #service = mailing.gmail_authenticate()
    #mailing.send_message(service, "lucas.treiber@fr.ey.com", "Newsletter about AI LLMs", markdown_content)

    print("Markdown file has been generated successfully.")

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {"topic": "AI LLMs"}
    try:
        CrewaiGcpCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CrewaiGcpCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

