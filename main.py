import requests
from bs4 import BeautifulSoup

cookies = {"SOCS": "CAESHAgCEhJnd3NfMjAyMjEyMDUtMF9SQzMaAnN2IAEaBgiAvI6dBg"}
url = "https://www.google.com/search?q=webbyr%C3%A5+stockholm&sxsrf=ALiCzsaKh7hYMT2WYQRMpodBQ-QkGeIWPw%3A1671741179214&ei=-76kY_LaDI2arwT274moDw&oq=webbyr%C3%A5&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgBMggIABCABBDJAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBAgAEEMyBQgAEIAEMgUIABCABDILCC4QrwEQxwEQgAQyBQgAEIAEOgoIABBHENYEELADOgcIIxCwAhAnOgYIABAWEB46BwgjEOoCECc6BAgjECc6BggjECcQEzoLCAAQgAQQsQMQgwE6CAguEIMBELEDOgsILhCABBCxAxCDAToICAAQgAQQsQM6BwgjECcQnQI6CwguEIMBELEDEIAEOhAILhCxAxCDARDHARDRAxBDOg4ILhCABBCxAxDHARDRAzoKCC4QxwEQrwEQQzoKCC4QxwEQ0QMQQzoHCCMQsQIQJzoLCAAQgAQQsQMQyQM6CggAELEDEIMBEENKBAhBGABKBAhGGABQ7wZY1CBg9UJoAnABeAKAAaMCiAGODZIBBjE5LjEuMZgBAKABAbABCsgBCMABAQ&sclient=gws-wiz-serp"

google = requests.get(
    url, headers={"User-Agent": "Mozilla/5.0"}, cookies=cookies).text

soup = BeautifulSoup(google, "html.parser")

a_tags = soup.find_all('a')

index = 1
top_sites = []
for tag in a_tags:
    info = {}
    if tag['href'] == "#":
        continue
    if tag['href'].find("google") != -1:
        continue
    if tag['href'].find("search") != -1:
        continue
    if tag.div == None:
        continue
    info["index"] = index
    info["google_text"] = tag.find('h3').text
    info["url"] = tag['href'].split("&")[0].split("=")[1]
    index += 1
    top_sites.append(info)

for site in top_sites:
    agency = requests.get(site["url"])
    if agency.status_code != 200:
        site["status"] = "Blocked"
        continue

    site["status"] = "OK"

    agency_soup = BeautifulSoup(agency.text, "html.parser")

    meta = agency_soup.find_all('meta')
    print(meta)
    break


for site in top_sites:
    break
    print(site)
