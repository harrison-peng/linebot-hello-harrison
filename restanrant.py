# -*- coding: utf-8 -*-

from yelpapi import YelpAPI

YELP_API_KEY = os.environ['YELP_API_KEY']

# Defaults for our simple example.
DEFAULT_TERM = 'restaurant'
DEFAULT_LOCATION = 'No. 1, Section 4, Roosevelt Rd, Da’an District, Taipei City, Taiwan 10617'
SEARCH_LIMIT = 5


yelp_api = YelpAPI(YELP_API_KEY)
result = search_results = yelp_api.search_query(term=DEFAULT_TERM, location=DEFAULT_LOCATION, limit=5)

print(result['businesses'][0])