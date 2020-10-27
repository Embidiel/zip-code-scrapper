from bs4 import BeautifulSoup
import requests

zipncrpage = 'https://www.eltechs.com.ph/zipcode/mm.htm'
feature = 'html.parser'

response = requests.get(zipncrpage);
soup = BeautifulSoup(response.text, feature)

zipcodesrawhtml = soup.findAll("td", {"class": "Zcode"})
zipcodes = list(map(lambda zipcodehtml :  zipcodehtml.text, zipcodesrawhtml))

locationrawhtml = soup.findAll("td", {"class": "Zitem"})
locations = list(map(lambda loc :  loc.text, locationrawhtml))

ziplocation = {}

for zipcode, location in zip(zipcodes, locations):
    ziplocation[zipcode] = location;

print(ziplocation)