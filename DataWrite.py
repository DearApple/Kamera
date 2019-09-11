from CarData import CarData	
import sqlite3

class WriteData():	
	def write_base_data():
			
			
			con = 'tablice'
			conn = sqlite3.connect(con)
			conn.text_factory = sqlite3.OptimizedUnicode
			cur=conn.cursor()
			print("PPOP")	

			

			for row in cur.execute('SELECT * FROM Tablice '):
				x = row[2]
				y = row[1]+" "+row[0]
				tab=[]
				u=CarData(x,y)
				tab.append(u)
				print("PPOP")
				#CarData().plate_numbers.append(row[2])
				#CarData().owner_name.append(row[0])
				#CarData().owner_name.append(row[1]

				#print(row)
				#owner_string = ' '.join(row)
				#owner_name.append(owner_string)

WriteData().write_base_data
	

