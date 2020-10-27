import requests

r = requests.get("https://krak.dk")
# Little change
print(r.status_code)
