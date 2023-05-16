import requests
import time

while True:
    response = requests.get('http://service1:5000/helloworld')
    print(response.text)
    time.sleep(5)