import re
import requests
from bs4 import BeautifulSoup


def foo(url):
    response = requests.get(url)
    response.raise_for_status()
    text = response.text
    soup = BeautifulSoup(text, features='html.parser')
    dict_1 = {}
    keywords = ['дизайн', 'фото', 'web', 'python']
    keywords_with_a_capital_letter = []
    for word in keywords:
        x = word.capitalize()
        keywords_with_a_capital_letter.append(x)
    common_keywords = keywords + keywords_with_a_capital_letter
    for keyword in common_keywords:
        terms = soup.find('div', class_='tm-articles-list').find_all(string=re.compile('\\b' + keyword + '\\b'))
        for txt in terms:
            time = txt.find_previous('span', class_='tm-article-snippet__datetime-published').text
            list_1 = []
            title = txt.find_previous('a', class_='tm-article-snippet__title-link').text
            list_1.append(title)
            link = 'https://habr.com' + txt.find_previous('a').get('href')
            list_1.append(link)
            dict_1[time] = list_1
    return dict_1


if __name__ == '__main__':
    print(foo('https://habr.com/ru/all/'))
