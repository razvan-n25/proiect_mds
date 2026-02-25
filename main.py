import requests
url ="https://api.open-meteo.com/v1/forecast?latitude=44.4323&longitude=26.1063&current_weather=true"
response=requests.get(url)
if response.status_code==200:
	data=response.json()
	temp=data["current_weather"]["temperature"]
	print(f"Succes! Temperatura actuala in Bucuresti este de {temp}.")
else:
	print("Eroare la descarcare")


