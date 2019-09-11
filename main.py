from openalpr import Alpr

from distutils.core import setup

from distutils.core import setup

import datetime
import sqlite3
import cv2
import time
import base64

from cam2 import Stream
from Alpr_sc import AlprRecognition
from zapis import SavePlateResult
from CarData import CarData

def stream_to_photo():
		    cap = cv2.VideoCapture("rtsp://admin:admin123@192.168.2.240:554/ISAPI/Streaming/channels/102")
		    _, frame = cap.read()
		    succ, encode_frame = cv2.imencode('.jpg',frame)
		  
		    cap.release()			
		    AlprRecognition().photo_convert(encode_frame)

def write_base_data():
			
			
			con = 'tablice'
			conn = sqlite3.connect(con)
			conn.text_factory = sqlite3.OptimizedUnicode
			cur=conn.cursor()	

			

			for row in cur.execute('SELECT * FROM Tablice '):
				x = row[2]
				y = row[1]+" "+row[0]
				tab=[]
				u=CarData(x,y)
				tab.append(u)
				


alpr = None
try:
	write_base_data()
	while True:
        	
		stream_to_photo()
       
    
		

finally:
    if alpr:
        alpr.unload()
