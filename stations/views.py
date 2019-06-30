from django.shortcuts import render
from opencage.geocoder import OpenCageGeocode
import requests

def Stations(request):
    # hardcoded the paths into the .html file 
    
    return render(request, 'stations/stations.html')
    
def PassengerDetails(request):    
    # Hits the open-notify API and returns the astronauts currently on the ISS
    response = requests.get("http://api.open-notify.org/astros.json")
    data = response.json()
    people = data['people']
    temp = []
   
    for i in range(0, len(people)):
        temp.append(people[i]['name'])
        
    result = temp
    
    return render(request, 'stations/isspassenger.html', {'result': result})

def IssLocation(request):
    # API request to open-notify for lat/long of ISS
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()
    location = data['iss_position']
    
    # Reverse_geocodes the lat/long using opencage API
    key = '3a3f13fb513541f79345ff8a0eebbe1d'
    geocoder = OpenCageGeocode(key)
    reverse_geocode = geocoder.reverse_geocode(location['latitude'], location['longitude'])
    
    # Ocassionally goeocoding doesn't work, hence error handling
    try:
        result = reverse_geocode[0]['formatted']
    except IndexError:
        result = "It's in space. Duh!"
    
    return render(request, 'stations/isslocation.html', {'result': result})
    

