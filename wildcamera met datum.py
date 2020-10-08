from gpiozero import MotionSensor
from picamera import PiCamera 
from datetime import datetime

pir = MotionSensor(4)
camera = PiCamera()
filename = "{0:%c}".format(datetime.now())

while True:
    pir.wait_for_motion()
	print("Motion detected!")
	camera.start_recording(filename)
	pir.wait_for_no_motion()
	camera.stop_recording() 