from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# print(soup.get_text())
# print(soup.find_all("img"))
image1, image2 = soup.find_all("img")
print(image1.name)
print(image1["src"])
print(image2["src"])

url2 = "http://olympus.realpython.org/profiles"
page2 = urlopen(url2)
html2 = page2.read().decode("utf-8")
soup2 = BeautifulSoup(html2, "html.parser")

a_list = soup2.find_all("a")
print(a_list)
a_href_list = [i["href"] for i in a_list]
print(a_href_list)
a_url_list = ["http://olympus.realpython.org" + i for i in a_href_list]
for url2 in a_url_list:
    html3 = urlopen(url2).read().decode("utf-8")
    soup3 = BeautifulSoup(html3)
    print(soup3.get_text())

# test global var scope
print(url2)
# 在for中修改的量，最终也会修改到全局变量
# for 中不会自己新声明一个scope
print(globals())