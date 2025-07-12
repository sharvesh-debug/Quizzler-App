import requests
d=requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
question_data=d.json()["results"]

