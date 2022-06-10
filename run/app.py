from soco import SoCo
from utils import Handler
# from picamera import PiCamera


class CameraMock:

    def capture(self, *args):
        pass


handler = Handler()

if __name__ == "__main__":

    # camera = PiCamera()
    # camera.resolution = (640, 480)
    # camera.vflip = True
    camera = CameraMock()

    sonos_box = SoCo('192.168.178.23')
    handler.run(sonos_box, camera)
