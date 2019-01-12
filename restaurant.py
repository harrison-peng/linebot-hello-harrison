# -*- coding: utf-8 -*-

from yelpapi import YelpAPI

YELP_API_KEY = os.environ['YELP_API_KEY']

def find_near_restaurant(address):
    try:
        yelp_api = YelpAPI(YELP_API_KEY)
        results = yelp_api.search_query(term='restaurant', location=address, limit=5)['businesses']

        restaurant_list = list()
        for result in results:
            restaurant_item = {
                'name': result['name'],
                'image': result['image_url'],
                'address': result['location']['address1'],
                'url': result['url']
            }
            restaurant_list.append(restaurant_item)
        return restaurant_list
    except Exception as e:
        return e

# print(len(find_near_restaurant('台北市文山區育英街17巷10號')))