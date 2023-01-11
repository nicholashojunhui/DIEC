import cv2

cap = cv2.VideoCapture(0)

while(True):
	ret, frame = cap.read()
	cv2.imshow('Original',frame)
	
	print(frame.shape)
	
	img_resized = cv2.resize(frame, (320, 240), cv2.INTER_LINEAR)
	
	cv2.imshow('Resized', img_resized)
	
	if cv2.waitKey(1) & 0xff == ord('q'):
		break
		
		
cap.release()

cv2.destroyAllWindows()
