# Pi-Camera-Sonos

Just sandboxing with my sonos box. :)

## Next Steps

* Dev/Prod Dependencies @Raspi

## Topics touched

* Control Sonos Box via SoCo
* Raspberry Pi Camera Module v2
* Deploy @raspi via PyCharm Deployment (ssh)
* Tesseract OCR

## Notes

* Install pyenv on the raspi which is [straightforward](https://github.com/pyenv/pyenv#installation).
* Install [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)
* Install poetry which is also [straightforward](https://python-poetry.org/docs/#installation)

## Links

* [Install tesseract on Raspi](https://www.macheronte.com/en/how-to-install-tesseract-ocr-on-raspberry-pi/)

## Camera Module

### Enable camera

```console
sudo raspi-config
```

### Take a picture

```console
raspistill -v -o pic.jpg
```

