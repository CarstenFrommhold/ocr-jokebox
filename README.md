# Pi-Camera-Sonos

just sandboxing... :-) 

## Next Steps

* Dev/Prod Dependencies
* Mnist minimal sample

## Topics covered

* Control Sonos Box via SoCo
* Raspberry Pi Camera Module v2
* Deploy @raspi via PyCharm Deployment (ssh)

## Notes

* Install pyenv on the raspi which is [straightforward](https://github.com/pyenv/pyenv#installation).
* Install [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)
* Install poetry which is also [straightforward](https://python-poetry.org/docs/#installation)

## Camera Module

### Enable camera

```console
sudo raspi-config
```

### Take a picture

```console
raspistill -v -o pic.jpg
```

