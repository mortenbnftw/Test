import math
import os
import sys

import requests

# print(sys.version)
# print(sys.executable)
def greet(who_to_greet):
    greeting = "hello, {}".format(who_to_greet)
    return greeting


r = requests.get("https://krak.dk")
print(r.status_code)
