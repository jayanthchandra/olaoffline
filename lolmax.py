import requests,json

def getlat(exactloc):
	url = 'https://maps.googleapis.com/maps/api/geocode/json'
	params = {'sensor': 'false', 'address': exactloc }
	r = requests.get(url, params=params)
	results = r.json()['results']
#print (results)
	loc=[]
	location = results[0]['geometry']['location']
	loc.append(location['lat'])
	loc.append(location['lng'])
	return loc
#location = results[0]['geometry']['location']
# print(location['lat'])
# print(location['lng'])

print("Another Set")

#url='ttps://maps.googleapis.com/maps/api/place/nearbysearch/json'
def predict(address):
	#print(address)
	params={'input' :address,'key' :'AIzaSyCpblu38ttvclkcBvEdgejfJyaqemmLLoo'}
	url='https://maps.googleapis.com/maps/api/place/autocomplete/json'#?input=Kaggis Bakery&types=geocode&key=AIzaSyCpblu38ttvclkcBvEdgejfJyaqemmLLoo'
	r=requests.get(url,params=params)
	result=r.json()['predictions']
	j=[]
	for i in result:
		j.append(i['description'])
	return j