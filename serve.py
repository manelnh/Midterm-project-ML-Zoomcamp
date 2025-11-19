
import requests

url="http://localhost:8000/predict"


patient =  {
 "age": 65,
 "sex": "m",
 "chestpaintype": "asy",
 "restingbp": 160,
 "cholesterol": 0,
 "fastingbs": 1,
 "restingecg": "st",
 "maxhr": 122,
 "exerciseangina": "n",
 "oldpeak": 1.2,
 "st_slope": "flat"}


response = requests.post(url, json=patient).json()
print(response)




