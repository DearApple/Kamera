from Alpr_sc import AlprRecognition
import cv2
import time
import base64


class Stream():
	def stream_to_photo(self):
		    cap = cv2.VideoCapture("rtsp://admin:admin123@192.168.2.240:554/ISAPI/Streaming/channels/102")
		    _, frame1 = cap.read()
		    succ, encode_frame = cv2.imencode('.jpg',frame1)
		    frame=encode_frame.tobytes()
		    
		 
		 
		    #cv2.imshow(('Camera'+str(88)), frame)
		     
		 
		 
		   # k = cv2.waitKey(0) & 0xFF
		    #if k == 27: #esc key ends process
			#cap.release()
			#break
		    
		  
		    cap.release()
		    AlprRecognition().photo_convert(encode_frame)

