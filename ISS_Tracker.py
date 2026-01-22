import requests


def get_iss_location():
    response = requests.get('http://api.open-notify.org/iss-now.json')
    data = response.json()
    lat = data['iss_position']['latitude']
    lon = data['iss_position']['longitude']
    print(f"The ISS is currently at Lat: {lat}, Lon: {lon}")
    return float(lat), float(lon)


def get_user_location():
    response = requests.get('https://ipinfo.io/loc')  # raw text string output
    # The reason it wouldn't do anything at first is because I missed the https:// in the link. Whoops
    lat_str, lon_str = response.text.strip().split(',')  # gives clean value.
    return float(lat_str), float(lon_str) # The values from the website come in as strings so needs to be converted into floats


from math import radians, sin, cos, asin, sqrt


def calculate_distance(lat1, lon1, lat2, lon2):
    # decimal degree convert to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # this has been found on stackoverflow. Not the radius of the earth but the formula execution. https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
    return c * r

user_lat, user_lon = get_user_location()  # Call get user location function
iss_lat, iss_lon = get_iss_location()  # call Iss location function and assign both to their variables

distance = calculate_distance(user_lat, user_lon, iss_lat, iss_lon)  # distance calculation


# All the output stuff:
print(f"I am at {user_lat}, {user_lon}")
print(f"ISS is at {iss_lat}, {iss_lon}")
print(f"distance is {distance:.2f}km ")

if distance < 500:
    print("ISS is within 500 km")