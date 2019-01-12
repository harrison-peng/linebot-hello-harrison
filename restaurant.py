# -*- coding: utf-8 -*-

from yelpapi import YelpAPI

# YELP_API_KEY = os.environ['YELP_API_KEY']

# def find_near_restaurant(address):
#     try:
#         TERM = 'restaurant'
#         SEARCH_LIMIT = 5

#         yelp_api = YelpAPI(YELP_API_KEY)
#         results = search_results = yelp_api.search_query(term=TERM, location=address, limit=5)['businesses']

#         restaurant_list = list()
#         for result in results:
#             restaurant_item = {
#                 'name': result['name'],
#                 'image': result['image_url'],
#                 'address': result['location']['address1'],
#                 'url': result['url']
#             }
#             restaurant_list.append(restaurant_item)
#         return restaurant_list
#     except Exception as e:
#         return e