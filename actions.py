from __future__ import absolute_import, division, unicode_literals

import json
import smtplib

from rasa_sdk import Action
from rasa_sdk.events import SlotSet

import zomatopy
# Email Notification Trigger
from email_notification import trigger_email
# X & Y Cities classifier
from hra_classifier import search_city

CITIES = ['Ahmedabad', 'Bengaluru', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai', 'Pune', 'Agra', 'Ajmer', 'Aligarh', 'Amravati', 'Amritsar', 'Asansol', 'Aurangabad', 'Bareilly', 'Belgaum', 'Bhavnagar', 'Bhiwandi', 'Bhopal', 'Bhubaneswar', 'Bikaner', 'Bilaspur', 'Bokaro Steel City', 'Chandigarh', 'Coimbatore', 'Cuttack', 'Dehradun', 'Dhanbad', 'Bhilai', 'Durgapur', 'Dindigul', 'Erode', 'Faridabad', 'Firozabad', 'Ghaziabad', 'Gorakhpur', 'Gulbarga', 'Guntur', 'Gwalior', 'Gurgaon', 'Guwahati', 'Hamirpur', 'Hubli–Dharwad', 'Indore', 'Jabalpur', 'Jaipur', 'Jalandhar', 'Jammu', 'Jamnagar', 'Jamshedpur', 'Jhansi', 'Jodhpur', 'Kakinada', 'Kannur', 'Kanpur', 'Karnal', 'Kochi', 'Kolhapur', 'Kollam', 'Kozhikode', 'Kurnool', 'Ludhiana', 'Lucknow', 'Madurai', 'Malappuram', 'Mathura', 'Mangalore', 'Meerut', 'Moradabad', 'Mysore', 'Nagpur', 'Nanded', 'Nashik', 'Nellore', 'Noida', 'Patna', 'Pondicherry', 'Purulia', 'Prayagraj', 'Raipur', 'Rajkot', 'Rajahmundry', 'Ranchi', 'Rourkela', 'Salem', 'Sangli', 'Shimla', 'Siliguri', 'Solapur', 'Srinagar', 'Surat', 'Thanjavur', 'Thiruvananthapuram', 'Thrissur', 'Tiruchirappalli', 'Tirunelveli', 'Ujjain', 'Bijapur', 'Vadodara', 'Varanasi', 'Vasai-Virar City', 'Vijayawada', 'Visakhapatnam', 'Vellore', 'Warangal']
NOT_OPERATED_CITY = "We do not operate in that area yet."
PRICE_RANGE = {
	"high" : {
		"start" : 700,
		"end" : float('inf')
	},
	"mid" : {
		"start" : 300,
		"end" : 700
	},
	"low" : {
		"start" : 0,
		"end": 300
	}
}
class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def is_valid_city(self, name):
		"""only in Tier-1 and Tier-2 cities"""
		for city in CITIES:
			if city.lower() == name.lower():
				return True
		return False

	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"259c6c6a2158b8da98a654049f0659c7"}
		zomato = zomatopy.initialize_app(config)
		
		loc = tracker.get_slot('location')
		if not self.is_valid_city(loc):
			dispatcher.utter_message(NOT_OPERATED_CITY)
			return [SlotSet('location',None)]

		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]

		cuisine = tracker.get_slot('cuisine')
		cuisines_dict={'american':1, "mexican" : 73, 'chinese':25, 'italian':55,'north indian':50,'south indian':85}
		
		# results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine.lower())), 20)
		# d = json.loads(results)
		restaurants = self.get_data(lat, lon, str(cuisines_dict.get(cuisine.lower())))
		response = ""
		if len(restaurants) == 0:
			response = "no results"
		else:
			# Sorting done on API side with params : order=desc&sort=rating
			price_range = PRICE_RANGE.get(tracker.get_slot('price').lower())
			restaurants = self.filter(restaurants, price_range)
			response = self.format_results(restaurants)
		dispatcher.utter_message("Found Results: \n\n", response)
		return [SlotSet('location',loc), SlotSet('results',response)]

	def format_results(self, restaurants):
		response = ""
		for restaurant in restaurants:
				response = response + restaurant['restaurant']['name'] +\
				" in " +\
				restaurant['restaurant']['location']['address'] + " has been rated " +\
				restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n"
		return response

	def filter(self, restaurants, price_range):
		result = []
		for rest in restaurants[0]:
			if rest['restaurant']["average_cost_for_two"] >= price_range["start"] and rest['restaurant']["average_cost_for_two"] <= price_range["end"]: 
				result.append(rest) 
		
		if len(result) == 0:
			return restaurants[0][:5]
		
		if len(result) <= 5:
			return result
		
		return result[:5]

	def get_data(self, lat, lon, cuisine):
		config={ "user_key":"259c6c6a2158b8da98a654049f0659c7"}
		zomato = zomatopy.initialize_app(config)
		restaurants = []
		page_size = 20
		for count in range(5):
			results=zomato.restaurant_search("", lat, lon, cuisine, page_size, page_size*count)
			d = json.loads(results)
			if d['results_found'] == 0:
				break
			restaurants.append(d["restaurants"])
		return restaurants

class ActionSendResults(Action):
	"""Custom action class to sent results via emails"""
	sent_from = ("upgradassignment2020@gmail.com", "tztbxoaropfwtsub")

	def name(self):
		return 'action_send_results'
	
	def run(self, dispatcher, tracker, domain):
		email = tracker.get_slot('email_address')
		result = tracker.get_slot('results')
		self.trigger_email(to=email, email_body=result)
		dispatcher.utter_message("Search results sent to " + email)

	def trigger_email(self, to, email_body=""):
		
		subject = 'Your Restaurent test results'
		message = 'Subject: {}\n\n{}'.format(subject, email_body)
		try:
			server = smtplib.SMTP_SSL('smtp.gmail.com:465')		
			server.ehlo()
			server.login(self.sent_from[0], self.sent_from[1])
			server.sendmail(self.sent_from[0],to, message)
			server.close()
		except Exception as e:
			print(e)

if __name__ == "__main__":
	object = ActionSendResults()
	object.trigger_email("utkarsharma2@gmail.com", "test")