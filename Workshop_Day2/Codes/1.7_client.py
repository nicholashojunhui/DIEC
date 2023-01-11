import cv2
import pickle
import socket
import struct

# Replace this with your server IP address
ip = '192.168.XX.XX'
port = 12345

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip, port))
print('Connected to server')
connection = s.makefile('wb')



try:
	cap = cv2.VideoCapture(0)
	img_counter = 0
	
	encode_param = [int(cv2.IMWRITE_JPEG_QUALITY),90]
	
	while True:
	    ret, frame = cap.read()
	
	    result, frame = cv2.imencode('.jpg',frame, encode_param)    
	
	#frame_resize = cv2.resize(frame,(320,240),cv2.INTER_LINEAR)
	
	    data = pickle.dumps(frame, 0)
	    size = len(data)
	
	    s.sendall(struct.pack(">L", size) + data)
	    img_counter += 1
	
	
finally:
	print('Sent')
	s.close()