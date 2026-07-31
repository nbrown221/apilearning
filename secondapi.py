import requests
import json
url = input("Enter the URL: ")


headers = {
    "User-Agent": "Nick-Learning-API"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    try: 
        data = response.json()
        print(data)
        print(type(data))
        print(f"Request was successful.{response.status_code}")
        with open("api_response.json", "w") as file:
            json.dump(data, file, indent=4)
    except ValueError:
        print("Response content is not valid JSON.")
else: 

    print(f"Request failed with status code: {response.status_code}")

