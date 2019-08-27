import sys 
import os
sys.path.append('C:\\Users\\doradigital\\Desktop\\klasowe')
from ApiControler import ApiConector
from PlateRecognitionResult import PlateRecognitionResult


def save_log(log, path):
        file=open(path,'a')
        file.write(log+'\n')
        file.close()

api_connector = ApiConector()
result = api_connector.send_plate_recognition_request(sys.argv[1])
save_log(result.to_string(),'C:\\Users\\doradigital\\Desktop\\wyniki.txt')
