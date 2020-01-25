import json
import xml.etree.ElementTree as ET
import re

def get_words_from_json():
    """
    Возвращает из файла json словарь {слово длиной 6 и более символов: количество повторений} 
    """
    
    with open('newsafr.json') as news_file:
        news_dict = json.load(news_file)    
    words_dict = {}
    for foo in news_dict["rss"]["channel"]["items"]:
        for word in re.findall("\w{6,}", foo["description"]):
            words_dict.setdefault(word, 0)
            words_dict[word] += 1

    return words_dict

def get_words_from_xml():
    """
    Возвращает из файла xml словарь {слово длиной 6 и более символов: количество повторений} 
    """
    tree = ET.parse('newsafr.xml')
    root = tree.getroot()
    xml_items = root.findall("channel/item/description")
    words_dict = {}
    for xmli in xml_items:
        for word in re.findall("\w{6,}", xmli.text):
            words_dict.setdefault(word, 0)
            words_dict[word] += 1

    return words_dict

def get_top_words(words, count=10):
    words = sorted(words.items(), key=lambda bar: bar[1], reverse=True)
    #[print(words[bar]) for bar in range (count)]
    return [words[bar] for bar in range (count)]

def my_print(list_of_tuples):
    print('№. Слово: Количество')
    [print(f'{list_of_tuples.index(bar)+1}. {bar[0]}: {bar[1]}') for bar in list_of_tuples]

if __name__ == '__main__':

    print('Программа, которая покажет вам топ-10 наиболее встречающихся слов из файлов json и xml')
    while True:
        user_choice = input('\nВведите 1 для json, 2 для xml, Enter для выхода: ').strip()
        if user_choice =='1':
            my_print(get_top_words(get_words_from_json()))
        elif user_choice =='2':
            my_print(get_top_words(get_words_from_xml()))
        else:
            break
