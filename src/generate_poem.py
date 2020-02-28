import requests
from bs4 import BeautifulSoup as Soup

def copy_poems(url):
    try:
        #form http request
        page = requests.get(url)
        soup = Soup(page.content,"html.parser")
        page.close()

    except:
        print("Error Occured While connecting to page ",url)

    subsoup = list(soup.children)[2]
    child_soup = list(subsoup.children)[3]  #child_soup will contain the <body> element here
    soup3 = child_soup.find('div',class_="KonaBody")
    soup4 = soup3.find('p')
    soup5 = list(soup4.children)
    nosoup = [str(value) for value in soup5]
    nosoup = list(filter(lambda a: a != "<br/>", nosoup))
    return nosoup


if __name__ == "__main__":
    url = "https://www.poemhunter.com/poem/still-another-day-xvii-men/"
    url = "https://www.poemhunter.com/poem/the-fear-11/"
    url = "https://www.poemhunter.com/poem/annabel-lee/"
    copy_poems(url)    