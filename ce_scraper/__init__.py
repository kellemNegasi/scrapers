import urllib
import pprint
import requests
from bs4 import BeautifulSoup as Bsoup

def get_items(search_phrase='machine learning'):
    base_search_url ='https://www.coursera.org/search?query='
    search_phrase = search_phrase
    encoded_query =urllib.parse.quote(search_phrase)
    ce_url = base_search_url+search_phrase
    res = requests.get(ce_url)
    soup = Bsoup(res.content,'html.parser')
    items = soup.find_all('li',attrs={'class':'ais-InfiniteHits-item'})
    courses = list()
    for item in items:
        course ={}
        course_title = item.find('h2').get_text()
        partner = item.find('span',attrs={'class':'partner-name'}).get_text()
        rating_value = item.find('span',attrs ={'class':'ratings-text'}).get_text()
        rating_count =item.find('span',attrs ={'class':'ratings-count'}).get_text()
        enrollment_number = item.find('span',attrs={'class':'enrollment-number'}).get_text()
        difficulty_level = item.find('span',attrs={'class':'difficulty'}).get_text()
        item_type = item.find('div'  ,attrs={'class' :'product-type-row'}).get_text()
        course['course_title'] =course_title
        course['partner'] = partner
        course['rating_value'] = rating_value
        course['rating_count'] = rating_count[1:-1]
        course['enrollement_numbers'] = enrollment_number +' students'
        course['course_difficulty'] = difficulty_level
        course['type'] = item_type
        courses.append(course)
    return courses