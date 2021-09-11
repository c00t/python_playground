import mechanicalsoup
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
page = browser.get(url)
login_html = page.soup
# print(page.soup)

# get the form and input box
form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

# click the button to login
profile_page = browser.submit(form, page.url)
print(profile_page.url)
print(profile_page.soup.title.string)

# return to login page
