import urllib.request, urllib.parse, urllib.error
import json, ssl

#ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

service = 'https://restcountries.com/v3.1/name/'

while True:
    country = input('Enter country - ')
    if len(country) < 1: break
    country = country.strip()
    res = dict()
    res["c"] = country
    url = service + urllib.parse.urlencode(res)
    url = url[:-9] + country
    print('Retrieving data..')

    req = urllib.request.urlopen(url, context=ctx)
    data = req.read().decode()

    try:
        jsn = json.loads(data)
    except:
        jsn = None

    country_name = jsn[0].get("name").get("common")
    country_official = jsn[0].get("name").get("official")
    country_reg = jsn[0].get("region")
    country_sub_reg = jsn[0].get("subregion")
    country_lang = ", ".join(jsn[0].get("languages", []))  # Join languages if present

    print('Country Name: ', country_name)
    print('Official Name: ', country_official)
    print('Region: ', country_reg, country_sub_reg)
    print('language: ', country_lang)
