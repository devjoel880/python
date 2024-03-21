import urllib.request
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

service = 'https://restcountries.com/v3.1/name/'

while True:
    country = input('Enter country - ')
    if len(country) < 1:
        break

    country = country.strip()
    res = {"c": country}
    url = service + urllib.parse.urlencode(res)
    url = url[:-9] + country
    print('Retrieving data..')

    try:
        req = urllib.request.urlopen(url, context=ctx)
        data = req.read().decode()

        jsn = json.loads(data)

        # Check if any data is returned
        if not jsn:
            print('Country not found:', country)
            continue

        # Extract country details
        country_name = jsn[0].get("name").get("common")
        country_official = jsn[0].get("name").get("official")
        country_reg = jsn[0].get("region")
        country_sub_reg = jsn[0].get("subregion")
        country_lang = ", ".join(jsn[0].get("languages", []))  # Join languages if present

        # Print country details
        print('Country Name: ', country_name)
        print('Official Name: ', country_official)
        print('Region: ', country_reg, country_sub_reg)
        print('Language: ', country_lang)
        print()

    except urllib.error.HTTPError as e:
        print('HTTP Error:', e.code, e.reason)
    except urllib.error.URLError as e:
        print('URL Error:', e.reason)
    except json.JSONDecodeError as e:
        print('JSON Decode Error:', e)
    except Exception as e:
        print('An error occurred:', e)
