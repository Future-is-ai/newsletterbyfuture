import os
from google.cloud import aiplatform
from dotenv import load_dotenv

# Set the path to your service account key JSON file
load_dotenv()


import json

# Initialize Vertex AI client
project_id = os.getenv("GOOGLE_CLOUD_PROJECT")  # Replace with your Google Cloud Project ID
region = os.getenv("VERTEX_AI_LOCATION")          # Replace with your Vertex AI region (e.g., "us-central1")

aiplatform.init(project=project_id, location=region)

# Test the connection by listing available models
models = aiplatform.Model.list()
for model in models:
    print(f"Model Name: {model.display_name}, Model ID: {model.resource_name}") 
