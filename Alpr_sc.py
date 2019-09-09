from openalpr import Alpr

from zapis import SavePlateResult
from distutils.core import setup

import datetime
from distutils.core import setup

class AlprRecognition():

	def photo_convert(self,frame):
		

		alpr = Alpr("eu", "/etc/openalpr/openalpr.conf", "/usr/share/openalpr/runtime_data")
			
		if not alpr.is_loaded():
			print("Error loading OpenALPR")
		else:
			print("Using OpenALPR " + alpr.get_version())

			alpr.set_top_n(7)
			alpr.set_default_region("eu")
			alpr.set_detect_region(False)

			jpeg_bytes = frame.tobytes()
			results = alpr.recognize_array(jpeg_bytes)
			if results["results"]:
				
				SavePlateResult(results).save_to_file(SavePlateResult(results).to_string())
			else:
				print("Bad photo")
