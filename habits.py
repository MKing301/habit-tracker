import os
import requests
import datetime

from rich.console import Console
from rich.prompt import Prompt
from dotenv import load_dotenv


# Resources
# https://pixe.la/
# https://docs.pixe.la/entry/post-user

load_dotenv()
console = Console()
prompt = Prompt()


USERNAME = os.getenv('UNAME')
TOKEN = os.getenv('TOKEN')
GRAPH_ID = os.getenv('GRAPH_ID')
pixela_endpoint = 'https://pixe.la/v1/users'

console.print(USERNAME)

user_params = {
    "token": TOKEN,
    "username": USERNAME,

    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Create user account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Create graph
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# Create graph
# response = requests.post(
#   url=graph_endpoint, json=graph_config, headers=headers
# )
# print(response.text)

# Graph url
# https://pixe.la/v1/users/maevki/graphs/graph1.html

pixel_creation_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

pixel_data = {
    "date": datetime.datetime.now().strftime('%Y%m%d'),
    "quantity": prompt.ask("How many hours did you code today?"),
}

response = requests.post(
    url=pixel_creation_endpoint, json=pixel_data, headers=headers
)
console.print(response.text)

