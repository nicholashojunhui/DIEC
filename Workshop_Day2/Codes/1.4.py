import cv2

cap = cv2.VideoCapture(0)

while(True):
	ret, frame = cap.read()
	cv2.imshow('Original',frame)
	
	print(frame.shape)
	
	frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	cv2.imshow('Gray', frame_gray)
	
	if cv2.waitKey(1) & 0xff == ord('q'):
		break
		
		
cap.release()

cv2.destroyAllWindows()
