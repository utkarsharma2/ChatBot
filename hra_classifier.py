cities_x = [
    "Ahmedabad", 
    "Bengaluru", 
    "Chennai", 
    "Delhi", 
    "Hyderabad", 
    "Kolkata", 
    "Mumbai", 
    "Pune",
    "Agra", 
    "Ajmer",
    "Aligarh", 
    "Amravati", 
    "Amritsar", 
    "Asansol", 
    "Aurangabad", 
    "Bareilly"]
cities_y = [
    "Belgaum Bhavnagar Bhiwandi Bhopal Bhubaneswar Bikaner Bilaspur Bokaro-Steel-City Chandigarh Coimbatore Cuttack Dehradun Dhanbad Bhilai Durgapur Dindigul Erode Faridabad Firozabad Ghaziabad Gorakhpur Gulbarga Guntur Gwalior Gurgaon Guwahati Hamirpur Hubli–Dharwad Indore Jabalpur Jaipur Jalandhar Jammu Jamnagar Jamshedpur Jhansi Jodhpur Kakinada Kannur Kanpur Karnal Kochi Kolhapur Kollam Kozhikode Kurnool Ludhiana Lucknow Madurai Malappuram Mathura Mangalore Meerut Moradabad Mysore Nagpur Nanded Nashik Nellore Noida Patna Pondicherry Purulia Prayagraj Raipur Rajkot Rajahmundry Ranchi Rourkela Salem Sangli Shimla Siliguri Solapur Srinagar Surat Thanjavur Thiruvananthapuram Thrissur Tiruchirappalli Tirunelveli Ujjain Bijapur Vadodara Varanasi Vasai-Virar City Vijayawada Visakhapatnam Vellore Warangal"
]

cities_y = cities_y[0].split()

classified_cities = cities_x + cities_y

def search_city(city_name):
    if city_name in classified_cities:
        return True
    else:
        return False