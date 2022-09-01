import picamera
import time

path = '/home/pi/src'
camera = picamera.PiCamera()

try:
    camera.resolution = (640, 480)
    camera.start_preview()
    time.sleep(5)
    while True:
        print("photo:1, video:2, exit:9 > ", end='')
        inp = int(input())
        if inp == 1:
            print("사진 촬영")
            now_str = time.strftime("%Y%m%d_%H%M%S")
            camera.capture('%s/photo_%s.jpg' % (path, now_str))
            
        elif inp == 2:
            print("동영상 촬영")
            now_str = time.strftime("%Y%m%d_%H%M%S")
            camera.start_recording('%s/video_%s.h264' % (path, now_str))
            time.sleep(3)
            camera.stop_recording()
        elif inp == 9:
            break
        else:
            print("incorrect command")

finally:
    camera.stop_preview()