from openalpr import Alpr

from distutils.core import setup


from distutils.core import setup
import datetime
import sqlite3

from cam2 import Stream
from Alpr_sc import AlprRecognition
from zapis import SavePlateResult
from CarData import CarData


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
        	
		Stream().stream_to_photo()
       
    
		

finally:
    if alpr:
        alpr.unload()
