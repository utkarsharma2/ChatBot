## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "Delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Chennai](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican](cuisine)
- can you book a table in [rome](location) in a [moderate]{"entity": "price", "value": "mid"} price range with [North Indian](cuisine) food for [four]{"entity": "people", "value": "4"} people
- can you book a table in [mumbai](location) in a [moderate]{"entity": "price", "value": "mid"} price range with [South Indian](cuisine) food for [four]{"entity": "people", "value": "4"} people
- can you book a table in [Kolkata](location) in a [high](price) price range with [American](cuisine) food for [four]{"entity": "people", "value": "4"} people
- can you book a table in [Calcutta](location) in a [high](price) price range with [American](cuisine) food for [four]{"entity": "people", "value": "4"} people
- can you book a table in [Chennai](location) in a [low](price) price range with [Italian](cuisine) food for [four]{"entity": "people", "value": "4"} people
- find me a [mid](price) range restaurants in [delhi](location)
- locate [high](price) range restaurants in [Hyderabad](location)
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [Pune](location)
- [mumbai](location)
- [Kolkata](location)
- [Hyderabad](location)
- [Chennai](location)
- [Ahmedabad](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- can you find me a [Italian](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- please show me a few [American](cuisine) restaurants in [Hyderabad](location)
- [mid](price)
- [high](price)
- [low](price)
- [moderate]{"entity": "price", "value": "mid"}
- find me
- find me a restaurant
- [Mid](price)
- find me a restaurant in [mid](price) range in [delhi](location)
- [High](price)
- find me [mid](price) range restaurant in [mumbai](location)
- find me an [italian](cuisine) restaurant in [mid](price) range
- find me a restaurant in [delhi](location)
- [Low](price)

## synonym:4
- four

## synonym:Delhi
- New Delhi

## synonym:Kolkata
- Calcutta

## synonym:bangalore
- Bengaluru

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:mid
- moderate

## synonym:mumbai
- Bombay

## synonym:vegetarian
- veggie
- vegg

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}
