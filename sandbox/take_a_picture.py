from datetime import datetime
import os
from picamera import PiCamera


def ts():
    dt = datetime.now()
    y, m, d, h, min, s = (str(dt.year), str(dt.month), str(dt.day), str(dt.hour), str(dt.minute), str(dt.second))
    return f"{y}_{m}_{d}_{h}_{min}_{s}"


if __name__ == "__main__":
    if not "pictures" in os.listdir("../"):
        os.makedirs("../pictures")

    camera = PiCamera()
    camera.capture(f"../pictures/{ts()}.jpg")

