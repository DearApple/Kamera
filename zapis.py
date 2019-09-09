import datetime

class SavePlateResult():
    def __init__(self,result):
        self.plate = result["results"][0]["plate"]
        self.confidence = round(result["results"][0]["confidence"],1)
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.is_valid = len(self.plate)

    def to_string(self):
	if self.is_valid < 7:
		sav = "valid plate"
	else:
        	sav = str(self.date) + " " + str(self.plate) + " " + str(self.confidence)
        	return sav
	
    def save_to_file(self, string):
	path = "/home/doradigital/Desktop/wyniki.txt"
	file=open(path,'a')
        file.write(string+'\n')
        file.close()
