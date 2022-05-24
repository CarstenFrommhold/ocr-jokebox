import time
import random
from typing import Any, Tuple


class Camera:

    def take_a_picture(self) -> Any:
        return ...


class Model:

    def predict(self, pic: Any) -> Tuple[float, str]:
        return random.random(), "blur"


class SonosWrapper:

    def play(self, song):
        print(f"Play song {song}")


if __name__ == "__main__":

    cam = Camera()
    clf = Model()
    box = SonosWrapper()

    while True:
        pic = cam.take_a_picture()
        proba, prediction = clf.predict(pic)

        if proba > 0.5:
            box.play(prediction)
            time.sleep(5)
            continue
        print("Not sure.")
        continue
