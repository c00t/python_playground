from urllib.request import urlopen
import re

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
print(title)
sub_pattern = "<.*?>"
title = re.sub(sub_pattern, "", title, flags=re.IGNORECASE)
print(title)
