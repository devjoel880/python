# Developed by Dev- Joel while learning Python

import urllib.request, urllib.parse
import json, ssl

key = '&apiKey=7984a54699694596a261db4e805007fb'
service = 'https://api.geoapify.com/v1/geocode/search?'

# To ignore SSL certifiate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True :
    search = input("Enter location : ")
    if len(search) < 1 :
        break
    search = search.strip()
    res = {"text": search} # create a dict() to store the user input
    data = urllib.parse.urlencode(res) # parse and encode the search item the user inputs

    url = service + data + key
    print('Retrieving', url)

    try :
        request = urllib.request.urlopen(url, context=ctx)
        dd = request.read().decode()
        jj = json.loads(dd)

        if not jj :
            print('===== Location Not Found =====')
            continue

        country = jj['features'][0]['properties']['country']
        code = jj['features'][0]['properties']['country_code']
        state = jj['features'][0]['properties']['state']
        state_code = jj['features'][0]['properties']['state_code']
        city = jj['features'][0]['properties']['city']
        lon = jj['features'][0]['properties']['lon']
        lat = jj['features'][0]['properties']['lat']
        fmt = jj['features'][0]['properties']['formatted']
        time = jj['features'][0]['properties']['timezone']['name']

        print('Country:', country)
        print('Country Code', code)
        print('State:', state)
        print('State Code:', state_code)
        print('City', city)
        print('Latitude:', lat, 'Longitude:', lon)
        print('Time Zone:', time)
        print('Formated Address:', fmt)

    except Exception as e:
        print('Error:', e)
