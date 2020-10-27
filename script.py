import requests


r = requests.get("https://krak.dk")
print(r.status_code)
