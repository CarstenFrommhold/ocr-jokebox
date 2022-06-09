from soco import SoCo
from utils import Handler


handler = Handler()

if __name__ == "__main__":

    sonos_box = SoCo('192.168.178.23')
    handler.run(sonos_box)
