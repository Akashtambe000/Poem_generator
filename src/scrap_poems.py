import requests
from bs4 import BeautifulSoup as Soup


def form_poems(url,poem_list):
    try:
        #form http request
        page = requests.get(url)
        soup = Soup(page.content,"html.parser")
        page.close()

    except:
        print("Error Occured While connecting to page ",url)
        return poem_list
    subsoup = list(soup.children)[2]
    child_soup = list(subsoup.children)[3]  #child_soup will contain the <body> element here

    soup1 = child_soup.find_all('td',class_="title")  #list containing element = 'td' and class = 'title' 
    soup1_length = len(soup1) #no of poems in this page
    for i in range(soup1_length):
        try:
            soup2 = list(soup1[i].children)[1] #soup2 will contain <a href=""> element
            poem_list.append((soup2.attrs.get('href'),soup2.get_text()))
        except:
            pass    

    soup3 = child_soup.find('div',class_="pagination mb-15")
    soup4 = soup3.find('li',class_="next")
    if soup4 is not None:
        soup5 = list(soup4.children)[0]
        url = "https://www.poemhunter.com" + soup5.attrs.get('href')
        form_poems(url,poem_list)
    return poem_list    

if __name__ == "__main__":
    poem_list = []
    form_poems("https://www.poemhunter.com/pablo-neruda/poems/",poem_list)
    print("No of Poems - ",len(poem_list),"\n")
    for poem in poem_list:
        print(poem)