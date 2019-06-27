# Face-Recognition-with-Raspberry-Pi
using face_recognition with raspberry pi 3 B+
在樹梅派3 B+ 安裝與應用face_regnition

Expand Filesystem
```
sudo raspi-config
```
選擇Advanced Option -> A1 Expanded Filesystem > R

安裝相關軟件
```
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install build-essential cmake unzip pkg-config -y
sudo apt-get install libjpeg-dev libpng-dev libtiff-dev -y
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev -y
sudo apt-get install libxvidcore-dev libx264-dev -y
sudo apt-get install libgtk-3-dev -y
sudo apt-get install libcanberra-gtk* -y
sudo apt-get install libatlas-base-dev gfortran -y
sudo apt-get install python3-dev -y
```

下載OpenCV
可以在官網查看最新版本 https://opencv.org/releases/
```
cd ~
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.1.0.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.1.0.zip
```

解壓縮
```
unzip opencv.zip
unzip opencv_contrib.zip
```

