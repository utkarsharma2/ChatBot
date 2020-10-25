from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json

# X & Y Cities classifier
from hra_classifier import search_city

# Email Notification Trigger
from email_notification import trigger_email

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"259c6c6a2158b8da98a654049f0659c7"}
		zomato = zomatopy.initialize_app(config)
		
		loc = tracker.get_slot('location')
		not_supported = "Location Not Supported"

		if search_city(loc) == True:
			return loc
		else:
			return not_supported
		
		location_detail=zomato.get_location(loc, 1)

		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]

		cuisine = tracker.get_slot('cuisine')
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		price_range = tracker.get.slot('price')
		user_email = tracker.get_slot('email_address')
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)),  5)
		d = json.loads(results)
		response=""
		if d['results_found'] == 0:
			response= "No results"
		else:
			for restaurant in d['restaurants']:
				response=response+ "Top 5 "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ restaurant['aggregate_rating'] +"\n"
			
			trigger_email(user_email=user_email, email_body=response)
		
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc)]

