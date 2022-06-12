from soco import SoCo

SONOS_IP = '192.168.178.23'


if __name__ == "__main__":

    sonos_box = SoCo(SONOS_IP)
    sonos_box.stop()
