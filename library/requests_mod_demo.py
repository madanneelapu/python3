# accessing URL using requests module.

import requests

username = "madanneelapu"
resp = requests.get("https://api.github.com/users/" + username + "/repos")  # GET request
if resp.status_code == 200:  # HTTP Status Code
    repos = resp.json()  # convert response body to JSON.
    for r in repos:  # iterating over a list of dictionaries
        print(r["name"], "-", r["description"])

else:
    print("Sorry! User not found.")
