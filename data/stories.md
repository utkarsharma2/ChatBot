## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
* restaurant_search{"price": "Mid"}
    - slot{"price": "Mid"}
    - utter_ask_cuisine
* restaurant_search{"price": "mid", "cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_goodbye
    - export

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"price": "Mid"}
    - slot{"price": "Mid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* restaurant_search{"price": "mid", "location": "delhi"}
    - slot{"location": "delhi"}
    - slot{"price": "mid"}
* affirm
    - utter_goodbye

## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search{"price": "High"}
    - slot{"price": "High"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye

## interactive_story_3
* greet
    - utter_greet
* restaurant_search{"price": "mid", "location": "mumbai"}
    - slot{"location": "mumbai"}
    - slot{"price": "mid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* affirm
    - utter_goodbye

## interactive_story_4
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "price": "mid"}
    - slot{"cuisine": "italian"}
    - slot{"price": "mid"}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* affirm
    - utter_goodbye

## interactive_story_5
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* restaurant_search{"price": "Low"}
    - slot{"price": "Low"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye

## interactive_story_6
* greet
    - utter_greet
