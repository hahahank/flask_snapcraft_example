# flask_snapcraft_example
This is snapcraft example for flask with bootstrap5
Use psutil to get CPU/RAM/DISK and system temperature



#### Building
    sudo snapcraft

#### Install
    sudo snap install [.snap file] --classic --dangerous
    
    
## Know Issuse:
Psutil cannot Read disk and temperature infomaiotn on SNAP service
(but Psutil can get the infomation in host)
