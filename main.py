import requests
from bs4 import BeautifulSoup

def print_hi(name):
    req = requests.get('https://blockchain.news/news/bakkt-president-adam-white-said-he-will-depart-from-bakkt-next-week')
    soup = BeautifulSoup(req.text, 'html.parser')
    element = soup.find('div', 'main col-sm-12')
    title = element.find('h1', 'title21')
    author = element.find("span", {"id": "author"})
    time_read = element.find('span', 'textdesc')
    print(title.text)
    print(author.text)
    print(time_read.text)
    post = element.find('div', 'textbody')
    paragraph = post.find_all('p')
    for p in paragraph:
        if p.find('img'):
            # сохрание картинки
            print('image')
        if p.text[:1] == '"':
            # сохранение цитаты
            print('quote')
        else:
            # сохраняем параграф
            print(p.text)
    tags = soup.find_all('button', 'btn tag-btn')
    for t in tags:
        # сохраняем теги
        print(t.text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
