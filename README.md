<h1 align="center">flask_snapcraft_example</h1>

## Description
- This is snapcraft example for flask with bootstrap5
- Use psutil to get system information


## Build SNAP By Command 
#### Step 1. Build
```  shell
sudo snapcraft
```

#### Step 2. Install SNAP
``` shell
sudo snap install [snap file] --classic --dangerous
```

#### Step 3. Check On Web
``` 
http://[Your IP]:1234/
```

## Build SNAP By Scripts
#### Step 1. Modify [snap file] in script
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

#### Step 2. Execxute script
``` shell
cd [example folder]
sh rebuild.sh
```
   
## Run web Application Without SNAP
``` shell
sh stopsnap.sh
cd Flask 
python3 runserver.py
```
Note: Need to stop/remove App SNAP

## Web UI Example (SNAP)
![ui](https://user-images.githubusercontent.com/4043666/163672226-5a7e5ebb-c09d-4948-9cfa-733e0ebdbb89.PNG)


## Know Issuse:
- Psutil cannot Read disk and temperature infomaiotn on SNAP service 
<br>(but Psutil can get the infomation in host)
