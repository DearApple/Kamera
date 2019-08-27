import json
import datetime


class PlateRecognitionResult():
    def __init__(self,json_result):
        self.result = json_result["results"][0]["plate"]
        self.confidence = round(json_result["results"][0]["confidence"],1)
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.is_valid = len(self.result)== 7
        
    def to_string(self):
        string = str(self.date) + " " + str(self.result) + " " + str(self.confidence)
        return string
