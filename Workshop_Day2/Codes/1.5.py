import cv2

cap = cv2.VideoCapture(0)

while(True):
	ret, frame = cap.read()
	cv2.imshow('Original',frame)
	
	# Uncomment the commented code set to test the various filtering and edge detection methods one by one and check their differences
	
	# (1) with Mean Filtering (Uncomment the code set below to try out)
	'''
	frame_mean = cv2.blur(frame,(11,11))
	# (11,11) above is the kernel (aka filtering) size
	cv2.imshow('Mean',frame_mean)
	'''
	
	# (2) with Gaussian Filtering (Uncomment the code set below to try out)
	'''
	frame_gaussian = cv2.GaussianBlur(frame,(11,11), 0)
	# (11,11) above is the kernel (aka filtering) size
	cv2.imshow('Gaussian',frame_gaussian)
	'''
	
	# (3) with Median Filtering (Uncomment the code set below to try out)
	'''
	frame_median = cv2.medianBlur(frame, 11)
	# 11 above is the kernel (aka filtering) size (11,11)
	cv2.imshow('Median',frame_median)
	'''
	
	# (4) with Canny Edges (frame, minVal, maxVal, Sobel Kernel size)
	# Sobel filtering works by calculating the gradient of image intensity at each pixel within the image
	'''
	frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	frame_canny = cv2.Canny(frame_gray, 10, 30, apertureSize=3)
	cv2.imshow('Canny',frame_canny)
	'''
	
	if cv2.waitKey(1) & 0xff == ord('q'):
		break
		
		
cap.release()

cv2.destroyAllWindows()
