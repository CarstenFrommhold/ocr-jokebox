from datetime import datetime
import os
import time
from picamera import PiCamera


def ts():
    dt = datetime.now()
    y, m, d, h, min, s = (str(dt.year), str(dt.month), str(dt.day), str(dt.hour), str(dt.minute), str(dt.second))
    return f"{y}_{m}_{d}_{h}_{min}_{s}"


def take_a_picture(camera: PiCamera, path: str = "../pictures"):
    camera.capture(f"{path}/{ts()}.jpg")


def record(camera: PiCamera, len_: int = 5, path: str = "../clips"):
    camera.start_recording(f"{path}/{ts()}.h264")
    time.sleep(len_)
    camera.stop_recording()


if __name__ == "__main__":
    if not "pictures" in os.listdir("../"):
        os.makedirs("../pictures")
    # if not "clips" in os.listdir("../"):
    #     os.makedirs("../clips")

    camera = PiCamera()
    camera.resolution = (640, 480)  # optional
    camera.rotation = 180

    take_a_picture(camera)


