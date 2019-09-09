from openalpr import Alpr

from distutils.core import setup


from distutils.core import setup
import datetime

from cam2 import Stream
from Alpr_sc import AlprRecognition
from zapis import SavePlateResult




alpr = None
try:
        
	Stream().stream_to_photo()
        
    
		

finally:
    if alpr:
        alpr.unload()
