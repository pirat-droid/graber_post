import datetime
import time
import transliterate
from mtranslate import translate
import requests
from bs4 import BeautifulSoup
import connect_db


def main():
    cnh_db = connect_db.DbCNH()
    req = requests.get('https://blockchain.news/news/bakkt-president-adam-white-said-he-will-depart-from-bakkt-next-week')
    # добавить аккаунты
    # выбрать рандомный аккаунт
    soup = BeautifulSoup(req.text, 'html.parser')
    element = soup.find('div', 'main col-sm-12')
    title = translate(element.find('h1', 'title21').text, 'ru')
    print(title)
    slug_t = transliterate.translit(title, reversed=True).replace(' ', '-')
    print(slug_t)
    # скачать картинку
    # сохранить картинку в базу
    time.sleep(5000)
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
    list_tags = []
    for t in tags:
        # сохраняем теги если их не было в базе
        list_tags.append(t.text)
        if not cnh_db.select(f"SELECT ID FROM blog_tagmodel WHERE slug = '{t.text}'"):
            # переводим теги
            tag_name = translate(t.text, 'ru')
            cnh_db.insert('''INSERT INTO blog_tagmodel (name, slug, datetime_create, datetime_update)
                             VALUES (%s, %s, %s, %s)''',
                          (tag_name, t.text, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                           datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            # лог записываем о добавлении нового тега
            time.sleep(2)


if __name__ == '__main__':
    main()
