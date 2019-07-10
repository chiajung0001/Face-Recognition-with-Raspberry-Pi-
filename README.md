# Face Recognition with Raspberry Pi 3B+
在樹梅派3B+ 安裝與應用face_recognition

using face_recognition with raspberry pi 3B+

![image](https://github.com/chiajung0001/Face_Recognition_with_Raspberry_Pi_3B/blob/master/face_recognition%20with%20raspberry%20pi%203B%2B.png)



Expand Filesystem
```
sudo raspi-config
```
選擇Advanced Option -> A1 Expanded Filesystem > Reboot

安裝相關軟件
```
sudo apt-get update && sudo apt-get upgrade -y 
sudo apt-get install git -y \
    wget -y \
    curl -y \
    zip -y \
    build-essential cmake unzip pkg-config -y \
    libjpeg-dev libpng-dev libtiff-dev -y \
    libavcodec-dev libavformat-dev libswscale-dev libv4l-dev -y \
    libxvidcore-dev libx264-dev -y \
    libgtk-3-dev -y \
    libcanberra-gtk* -y \
    libatlas-base-dev gfortran -y \
    python3-dev -y
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

重新命名
```
mv opencv-4.1.0 opencv
mv opencv_contrib-4.1.0 opencv_contrib
```

刪除壓縮檔案
```
rm -f opencv.zip opencv_contrib.zip
```

為Python3架設虛擬環境
```
sudo pip install virtualenv virtualenvwrapper
sudo pip3 install virtualenv virtualenvwrapper
sudo rm -rf ~/get-pip.py ~/.cache/pip
```

更新〜/ .profile文件
```
nano ~/.profile
```

加上以下代碼
```
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
```
按CTRL + X按鈕，然後按確認Y保存〜/ .profile文件

使用~/.profile
```
source ~/.profile
```

建立一個虛擬環境並取名, 例如cv
```
mkvirtualenv cv -p python3
```

進入cv虛擬環境
```
workon cv
```


安裝NumPy(在虛擬環境中)
```
pip install numpy
```

離開虛擬環境
```
deactive
```

配置OpenCV CMake
```
cd ~/opencv
mkdir build
cd build
```

執行以下cmake命令(需要一段時間)
```
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
    -D ENABLE_NEON=ON \
    -D ENABLE_VFPV3=ON \
    -D BUILD_TESTS=OFF \
    -D OPENCV_ENABLE_NONFREE=ON \
    -D INSTALL_PYTHON_EXAMPLES=OFF \
    -D BUILD_EXAMPLES=OFF ..
```

增加內存
```
sudo nano /etc/dphys-swapfile
```
更改為CONF_SWAPSIZE=2048

啟用新的swap
```
sudo dphys-swapfile setup
sudo dphys-swapfile swapon
```

編譯OpenCV(花費約4~5小時)
```
make -j4
```

安裝
```
sudo make install
sudo ldconfig
```

連接OpenCV到虛擬環境
```
sudo ln -s  /usr/local/lib/python3.5/site-packages/cv2/python-3.5/cv2.cpython-35m-arm-linux-gnueabihf.so ~/.virtualenvs/cv/lib/python3.5/site-packages/cv2.so
```

測試OpenCV
```
workon cv
python
>>> import cv2
>>> cv2.__version__
>>> exit()
```
如回傳安裝版本編號如4.1.0代表OpenCV安裝成功


安裝face_recognition及相關套件在虛擬環境(dlib約需要2小時)
```
workon cv
pip install dlib
pip install face_recognition
pip install imutils
pip install opencv-python
```

如果安裝face_recognition錯誤，請用以下方式手動安裝
```
wget https://www.piwheels.org/simple/face-recognition-models/face_recognition_models-0.3.0-py2.py3-none-any.whl
pip install face_recognition_models-0.3.0-py2.py3-none-any.whl
pip install --upgrade face_recognition
```

如果使用樹梅派相機配件請開啟相機並在虛擬環境(cv)安裝以下套件
```
sudo raspi-config
```
Interfacing Option -> P1 Camera

```
sudo apt-get install python3-picamera
sudo pip install --upgrade picamera[array]
```


下載人臉辨識範例
```
git clone --single-branch https://github.com/ageitgey/face_recognition.git
```

測試範例程式
```
cd ./face_recognition/examples
python facerec_on_raspberry_pi.py
```


 
參考網站

face_recognition套件(內容詳細):
https://github.com/ageitgey/face_recognition

樹梅派安裝指南:

https://www.teknotut.com/en/install-opencv-4-on-the-raspberry-pi/

https://www.teknotut.com/en/facial-recognition-with-raspberry-pi-and-opencv/
