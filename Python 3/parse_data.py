from bs4 import BeautifulSoup

import requests
import lxml


def main():
    query = input("Aryan ? : ")
    headers = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}
    response = requests.get("https://www.google.com/search", params={"q" : query}, headers = headers)
    
    results = chimken_soup(response.content)
    return results

def chimken_soup(page):
    soup = BeautifulSoup(page, "lxml")
    names = soup.find_all("h3", class_ = "LC20lb DKV0Md")
    links = soup.find_all("cite", class_ = "iUh30 Zu0yb qLRx3b tjvcx")
    desc = soup.find_all("div", class_ = "VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc")
    parsed_data = [{"title":title.text, "link":link.text, "desc":desc.text} for title, link, desc in zip(names, links, desc)]
    return parsed_data
if __name__ == "__main__":
    main()
