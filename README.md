<h1 align="center">flask_snapcraft_example</h1>

## Description
- This is snapcraft example for flask with bootstrap5
- Use psutil to get system information

![ui](https://user-images.githubusercontent.com/4043666/163672226-5a7e5ebb-c09d-4948-9cfa-733e0ebdbb89.PNG)


#### Build
    sudo snapcraft

#### Install
    sudo snap install [snap file] --classic --dangerous

## Build and install Scripts
#### Modify [snap file] in script
```shell
echo "> Start Rebuild"
echo "> Build new APP snap"
sudo snapcraft
echo "> Build Done"
sleep 2
echo ""
echo "> Clean Build"
sudo snapcraft clean
sleep 1
echo ""
echo "> Remove Old APP from installed snap"
sudo snap remove  [snap file]
echo "> Remove Done"
echo ""
echo "> Install new APP SNAP"
sudo snap install [snap file] --classic --dangerous
echo "> DONE"

```

   
## Know Issuse:
- Psutil cannot Read disk and temperature infomaiotn on SNAP service 
<br>(but Psutil can get the infomation in host)
