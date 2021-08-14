import requests
resp = requests.get("http://olympus.realpython.org")#It's a sync operation?
html = resp.text
# default behavior change in python 3.9?
# my result:
# <h2>Please log in to access Mount Olympus:</h2
# book result:
# <h2>Please log in to access Mount Olympus:</h2>
print(html[86:132])