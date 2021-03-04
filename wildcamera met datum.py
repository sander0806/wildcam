from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime
import time

pir = MotionSensor(4)
camera = PiCamera()

while True: 
    pir.wait_for_motion() 
    print("Beweging Gedecteerd") 
    timestamp = datetime.now().strftime("%c") 
    camera.start_recording("/home/pi/Desktop/verander.dit.naar.je.eigen.map!/{}.h264".format(timestamp))
    time.sleep(60)
    camera.stop_recording()
