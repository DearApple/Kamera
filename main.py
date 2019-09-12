from openalpr import Alpr

from distutils.core import setup

from distutils.core import setup

from openalpr import Alpr

import time
import datetime
import sqlite3
import cv2
import time
import base64
import threading

from LicencePlatesManager import LicencePlatesManager
from SavePlateResult import RecognitionResult
from Car import Car


def recognize(image):
			alpr = Alpr("eu", "/etc/openalpr/openalpr.conf", "/usr/share/openalpr/runtime_data")
				
			#if not alpr.is_loaded():
				#print("Error loading OpenALPR")
			#else:
				#print("Using OpenALPR " + alpr.get_version())

				#alpr.set_top_n(7)
				#alpr.set_default_region("eu")
				#alpr.set_detect_region(False)

			jpeg_bytes = image.tobytes()
			results = alpr.recognize_array(jpeg_bytes)
			
			if len(results["results"])>0:
 				recognition_results = RecognitionResult(results)
				print("dobrze")
				return True, recognition_results
				
			else:
				print("zle")
				return False, None

def StringPrepare(recognition_result,car): 
	date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  	
	
	string = str(date) + " " + str(recognition_result.plate) + " " + str(recognition_result.confidence)
	if car:
		string +=" " + Car().owner
		
	return string
	
			
def SaveResult(string):    
		path = "/home/doradigital/Desktop/wyniki.txt"
		file=open(path,'a')
		file.write(string+'\n')
		file.close()
		print("zapis")

def jpg_from_stream(stream):
		    
		    _, frame = stream.read()
		    succ, jpg_frame = cv2.imencode('.jpg',frame)
		  		    
		    return jpg_frame
         	
		    
			
plate_manager = LicencePlatesManager()
plate_manager.read_plates_from_database()

stream = cv2.VideoCapture("rtsp://admin:admin123@192.168.2.240:554/ISAPI/Streaming/channels/102")

while True:		
	starttime=time.time()
		#zbierane klatek
	jpg_frame = jpg_from_stream(stream)
		#konwersja
	rec_success, recognition_results = recognize(jpg_frame)
		#rozpoznanie
	if rec_success:
		match_success, recognized_car = plate_manager.plate_match(recognition_results.plate)
		
		string = StringPrepare(recognition_results,recognized_car)
		SaveResult(string)
	time.sleep(1.0-(time.time()-starttime))
