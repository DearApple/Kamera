import requests
import base64
import json
import datetime
import sys 
import os
# Sample image file is available at http://plates.openalpr.com/ea7the.jpg
#IMAGE_PATH = 'C:\\Users\\doradigital\\Desktop\\snapshots\\test_044.jpg'
SECRET_KEY = 'sk_c2953cc32733126b8215bc9d'

photo = sys.argv[1]

with open(photo, 'rb') as image_file:
    img_base64 = base64.b64encode(image_file.read())

url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=us&secret_key=%s' % (SECRET_KEY)
r = requests.post(url, data = img_base64)

result = (json.dumps(r.json(), indent=2))

#print(result)
result = json.loads(result)

plate = result["results"][0]["plate"]
confidence =str( round(result["results"][0]["confidence"],1))
date= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#print(plate)
#print(confidence)
#print(date)

tosave=[date,plate,confidence]
#path to savefile
file=open('C:\\Users\\doradigital\\Desktop\\wyniki.txt','a')
file.write(''.join(date)+' ')
file.write(''.join(plate)+' ',)
file.write(''.join(confidence)+'\n')
file.close()
