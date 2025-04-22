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

    # email_list_archi = [
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

# email_list = [
#     "achraf.sanhaji@fr.ey.com",
#     "alexander.borisov@fr.ey.com",
#     "alexandre.fougeres@fr.ey.com",
#     "ambrine.masson@fr.ey.com",
#     "amer.taleb.al.ajouz@fr.ey.com",
#     "ange.bernard@fr.ey.com",
#     "anne.marie.timar@fr.ey.com",
#     "antoine.chezaubernard@fr.ey.com",
#     "apolline.rajaonarison@fr.ey.com",
#     "aurelien.martin@fr.ey.com",
#     "bilal.khatib@fr.ey.com",
#     "camille.gal@fr.ey.com",
#     "celia.chabrant@fr.ey.com",
#     "celine.lim@fr.ey.com",
#     "charles.servel@fr.ey.com",
#     "charlotte.cazelles@fr.ey.com",
#     "claire.szczerbowski@fr.ey.com",
#     "clement.delfini@fr.ey.com",
#     "david.neftel@fr.ey.com",
#     "dimitri.paimparay@fr.ey.com",
#     "emeline.lahaye@fr.ey.com",
#     "emmanuel.layot@fr.ey.com",
#     "emna.turki@fr.ey.com",
#     "eugenie.laborde@fr.ey.com",
#     "ghislain.halatre@fr.ey.com",
#     "ghizlane.alami.badaoui@fr.ey.com",
#     "guillaume.herbelin@fr.ey.com",
#     "hamid.filali@fr.ey.com",
#     "helene.marque@fr.ey.com",
#     "hugues.lorez@fr.ey.com",
#     "ines.jaidane2@fr.ey.com",
#     "iouri.dadhemar.de.cransac@fr.ey.com",
#     "isabelle.yang@fr.ey.com",
#     "joseph.harari@fr.ey.com",
#     "julien.achrafi@fr.ey.com",
#     "julien.lejeune@fr.ey.com",
#     "juliette.piccolin@fr.ey.com",
#     "juliette.vallat@fr.ey.com",
#     "karine.ferus@fr.ey.com",
#     "khadija.jaber@fr.ey.com",
#     "laziza.bellahbib@fr.ey.com",
#     "leo.cadiou@fr.ey.com",
#     "lucas.treiber@fr.ey.com",
#     "lynn.thoumy@fr.ey.com",
#     "marie.astrid.reverdy@fr.ey.com",
#     "marin.lavigne@fr.ey.com",
#     "martin.harb@fr.ey.com",
#     "matthieu.bouix@fr.ey.com",
#     "meriem.abid1@fr.ey.com",
#     "myriam.monteilhet@fr.ey.com",
#     "nathan.brigot@fr.ey.com",
#     "nell.souryadhay@fr.ey.com",
#     "nicolas.seauve@fr.ey.com",
#     "ombeline.furet@fr.ey.com",
#     "paul.ballet@fr.ey.com",
#     "paul.henri.behague@fr.ey.com",
#     "philippine.perrier@fr.ey.com",
#     "sarah.snoussi@fr.ey.com",
#     "sebastien.courcambeck@fr.ey.com",
#     "sophie.diallo@fr.ey.com",
#     "sosthene.lapeze@fr.ey.com",
#     "taki.eddine.chalbi@fr.ey.com",
#     "thibault.gouvier@fr.ey.com",
#     "thibault.klajzyngier@fr.ey.com",
#     "toufik.hartani@fr.ey.com"
# ]

    email_list = ["nathanph.brigot@gmail.com", "nathan.brigot@fr.ey.com"]
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
    # for root, dirs, files in os.walk("/"):
    #     for name in files:
    #         if "report_test3.md" in name:
    #             print(os.path.join(root, name))
                
    markdown_file_path = os.path.join('/workspaces/NathanVertex/src/crewai_gcp/helpers', 'report_test3.md')
    print(markdown_file_path)
    for email in email_list:
        print("Chemin courant :", os.getcwd())
        first_name = email.split('.')[0].capitalize()
        subject = f"{first_name}, Your daily dose of innovation is here 🔥"
        # chemin cloud
        markdown_file_path = os.path.join('/code/src/crewai_gcp/helpers', 'report_test3.md')
        # chemin local
        # markdown_file_path = os.path.join('/workspaces/NathanVertex/src/crewai_gcp/helpers', 'report_test3.md')
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

