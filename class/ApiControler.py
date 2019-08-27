import requests
import base64
import json
import sys 
import os
sys.path.append('C:\\Users\\doradigital\\Desktop\\klasowe')
from PlateRecognitionResult import PlateRecognitionResult

class ApiConector():
    def __init__(self):
        pass
               

    def prepare_photo(self, image):
        with open(image, 'rb') as image_file:
            img_base64 = base64.b64encode(image_file.read())
        return img_base64

    def send_plate_recognition_request(self, image):
        SECRET_KEY = 'sk_c2953cc32733126b8215bc9d'
        url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=us&secret_key=%s' % (SECRET_KEY)
            
        base64_image = self.prepare_photo(image)
        r = requests.post(url, base64_image)
        json_result = (json.dumps(r.json(), indent=2))
        json_result = json.loads(json_result)
        result = PlateRecognitionResult(json_result) 
        return result
