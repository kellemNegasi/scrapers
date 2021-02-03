## ce scraper(coursera scraper)
This is a simple library that helps in getting some data from coursera
which can be used by content aggregators</br>

## usage
### I, installing the packaged distribution from pypi
   ```
   pip install ce-scraper 
   ```
## 1. simple search feature
   this feature gives us the first 10 results of the search</br>
   to perform a simple search..<br>
   first import the ``search_courses`` module and call the </br>
```python
from ce_scraper import search_courses
courses=search_courses.simple_search(search_phrase='machine learning',type='json')
print(courses)
```
##Output
```json
[
   {
      "course_title": "Machine Learning",
      "partner": "Stanford University",
      "rating_value": "4.9",
      "rating_count": "154,848",
      "enrollment_numbers": "3.9m",
      "course_difficulty": "Mixed",
      "type": "COURSE"
   },
   {
      "course_title": "Deep Learning",
      "partner": "DeepLearning.AI",
      "rating_value": "4.8",
      "rating_count": "117,652",
      "enrollment_numbers": "990k",
      "course_difficulty": "Intermediate",
      "type": "SPECIALIZATION"
   },
   {
      "course_title": "Machine Learning",
      "partner": "University of Washington",
      "rating_value": "4.6",
      "rating_count": "14,496",
      "enrollment_numbers": "400k",
      "course_difficulty": "Intermediate",
      "type": "SPECIALIZATION"
   },
   {
      "course_title": "Mathematics for Machine Learning",
      "partner": "Imperial College London",
      "rating_value": "4.6",
      "rating_count": "10,371",
      "enrollment_numbers": "250k",
      "course_difficulty": "Beginner",
      "type": "SPECIALIZATION"
   },
   {
      "course_title": "IBM Machine Learning",
      "partner": "IBM",
      "rating_value": "4.6",
      "rating_count": "211",
      "enrollment_numbers": "11k",
      "course_difficulty": "Intermediate",
      "type": "PROFESSIONAL CERTIFICATE"
   },
   {
      "course_title": "Applied Data Science with Python",
      "partner": "University of Michigan",
      "rating_value": "4.5",
      "rating_count": "28,245",
      "enrollment_numbers": "700k",
      "course_difficulty": "Intermediate",
      "type": "SPECIALIZATION"
   },
   {
      "course_title": "Machine Learning for All",
      "partner": "University of London",
      "rating_value": "4.7",
      "rating_count": "2,290",
      "enrollment_numbers": "80k",
      "course_difficulty": "Beginner",
      "type": "COURSE"
   },
   {
      "course_title": "IBM Data Science",
      "partner": "IBM",
      "rating_value": "4.6",
      "rating_count": "68,872",
      "enrollment_numbers": "740k",
      "course_difficulty": "Beginner",
      "type": "PROFESSIONAL CERTIFICATE"
   },
   {
      "course_title": "Naive Bayes 101: Resume Selection with Machine Learning",
      "partner": "Coursera Project Network",
      "rating_value": "Not Available",
      "rating_count": "Not Available",
      "enrollment_numbers": "Not Available",
      "course_difficulty": "Intermediate",
      "type": "GUIDED PROJECT"
   },
   {
      "course_title": "Advanced Machine Learning",
      "partner": "HSE University",
      "rating_value": "4.4",
      "rating_count": "3,701",
      "enrollment_numbers": "300k",
      "course_difficulty": "Advanced",
      "type": "SPECIALIZATION"
   }
]
```
`search_phrase` is the key word that is used to search the courses</br>
`type` is the type of file we want from the search result.</br>
these are the supported values of `type` on this release.

 i. `list`</br>
 ii. `json` </br>
 iii. `dataframe`</br>

## 2. Advanced Search
To perform the advance search we call the advance search in the search course module <br>
with a dictionary of filters as an argument.
this feature currently supports only page number as a filter.
```python
from ce_scraper import search_courses
courses=search_courses.advanced_search(search_phrase='deep learning', filters={'pages': 2}, type=list)
print(courses)
```
The above code searches with key word `deep learning` and returns the courses 
from two pages result on the coursera page which is around 30 courses. 
More filters and features will be included in the next release of this library.





