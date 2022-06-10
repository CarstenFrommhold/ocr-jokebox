import time
import pytesseract
from PIL import Image
from rapidfuzz import process, fuzz
import os


class Handler:

    def __init__(self):
        self.options = {
            "Coldplay": "https://www.mboxdrive.com/Coldplay_X_BTS_-_My_Universe_Offic_(getmp3.pro).mp3",
            "Guns and Roses": "https://www.mboxdrive.com/Guns-N-Roses-Sweet-Child-O-Mine-Official-Music-Video_1w7OgIMMRc4.mp3",
            "Queen": "https://www.mboxdrive.com/Queen%20-%20Another%20One%20Bites%20The%20Dust.mp3",
            "Daftpunk": "https://www.mboxdrive.com/daft-punk-something-about-us-official-audio.mp3"
        }
        self.current_song = None
        self.threshold = 0.75

    def shot(self):
        img = Image.open("../camera_mock/pic.jpg")  # mock
        return img

    def del_(self):
        try:
            os.remove("tmp/pic.jpg")
        except:
            pass

    def ocr(self, img) -> str:
        return pytesseract.image_to_string(img)

    def track_from_img(self, img):
        img_to_str = self.ocr(img)

        if img_to_str == "":
            return "", 0.01

        nearest_string, confidence, _ = process.extract(
            img_to_str, self.options.keys(), scorer=fuzz.WRatio, limit=1)[0]

        return nearest_string, confidence

    def play_track_on_sonos_box(self, sonos_box, track):
        sonos_box.play_uri(self.options.get(track))
        self.current_song = track

    def run(self, sonos_box):
        print("Write down what you want to hear...")
        while True:
            try:
                os.makedirs("tmp")
            except:
                pass
            img = self.shot()
            track, confidence = self.track_from_img(img)
            if confidence > self.threshold:
                if track != self.current_song:
                    self.current_song = track
                    print(f"Playing {track}")
                    self.play_track_on_sonos_box(sonos_box, track)
            self.del_()
            time.sleep(1)
