import requests
from bs4 import BeautifulSoup as bs

url = "https://www.decathlon.rs/satori-za-2-osobe/331853-65669-sator-mh100-xl-fresh-black-za-2-osobe.html#/demodelundefined-8641759/demodelsize-254univerzalna_velicina?queryID=33c0378b7235727885ce980e4e06779b&objectID=4271869"


class Parser:
    def palatka_parse(url):
        r = requests.get(url)
        soup = bs(r.text, "html.parser")
        block = soup.find("div", class_="js-out-of-stock")
        block_text = block.find("button", class_="btn btn--disabled btn--add-to-cart").get_text()
        return 'Nije dostupno onlajn' not in  block_text 


if __name__ == "__main__":
    print(Parser.palatka_parse(url))
