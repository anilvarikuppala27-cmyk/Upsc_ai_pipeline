import requests

url = "https://pib.gov.in"

response = requests.get(url)

print("Status Code:", response.status_code)

print(response.text[:500])
