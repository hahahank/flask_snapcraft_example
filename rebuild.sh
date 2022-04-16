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
