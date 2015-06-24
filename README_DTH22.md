# DTH22 (temperature & humidity sensor)
# BMP180 Barometer sensor (I2C)
#
#required SW
#python-build-essentials, python-smbus, python-pip
#
#Raspberry pi info
#kernel 3.18.11
#from raspi-config: enable device tree, enable i2c
#
#edit /etc/modules file. Add following lines there: 
#i2c-dev, 
#spidev, 
#bcm2708-rng
