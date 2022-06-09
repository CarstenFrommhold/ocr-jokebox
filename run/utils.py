""" WIP
Todo: Replace mock with real photo taken by Raspi
"""
import time
import pytesseract
from PIL import Image
from rapidfuzz import process, fuzz


class Handler:

    def __init__(self):
        self.options = {
            "Coldplay": "https://www.mboxdrive.com/Coldplay_X_BTS_-_My_Universe_Offic_(getmp3.pro).mp3",
            "Guns and Roses": "https://www.mboxdrive.com/Guns-N-Roses-Sweet-Child-O-Mine-Official-Music-Video_1w7OgIMMRc4.mp3",
        }
        self.current_song = None
        self.threshold = 0.75

    def take_picture(self):
        pass

    def delete_picture(self):
        pass

    def ocr(self) -> str:
        img = Image.open("../camera_mock/pic.jpg")
        return pytesseract.image_to_string(img)

    def track_from_img(self, img):
        img_to_str = self.ocr()

        if img_to_str == "":
            return "", 0.01

        nearest_string, confidence, _ = process.extract(
            img_to_str, self.options.keys(), scorer=fuzz.WRatio, limit=1)[0]
        return nearest_string, confidence

    def play_track_on_sonos_box(self, sonos_box, track):
        sonos_box.play_uri(self.options.get(track))
        self.current_song = track

    def run(self, sonos_box):
        while True:
            img = self.take_picture()
            track, confidence = self.track_from_img(img)
            if confidence > self.threshold:
                if track != self.current_song:
                    self.play_track_on_sonos_box(sonos_box, track)
            self.delete_picture()
            time.sleep(5)
