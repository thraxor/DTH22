# DTH22 (temperature & humidity sensor)
#=======================================
# Link to BMP instructions: https://learn.adafruit.com/mcp4725-12-bit-dac-with-raspberry-pi/configuring-your-pi-for-i2c
# Link to DTH instructions:  
#
# Installed SW & HW
# 1. Raspberry pi SW (05-05-2015, kernel 3.18.11)
# 2. Install the following packages (form apt-get):
# 2.1 build-essential, python-smbus, python-pip, python-dev
# 2.2 Download the following libraries from github: Adafuit-BMP and Adafruit-DTH
#     - git clone https://github.com/adafruit/Adafruit_Python_BMP.git
#     - git clone 
# required SW
#build-essential, python-smbus, python-pip, python-dev
#
#Raspberry pi info
#kernel 3.18.11
#from raspi-config: enable device tree, enable i2c
#
#edit /etc/modules file. Add following lines there: 
#i2c-dev, 
#spidev, 
#bcm2708-rng
