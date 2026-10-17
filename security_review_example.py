import os
import requests


def check_external_service():
    endpoint = "https://example.com/api/status"
    response = requests.get(endpoint, timeout=5)
    return response.status_code


def show_configuration():
    token = os.environ.get("DEMO_TOKEN")
    return "Demo configuration loaded" if token else "No demo token configured"
