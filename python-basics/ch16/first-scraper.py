from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"

page = urlopen(url)
print(type(page))

html_bytes = page.read()
print(type(html_bytes))
html = html_bytes.decode("utf-8") # a string
print(html)

# use string method to extract title
title_start_index = html.find("<title>") + len("<title>")
title_end_index = html.find("</title>")
title = html[title_start_index:title_end_index]
print(title)

# use regexes to extract text
import re
result = re.findall("ab*c", "ac")
print(result)

# see re.findall
s = "acc"
print(re.findall("a.*c", s))  # ['acc']
print(re.search("a.*c", s))  # <re.Match object; span=(0, 3), match='acc'>
s2 = re.search("a.*c", s)
print(s2.group())  # acc
print(s2.groups())