import time
import hashlib
from urllib.request import urlopen, Request

url = Request('http://localhost:3000/', headers={'User-Agent': 'Mozilla/5.0'})

response = urlopen(url).read()

current_hash = hashlib.sha224(response).hexdigest()

print("running")

time.sleep(10)

while True:
    try:
        response = urlopen(url).read()

        current_hash = hashlib.sha224(response).hexdigest()

        time.sleep(30)

        new_hash = hashlib.sha224

        if new_hash == current_hash:
            continue 
            
        else:
            print("something changed")

            response = urlopen(url).read()

            current_hash = hashlib.sha224(response).hexdigest()

            time.sleep(30)
            continue 
    
    except Exception as e: 
        print("error: ", e)