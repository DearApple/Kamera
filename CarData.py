import sqlite3

class CarData():
	plate_numbers=[]
	owner_name=[]

	def write_base_data(self,plate_numbers,owner_name):
		
		
		con = 'tablice'
		conn = sqlite3.connect(con)
		conn.text_factory = sqlite3.OptimizedUnicode
		cur=conn.cursor()
			

		

		for row in cur.execute('SELECT * FROM Tablice '):
			CarData().plate_numbers.append(row[2])
			CarData().owner_name.append(row[0])
			CarData().owner_name.append(row[1])
			print(CarData().owner_name)

			#print(row)
			#owner_string = ' '.join(row)
			#owner_name.append(owner_string)


CarData().write_base_data(CarData().plate_numbers,CarData().owner_name)		
			
	
