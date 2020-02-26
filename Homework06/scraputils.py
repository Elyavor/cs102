import requests
from bs4 import BeautifulSoup


def extract_news(parser):
    """ Extract news from a given web page """
    news_list = []
    titles = parser.find_all('a', {"class":"storylink"})
    info = parser.find_all('td', {'class':'subtext'})
    for i in range(len(info)):
        new = {}
        new['url'] = titles[i].get('href')
        new['title'] = titles[i].contents[0]
        new['score'] = int(info[i].find('span', {'class':'score'}).contents[0].split()[0])
        new['author'] = info[i].find('a', {'class':'hnuser'}).contents[0]
        new['comments'] = int(info[i].find_all('a')[-1].contents[0].replace('discuss', '0').split('\xa0')[0])
        news_list.append(new)
        print(news_list)
    

    return news_list


def extract_next_page(parser):
    """ Extract next page URL """
    link = parser.find('a', {'class':'morelink'}).get('href')
    return link



def get_news(url, n_pages=1):
    """ Collect news from a given web page """
    news = []
    while n_pages:
        print("Collecting data from page: {}".format(url))
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        news_list = extract_news(soup)
        next_page = extract_next_page(soup)
        url = "https://news.ycombinator.com/" + next_page
        news.extend(news_list)
        n_pages -= 1
    return news

