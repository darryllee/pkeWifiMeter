# pkeWifiMeter
A wifi proximity meter themed to function like a Ghostbusters PKE meter using PocketCHIP


sudo apt-get build-dep aircrack-ng
sudo apt-get install libssl-dev
wget http://download.aircrack-ng.org/aircrack-ng-1.2-rc4.tar.gz
tar -zxvf aircrack-ng-1.2-rc4.tar.gz
cd aircrack-ng-1.2-rc4
make
sudo make install

sudo apt-get install git build-essential python-dev python-smbus
cd ~
git clone https://github.com/adafruit/Adafruit_Python_PCA9685.git
cd Adafruit_Python_PCA9685
sudo python setup.py install
