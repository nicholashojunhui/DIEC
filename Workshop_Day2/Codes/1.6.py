import cv2

cap = cv2.VideoCapture(0)

while(True):
	ret, frame = cap.read()
	cv2.imshow('Original',frame)
	
	frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	
	face_dect = face.detectMultiScale(frame_gray, scaleFactor=1.3, minNeighbors=2)
	
	frame_face = frame.copy()
	for (x,y,w,h) in face_dect:
		cv2.rectangle(frame_face, (x,y), (x+w,y+h), (0,255,0),2)
		
	cv2.imshow('frame_face', frame_face)
	
	if cv2.waitKey(1) & 0xff == ord('q'):
		break
		
		
cap.release()

cv2.destroyAllWindows()
