from soco import SoCo
from utils import Handler
import os


SONOS_IP = '192.168.178.23'


class CameraMock:

    def capture(self, *args):
        pass


handler = Handler()

if __name__ == "__main__":

    if os.uname()[1] == 'raspberrypi':
        from picamera import PiCamera
        camera = PiCamera()
        camera.resolution = (640, 480)
        camera.rotation = 180
    else:
        camera = CameraMock()

    sonos_box = SoCo(SONOS_IP)
    handler.run(sonos_box, camera)
