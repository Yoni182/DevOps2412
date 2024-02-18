from datetime import datetime
import requests
print(datetime.now())

response = requests.get("https://github.com")
url = ["https://github.com", "https://google.com", "https://random.dog/"]
if response.status_code == 200:
    print("github is up!")