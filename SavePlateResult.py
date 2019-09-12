
class SavePlateResult():
    def __init__(self,result):
        self.plate = result["results"][0]["plate"]
        self.confidence = round(result["results"][0]["confidence"],1)
        self.is_valid = len(self.plate)



