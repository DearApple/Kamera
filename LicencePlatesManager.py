from openalpr import Alpr

#from zapis import SavePlateResult
from distutils.core import setup
import sqlite3
import datetime
from distutils.core import setup
#from Plate_match import Match
from Car import Car

class LicencePlatesManager():
	cars = []
	def read_plates_from_database(self):
		con = 'tablice'
		conn = sqlite3.connect(con)
		conn.text_factory = sqlite3.OptimizedUnicode
		cur=conn.cursor()	

			

		for row in cur.execute('SELECT * FROM Tablice '):
			x = row[2]
			y = row[1]+" "+row[0]
			u=Car(x,y)
			self.cars.append(u)
			
		

	def plate_match(plate):
		for car in cars:
			if car.plate == plate:
				return True, car
		
		return False, None
		
LicencePlatesManager().read_plates_from_database()



					
					
	
