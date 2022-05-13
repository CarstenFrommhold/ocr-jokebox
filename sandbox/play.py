from soco import SoCo

if __name__ == '__main__':
    sonos = SoCo('192.168.178.23')
    sonos.play_uri(
        'http://ia801402.us.archive.org/20/items/TenD2005-07-16.flac16/TenD2005-07-16t10Wonderboy.mp3')
    track = sonos.get_current_track_info()
    print(track['title'])
    sonos.pause()
    sonos.play()
