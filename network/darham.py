import requests

def process(url):
    response = requests.get(url)
    if response.status_code != 200:
        return "Bad Query"
    books = response.json()
    name = ""
    for book in books:
        if name == "":
            name = book['category']
            continue
        if book['category'] != name:
            return "I can't recognize it"
    if name == "":
        return "I can't recognize it"
    return name

