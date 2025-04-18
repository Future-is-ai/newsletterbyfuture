#!/usr/bin/env python
import sys
import logging
import os

from datetime import datetime
from crewai_gcp.crew import CrewaiGcpCrew
from crewai_gcp import Mailing as mailing
from crewai_gcp.helpers.format_news_for_email import format_news_for_email
# vvv YAML Configuration vvv
current_date = datetime.now().strftime("%Y-%m-%d") # Include current date for context
replacements = {
    "current_date": current_date
}

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding necessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information
# from traceloop.sdk import Traceloop
# from opentelemetry.exporter.cloud_trace import CloudTraceSpanExporter

# from traceloop.sdk.decorators import workflow

# exporter = CloudTraceSpanExporter("sa-org-project")
# Traceloop.init(app_name="langchain_example", exporter=exporter)

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
# @workflow(name="run_aniftos")
def run():
    """
    Run the crew.
    """
    import json
    inputs = {"topic": "AI LLMs"}
    # res = CrewaiGcpCrew().crew().kickoff(inputs=inputs)
    #print(res.to_dict())
    
    service = mailing.gmail_authenticate()
    email_list = ["nathanph.brigot@gmail.com", "nathan.brigot@fr.ey.com"]
    # email_list = [
    #     "nathan.brigot@fr.ey.com",
    #     "nathanph.brigot@gmail.com",
    #     "antoine.bichon@fr.ey.com",
    #     "thibault.gouvier@fr.ey.com",
    #     "paul.ballet@fr.ey.com",
    #     "anne.marie.timar@fr.ey.com",
    #     "lynn.thoumy@fr.ey.com",
    #     "emeline.lahaye@fr.ey.com",
    #     "bilal.khatib@fr.ey.com",
    # ]
   
    # email_list = [
    #     "nathan.brigot@fr.ey.com",
    #     "lucas.treiber@fr.ey.com",
    #     "hamid.filali@fr.ey.com",
    #     "emeline.lahaye@fr.ey.com",
    #     "charlotte.cazelles@fr.ey.com",
    #     "aurelien.martin@fr.ey.com",
    #     "ange.bernard@fr.ey.com",
    #     "alexander.borisov@fr.ey.com" 
    # ]

    # for email in email_list:
    #     first_name = email.split('.')[0].capitalize()
    #     if bool(email) :
    #         mailing.send_message(service, [email.strip()], first_name + ", ton résumé quotidien de l’innovation 🔥", format_news_for_email(res.pydantic, current_date))

    # for email in email_list:
        # first_name = email.split('.')[0].capitalize()
        # if bool(email):
        #     email_content = format_news_for_email(res.pydantic, current_date)
            
        #     if len(email_content) >= 750:
        #         subject = f"{first_name}, ton résumé quotidien de l’innovation 🔥"
        #         mailing.send_message(service, [email.strip()], subject, email_content)
        #     else:
        #         print(f"Newsletter not sent to {email}: content too short ({len(email_content)} chars).")
    for root, dirs, files in os.walk("/"):
        for name in files:
            if "report_test3.md" in name:
                print(os.path.join(root, name))
                
    markdown_file_path = os.path.join('/workspaces/NathanVertex/src/crewai_gcp/helpers', 'report_test3.md')
    print(markdown_file_path)
    for email in email_list:
        print("Chemin courant :", os.getcwd())
        first_name = email.split('.')[0].capitalize()
        subject = f"{first_name}, Your daily dose of innovation is here 🔥"
        markdown_file_path = os.path.join('/code/src/crewai_gcp/helpers', 'report_test3.md')
        print(f"markdown_file_path : {markdown_file_path}")
        mailing.send_message_V2(service, [email.strip()], subject, markdown_file_path )




    # Generate markdown content
    # print("generate markdown contente")
    # markdown_content = generate_markdown(res.to_dict())

    # # Write to a .md file
    # with open("report.md", "w") as file:
    #     file.write(markdown_content)

    # print("Markdown file has been generated successfully.")
    # logging.info("this file has been generated successfully")

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

