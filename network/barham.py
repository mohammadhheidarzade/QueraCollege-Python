import requests
def process(book):
    address = "http://127.0.0.1:8000/" + book['category'] + "/"
    if book in requests.get(address).json():
        return "bad query"
    requests.post(url=address, data=book)
