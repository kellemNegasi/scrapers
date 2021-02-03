import pprint
import urllib
import requests
from bs4 import BeautifulSoup as Bsoup
import pandas as pd
import json


def get_result(url):
    res = requests.get(url)
    default = 'Not Available'
    soup = Bsoup(res.content, 'html.parser')
    items = soup.find_all('li', attrs={'class': 'ais-InfiniteHits-item'})
    courses = list()
    for item in items:
        course = {}
        course_title_src = item.find('h2')
        if course_title_src:
            course_title = course_title_src.get_text()
        else:
            course_title = default
        partner_src = item.find('span', attrs={'class': 'partner-name'})
        if partner_src:
            partner = partner_src.get_text()
        else:
            partner = default
        rating_value_src = item.find('span', attrs={'class': 'ratings-text'})
        if rating_value_src:
            rating_value = rating_value_src.get_text()
        else:
            rating_value = default
        rating_count_src = item.find('span', attrs={'class': 'ratings-count'})
        if rating_count_src:
            rating_count = rating_count_src.get_text()[1:-1]
        else:
            rating_count = default
        enrollment_number_src = item.find('span', attrs={'class': 'enrollment-number'})

        if enrollment_number_src:
            enrollment_number = enrollment_number_src.get_text()
        else:
            enrollment_number = default

        difficulty_level_src = item.find('span', attrs={'class': 'difficulty'})
        if difficulty_level_src:
            difficulty_level = difficulty_level_src.get_text()
        else:
            difficulty_level = default

        item_type_src = item.find('div', attrs={'class': 'product-type-row'})
        if item_type_src:
            item_type = item_type_src.get_text()
        else:
            item_type = default

        course['course_title'] = course_title
        course['partner'] = partner
        course['rating_value'] = rating_value
        course['rating_count'] = rating_count
        course['enrollement_numbers'] = enrollment_number
        course['course_difficulty'] = difficulty_level
        course['type'] = item_type
        courses.append(course)
    return courses


def simple_search(search_phrase='machine learning', return_type='list'):
    ce_url = build_url(search_phrase)
    courses = get_result(ce_url)
    if return_type == 'list':
        return courses
    elif return_type == 'dataframe':
        return pd.DataFrame.from_dict(courses, orient='columns')
    elif return_type == 'json':
        return json.dumps(courses)
    else:
        return courses


def build_url(search_phrase, filters=None):
    base_search_url = 'https://www.coursera.org/search?query='
    search_phrase = search_phrase
    encoded_query = urllib.parse.quote(search_phrase)
    ce_url = base_search_url + encoded_query
    urls = []
    if filters is not None:
        if filters['pages'] is not None:
            pages = filters['pages']
            for page in range(1,pages+1):
                url = ce_url + f'&page={page}&index=prod_all_products_term_optimization&tab=all'
                urls.append(url)
        else:
            pass
        return urls


def advanced_search(search_phrase, filters={'pages': 2}):
    courses = []
    urls = build_url(search_phrase, filters)
    for url in urls:
        courses += get_result(url)
    return courses

results = advanced_search("deep learning", filters={'pages': 3})
print(len(results))
