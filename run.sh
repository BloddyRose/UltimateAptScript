
echo "      Installing Python3 "
sudo apt-get install python3

echo "      Installing pip3"
sudo apt-get install python3-pip

echo "      Running pip3 on requirements.txt"
sudo pip3 install -r requirements.txt

echo "      Now can run ultimateapt.py with sudo python3 ultimateapt.py"
echo "      Uderstand : Fine I will open it for you"

clear

python3 ultimateapt.py