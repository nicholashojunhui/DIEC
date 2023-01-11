from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()


camera.rotation = 180
sleep(1)
camera.stop_preview()

camera.capture('/home/pi/Desktop/test.jpg')
