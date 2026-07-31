# .venv\Scripts\Activate.ps1

import requests
import json


username = input("Who are you looking for? ")

response = requests.get(f"https://api.github.com/users/{username}")
response.status_code
data = response.json()

user_info = {
    "login": data["login"],
    "name": data["name"],
    "bio": data["bio"],    
    "created_at": data["created_at"]
}

with open("github_response.json", "w") as file:
    json.dump(user_info, file, indent=4)

